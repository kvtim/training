from pyspark.sql import SparkSession
import re
from datetime import datetime as dt
from pyspark import Row
from pyspark.sql import functions as F
from pyspark.sql import types as T

appName = 'formatter'
master = 'local'


def df_to_dict(df):
    return list(map(lambda row: row.asDict(), df.collect()))


def parse_consulates(consulates):
    spark = SparkSession.builder \
        .master(master) \
        .appName(appName) \
        .getOrCreate()

    df = spark.createDataFrame([Row(**i) for i in consulates])

    df = df.withColumn('address', F.regexp_replace(df.address, '\d+, г. ', ''))
    df = df.withColumn('city', F.split(df.address, ',').getItem(0)) \
        .withColumn('phone1', F.regexp_replace(F.split(df.phone, ',').getItem(0), ' ', '')) \
        .withColumn('phone2', F.regexp_replace(F.split(df.phone, ',').getItem(1), ' ', '')) \
        .drop('phone')

    return df_to_dict(df)


def parse_vacs(visa_centers):
    spark = SparkSession.builder \
        .master(master) \
        .appName(appName) \
        .getOrCreate()
    df = spark.createDataFrame([Row(**i) for i in visa_centers])

    df = df.withColumn('address', F.udf(lambda a: format_address(a))(df.address))
    df = df.withColumn('address', F.concat_ws(', ', df.city, df.address))

    return df_to_dict(df)


def parse_news(all_news):
    spark = SparkSession.builder \
        .master(master) \
        .appName(appName) \
        .getOrCreate()
    df = spark.createDataFrame([Row(**i) for i in all_news])

    df = df.withColumn('link', F.regexp_replace(df['link'], r'^https?:\/\/', '')) \
        .withColumn('date',
                    F.udf(lambda d: dt.strptime(d, '%Y-%m-%d').strftime('%d-%m-%Y'), T.StringType())
                    (F.col('date')))

    return df_to_dict(df)


def multiple_replace(dict, text):
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


def format_address(address):
    regex_dict = {'улица': 'ул.',
                  'Улица': 'ул.',
                  'Ул.': 'ул.',
                  'проспект': 'пр.'}
    formatted = multiple_replace(regex_dict, address)
    formatted = re.sub(r'^(.*)(?=ул.|пр.)', '', formatted)
    formatted = re.sub(r'(?<=[.,])(?=[^\s])', r' ', formatted)
    formatted = re.match(r'.+?(?=\d)\d+\S', formatted).group().strip(',')
    formatted = formatted.split()
    if not formatted[1].endswith(','):
        formatted[1] += ','
    formatted = ' '.join(formatted)
    return formatted
