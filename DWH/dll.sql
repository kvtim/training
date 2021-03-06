CREATE TABLE DIM_CAR (
	SK_CAR SERIAL PRIMARY KEY NOT NULL,
	VIN_CODE CHAR(17) NOT NULL,
	MODEL VARCHAR(50) NOT NULL,
	ISSUE_YEAR DATE NOT NULL,
	BRAND VARCHAR(30) NOT NULL,
	FROM_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	END_DATE TIMESTAMP DEFAULT '9999-12-31',
	IS_CURRENT SMALLINT DEFAULT 1
);

CREATE UNIQUE INDEX UNIQUE_SK_CAR
ON DIM_CAR(SK_CAR);

CREATE INDEX ON DIM_CAR (VIN_CODE, (lower(MODEL)), (lower(BRAND)));

CREATE OR REPLACE TRIGGER UPDATE_DIM_CAR 
	BEFORE UPDATE ON DIM_CAR
    FOR EACH ROW 
	EXECUTE PROCEDURE UPDATE_DIM_TYPE_2('DIM_CAR');
	
	
	

CREATE TABLE DIM_MANAGER (
	SK_MANAGER SERIAL PRIMARY KEY NOT NULL,
	EMP_CODE VARCHAR(3) NOT NULL,
	FIRSTNAME VARCHAR(30) NOT NULL,
	LASTNAME VARCHAR(30) NOT NULL,
	DEPT VARCHAR(3) NOT NULL,
	HIRE_DATE DATE NOT NULL,
	FROM_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	END_DATE TIMESTAMP DEFAULT '9999-12-31',
	IS_CURRENT SMALLINT DEFAULT 1
);

CREATE UNIQUE INDEX UNIQUE_SK_MANAGER
ON DIM_MANAGER(SK_MANAGER);
						 
CREATE INDEX ON DIM_MANAGER (EMP_CODE, (lower(LASTNAME)));

CREATE OR REPLACE TRIGGER UPDATE_DIM_MANAGER 
	BEFORE UPDATE ON DIM_MANAGER
	FOR EACH ROW 
	EXECUTE PROCEDURE UPDATE_DIM_TYPE_2('DIM_MANAGER');
	
	
	
CREATE TABLE DIM_CLIENT (
	SK_CLIENT SERIAL PRIMARY KEY NOT NULL,
	PASS_CODE VARCHAR(3) NOT NULL,
	FIRSTNAME VARCHAR(30) NOT NULL,
	LASTNAME VARCHAR(30) NOT NULL,
	BIRTHDAY DATE NOT NULL,
	TEL VARCHAR(20) NOT NULL,
	CITY VARCHAR(30) NOT NULL,
	EMAIL VARCHAR(30) NOT NULL,
	FROM_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	END_DATE TIMESTAMP 	DEFAULT '9999-12-31',
	IS_CURRENT SMALLINT DEFAULT 1
);

CREATE UNIQUE INDEX UNIQUE_SK_CLIENT
ON DIM_CLIENT(SK_CLIENT);

CREATE INDEX ON DIM_CLIENT (PASS_CODE, (lower(LASTNAME)));

CREATE OR REPLACE TRIGGER UPDATE_DIM_CLIENT 
	BEFORE UPDATE ON DIM_CLIENT
    FOR EACH ROW 
	EXECUTE PROCEDURE UPDATE_DIM_TYPE_2('DIM_CLIENT');



CREATE TABLE DIM_STORAGE (
	SK_STORAGE SERIAL PRIMARY KEY NOT NULL,
	STORAGE_ID SERIAL NOT NULL,
	CITY VARCHAR(30) NOT NULL,
	STREET VARCHAR(50) NOT NULL,
	BUILDING VARCHAR(5) NOT NULL,
	TEL VARCHAR(20) NOT NULL,
	PARKING_LOT_COUNT INT DEFAULT 0 CHECK (PARKING_LOT_COUNT >= 0),
	AREA INT NOT NULL
);

CREATE UNIQUE INDEX UNIQUE_SK_STORAGE
ON DIM_STORAGE(SK_STORAGE);

CREATE UNIQUE INDEX UNIQUE_STORAGE_ID
ON DIM_STORAGE(STORAGE_ID);

CREATE INDEX ON DIM_STORAGE ((lower(CITY)), (lower(STREET)));

						 

CREATE TABLE DIM_DATE (
	SK_SALES_DATE SERIAL PRIMARY KEY NOT NULL,
	DATE_ID SERIAL NOT NULL,
	MONTH SMALLINT NOT NULL CHECK (MONTH BETWEEN 1 AND 12),
	DAY_OF_WEEK SMALLINT NOT NULL CHECK (DAY_OF_WEEK BETWEEN 1 AND 7),
	QUARTER SMALLINT NOT NULL CHECK (QUARTER BETWEEN 1 AND 4),
	WEEK_OF_YEAR INT NOT NULL,
	IS_HOL BOOL NOT NULL
);

CREATE UNIQUE INDEX UNIQUE_SK_SALES_DATE
ON DIM_DATE(SK_SALES_DATE);

CREATE UNIQUE INDEX UNIQUE_DATE_ID
ON DIM_DATE(DATE_ID);


CREATE OR REPLACE TRIGGER UPDATE_DIM_DATE
	BEFORE UPDATE ON DIM_DATE
	FOR EACH ROW
	EXECUTE PROCEDURE UPDATE_DIM_TYPE_0();



CREATE TABLE DIM_SHOW_ROOM (
	SK_SHOW_ROOM SERIAL PRIMARY KEY NOT NULL,
	SHOW_ROOM_NAME VARCHAR(30) NOT NULL,
	CITY VARCHAR(30) NOT NULL,
	STREET VARCHAR(50) NOT NULL,
	BUILDING VARCHAR(5) NOT NULL,
	PREV_TEL VARCHAR(20),
	CURRENT_TEL VARCHAR(20) NOT NULL,
	TEL_UPDATE_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX UNIQUE_SK_SHOW_ROOM
ON DIM_SHOW_ROOM(SK_SHOW_ROOM);

CREATE UNIQUE INDEX UNIQUE_SHOW_ROOM_NAME
ON DIM_SHOW_ROOM(SHOW_ROOM_NAME);
						 
CREATE INDEX ON DIM_SHOW_ROOM (SHOW_ROOM_NAME, (lower(CITY)), (lower(STREET)));
						 


CREATE OR REPLACE TRIGGER UPDATE_DIM_TYPE_3
	BEFORE UPDATE OF CURRENT_TEL
	ON DIM_SHOW_ROOM
	FOR EACH ROW
	EXECUTE PROCEDURE UPDATE_DIM_TYPE_3();
	
	
	
CREATE TABLE SNAPSHOT_DATE (
	SK_SNAPSHOT_DATE SERIAL PRIMARY KEY NOT NULL,
	YEAR SMALLINT DEFAULT date_part('year', CURRENT_TIMESTAMP),
	MONTH SMALLINT DEFAULT date_part('month', CURRENT_TIMESTAMP) CHECK (MONTH BETWEEN 1 AND 12),
	DAY SMALLINT DEFAULT date_part('day', CURRENT_TIMESTAMP) CHECK (DAY BETWEEN 1 AND 31),
	FULL_DATE DATE DEFAULT CURRENT_DATE,
	TIME TIME DEFAULT CURRENT_TIME
);

CREATE TABLE MF_ORDER_DATE (
	SK_MF_ORDER_DATE SERIAL PRIMARY KEY NOT NULL,
	YEAR SMALLINT DEFAULT date_part('year', CURRENT_TIMESTAMP),
	MONTH SMALLINT DEFAULT date_part('month', CURRENT_TIMESTAMP) CHECK (MONTH BETWEEN 1 AND 12),
	DAY SMALLINT DEFAULT date_part('day', CURRENT_TIMESTAMP) CHECK (DAY BETWEEN 1 AND 31),
	FULL_DATE DATE DEFAULT CURRENT_DATE,
	TIME TIME DEFAULT CURRENT_TIME
);

CREATE TABLE ST_DELIVERY_DATE (
	SK_ST_DELIVERY_DATE SERIAL PRIMARY KEY NOT NULL,
	YEAR SMALLINT DEFAULT date_part('year', CURRENT_TIMESTAMP),
	MONTH SMALLINT DEFAULT date_part('month', CURRENT_TIMESTAMP) CHECK (MONTH BETWEEN 1 AND 12),
	DAY SMALLINT DEFAULT date_part('day', CURRENT_TIMESTAMP) CHECK (DAY BETWEEN 1 AND 31),
	FULL_DATE DATE DEFAULT CURRENT_DATE,
	TIME TIME DEFAULT CURRENT_TIME
);

CREATE TABLE CLIENT_ORDER_DATE (
	SK_CLIENT_ORDER_DATE SERIAL PRIMARY KEY NOT NULL,
	YEAR SMALLINT DEFAULT date_part('year', CURRENT_TIMESTAMP),
	MONTH SMALLINT DEFAULT date_part('month', CURRENT_TIMESTAMP) CHECK (MONTH BETWEEN 1 AND 12),
	DAY SMALLINT DEFAULT date_part('day', CURRENT_TIMESTAMP) CHECK (DAY BETWEEN 1 AND 31),
	FULL_DATE DATE DEFAULT CURRENT_DATE,
	TIME TIME DEFAULT CURRENT_TIME
);

CREATE TABLE CLIENT_DELIVERY_DATE (
	SK_CLIENT_DELIVERY_DATE SERIAL PRIMARY KEY NOT NULL,
	YEAR SMALLINT DEFAULT date_part('year', CURRENT_TIMESTAMP),
	MONTH SMALLINT DEFAULT date_part('month', CURRENT_TIMESTAMP) CHECK (MONTH BETWEEN 1 AND 12),
	DAY SMALLINT DEFAULT date_part('day', CURRENT_TIMESTAMP) CHECK (DAY BETWEEN 1 AND 31),
	FULL_DATE DATE DEFAULT CURRENT_DATE,
	TIME TIME DEFAULT CURRENT_TIME
);



CREATE TABLE FACT_SALES (
	SK_CAR INTEGER REFERENCES DIM_CAR,
	SK_CLIENT INTEGER REFERENCES DIM_CLIENT,
	SK_MANAGER INTEGER REFERENCES DIM_MANAGER,
	SK_SALES_DATE INTEGER REFERENCES DIM_DATE,
	SK_SHOW_ROOM INTEGER REFERENCES DIM_SHOW_ROOM,
	PRICE NUMERIC NOT NULL CHECK (PRICE >= 0)
);
						 
CREATE INDEX ON FACT_SALES (SK_SALES_DATE, PRICE);



CREATE TABLE FACT_STORAGE_SNAPSHOT (
	SK_CAR INTEGER REFERENCES DIM_CAR,
	SK_STORAGE INTEGER REFERENCES DIM_STORAGE,
	SK_SNAPSHOT_DATE INTEGER REFERENCES SNAPSHOT_DATE,
	DAYS_ON_STORAGE INT NOT NULL CHECK (DAYS_ON_STORAGE >= 0)
);

CREATE INDEX ON FACT_STORAGE_SNAPSHOT (SK_SNAPSHOT_DATE, DAYS_ON_STORAGE);



CREATE TABLE FACT_SALES_PIPELINE (
	SK_CAR INT REFERENCES DIM_CAR,
	SK_CLIENT INT REFERENCES DIM_CLIENT,
	SK_STORAGE INT REFERENCES DIM_STORAGE,
	SK_MF_ORDER_DATE INT REFERENCES MF_ORDER_DATE,
	SK_ST_DELIVERY_DATE INT REFERENCES ST_DELIVERY_DATE,
	SK_CLIENT_ORDER_DATE INT REFERENCES CLIENT_ORDER_DATE,
	SK_CLIENT_DELIVERY_DATE INT REFERENCES CLIENT_DELIVERY_DATE,
	MF_PRICE NUMERIC NOT NULL CHECK (MF_PRICE >= 0),
	DAYS_BTW_CLNT_ORDER_DLVRY INT NOT NULL CHECK (DAYS_BTW_CLNT_ORDER_DLVRY >= 0)
);

CREATE INDEX ON FACT_SALES_PIPELINE (SK_CLIENT_ORDER_DATE, SK_CLIENT_DELIVERY_DATE,
									   MF_PRICE, DAYS_BTW_CLNT_ORDER_DLVRY);
						 
						 




