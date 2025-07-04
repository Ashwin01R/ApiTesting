from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# SQL Server connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=zddevcad54;"
    "DATABASE=WSS_Content_Ziconnect;"
    "UID=spdevadmin_sql;"
    "PWD=Test$321"
)

@app.route('/add-data', methods=['POST'])
def add_data():
    data = request.json
    name = data.get('name')
    age = data.get('age')

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO APITest (Name, Age) VALUES (?, ?)", (name, age))
        conn.commit()
        return jsonify({"message": "Data inserted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


