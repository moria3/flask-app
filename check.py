import pymysql

# Connect to the database
conn = pymysql.connect(
    host='host.docker.internal',
    user='root',
    password='Moria1701',
    database='project',
    port=3308
)

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries

cursor.execute('''select * from Customers''')


# Fetch all the rows
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)


# Commit the changes
conn.commit()

# Close the connection
conn.close()
