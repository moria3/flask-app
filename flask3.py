from flask import Flask
import pymysql

app = Flask(__name__)

def get_data_from_db():
    conn = pymysql.connect(
        host='host.docker.internal',
        user='root',
        password='change-me',
        database='Northwind',
        port=3306
    )

    cursor = conn.cursor()

    query = "SELECT * FROM Customers where Country='portugal'"

    cursor.execute(query)

    data = cursor.fetchall()

    # Close the cursor, but don't commit as you're only reading data
    cursor.close()

    # Close the connection
    conn.close()

    return data

@app.route('/')
def index():
    data = get_data_from_db()
    
    combined_data = "\n".join(str(row) for row in data)
    
    return combined_data

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5200)

