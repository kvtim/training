CREATE OR REPLACE FUNCTION UPDATE_DIM_TYPE_0()
	RETURNS trigger AS
$PREVENT_UPDATE$
    BEGIN
        RAISE EXCEPTION 'It is type 0, update is forbidden!';
    END;
$PREVENT_UPDATE$ 
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION UPDATE_DIM_TYPE_2() 
	RETURNS trigger AS
$UPDATE_DIM_TYPE_2$
    BEGIN
		IF OLD.IS_CURRENT = 1 THEN
			IF TG_ARGV[0] = 'DIM_CAR' THEN
				INSERT INTO DIM_CAR (VIN_CODE, MODEL, ISSUE_YEAR, BRAND)
				VALUES
				(NEW.VIN_CODE, NEW.MODEL, NEW.ISSUE_YEAR, NEW.BRAND);
			ELSIF TG_ARGV[0] = 'DIM_MANAGER' THEN
				INSERT INTO DIM_MANAGER (EMP_CODE, FIRSTNAME, LASTNAME, DEPT, HIRE_DATE)
				VALUES
				(NEW.EMP_CODE, NEW.FIRSTNAME, NEW.LASTNAME, NEW.DEPT, NEW.HIRE_DATE);
			ELSIF TG_ARGV[0] = 'DIM_CLIENT' THEN
				INSERT INTO DIM_CLIENT (PASS_CODE, FIRSTNAME, LASTNAME, BIRTHDAY, TEL, CITY, EMAIL)
				VALUES
				(NEW.PASS_CODE, NEW.FIRSTNAME, NEW.LASTNAME, NEW.BIRTHDAY, NEW.TEL, NEW.CITY, NEW.EMAIL);
			END IF;
			
			OLD.END_DATE := CURRENT_TIMESTAMP;
			OLD.IS_CURRENT := 0;
		END IF;
		RETURN OLD;
    END;
$UPDATE_DIM_TYPE_2$ 
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION UPDATE_DIM_TYPE_3() 
	RETURNS trigger AS
$UPDATE_DIM_TYPE_3$
    BEGIN
		NEW.PREV_TEL := OLD.CURRENT_TEL;
		NEW.TEL_UPDATE_DATE := CURRENT_TIMESTAMP;
		RETURN NEW;
    END;
$UPDATE_DIM_TYPE_3$ 
LANGUAGE plpgsql;
