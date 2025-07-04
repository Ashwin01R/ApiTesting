from flask import Flask, request, jsonify
import pymssql

app = Flask(__name__)

# SQL Server connection details
server = 'zddevcad54'
user = 'spdevadmin_sql'
password = 'Test$321'
database = 'WSS_Content_Ziconnect'

@app.route('/add-data', methods=['POST'])
def add_data():
    data = request.json
    name = data.get('name')
    age = data.get('age')

    try:
        conn = pymssql.connect(server=server, user=user, password=password, database=database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO APITest (Name, Age) VALUES (%s, %s)", (name, age))
        conn.commit()
        conn.close()
        return jsonify({"message": "Data inserted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
