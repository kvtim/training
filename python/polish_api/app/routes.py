from app import app


@app.route("/api/test")
def test():
    # insert data
    # CRUD.insert(Country(name='Poland'))
    # return CRUD.select_by_id(Country, 1).name

    # select data by id
    # country = CRUD.select_by_id(Country, 1)
    # return country

    # select all data
    # countries = CRUD.select_all(Country)
    # return countries[0].name

    # update
    # CRUD.update(Country, 1, name='Pl')
    # return CRUD.select_by_id(Country, 1).name

    # CRUD.update(Country, 1, name='Poland')
    # return CRUD.select_by_id(Country, 1).name

    # delete
    #  CRUD.delete(CRUD.select_by_id(Country, 2))
    # return 'deleted'

    # CRUD.insert(Country(name='Poland'))

    return 'test'


@app.route("/api/consulates")
def get_consulates():
    return 'consulates'


@app.route("/api/vac")
def get_visa_centers():
    return 'vacs'


@app.route("/api/news")
def get_news():
    return 'news'


@app.route("/api/vac_and_consulates")
def get_visa_centers_and_consulates():
    return 'vac and consulates'


@app.route("/api/all_data")
def get_all_data():
    return 'all data'
