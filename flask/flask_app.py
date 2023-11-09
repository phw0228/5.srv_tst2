from flask import Flask, jsonify
import mysql.connector

app1 = Flask(__name__)

def employee_data():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db', #container name
        'port': '3306',
        'database': 'employees'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT Employee_Name, Title FROM employee_data')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

@app1.route('/')
def index():
    return jsonify({'Employee Data': employee_data()})

if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')
