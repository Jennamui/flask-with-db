import sqlite3
import pandas as pd

def get_db_connection():
    conn = sqlite3.connect('patients1.db')
    conn.row_factory = sqlite3.Row
    return conn

db = get_db_connection()
patientList = db.execute('SELECT * FROM patient_table').fetchall()
patientList

# save the data to a dataframe
df = pd.DataFrame(patientList)
df

# rename the columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob', 'ssn', 'streetadress', 'zipcode', 'city']
df