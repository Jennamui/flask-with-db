from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

def get_db_connection():
    dir = os.getcwd() + '/patients1.db'
    print('dir:', dir)
    conn = sqlite3.connect(dir) 
    conn.row_factory = sqlite3.Row 

    return conn

@app.route('/')
def index():
    db = get_db_connection()
    patientList = db.execute('SELECT * FROM patient_table').fetchall()
    db.close()
    print('patientList:', patientList)
    return render_template('index.html', listPatients=patientList)

@app.route('/patient')
def Patients():
    conn = get_db_connection()
    patientList = conn.execute('SELECT * FROM patient_table').fetchall()
    conn.close()
    print('patientList:', patientList)
    return render_template('index.html', listPatients=patientList)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)