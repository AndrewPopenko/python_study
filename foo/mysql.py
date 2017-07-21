import pymysql

conn = pymysql.connect(host='localhost', user='jump', passwd='secret', db='sakila')
#conn = mysql.connector.Connect(host="localhost", user="jump",
#password="secret", database="sakila")

# Step 3: obtain a cursor
cursor = conn.cursor()
# Step 4: construct and send a query
query = ("SELECT last_name, first_name FROM actor "
"ORDER BY last_name, first_name")
cursor.execute(query)
# Step 5: iterate the results
for row in cursor:
    print("{:<45} {:<45}".format(*row))
# Step 6: clean up
cursor.close()
conn.close()