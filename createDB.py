import sqlite3

connect = sqlite3.connect('patients')

db = connect.cursor()

db.execute("DROP TABLE IF EXISTS patient_table")

connect.commit()

#Table
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            ssn CHAR (25) NOT NULL,
            streetaddress (25) NOT NULL,
            zipcode (25) NOT NULL,
            city (25) NOT NULL
        ); """

db.execute(table)
connect.commit()

db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('12345', 'John', 'Smith', '01/01/2000', '123456789', '123 Water St', '12345', 'New York')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('23456', 'Jane', 'Doe', '02/02/2001', '789345627', '100 Circle Rd', '34567','New York')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('34567', 'Mary', 'Smith', '03/03/2002','109563813','1 Rainbow Rd', '38470', 'Stony Brook')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('45678', 'Bob', 'Smith', '04/04/2003','285095643','2 Benjamin Dr', '01903', 'Brooklyn')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('56789', 'Jane', 'Doe', '05/05/2004', '293673456', '34 Forest Ave', '34590', 'Staten Island')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('03746', 'Robert', 'Park', '04/09/2003', '193433656', '678 Toad St', '28750', 'Staten Island')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('20947', 'James', 'Brown', '02/02/2001', '993773316', '86 Forest Ave', '14792', 'New York')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('39579', 'Josh', 'Kim', '03/17/2000', '163673759', '34 Decker Ave', '24550', 'Stony Brook')")

connect.commit()

connect.close()