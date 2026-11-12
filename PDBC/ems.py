import pymysql

dbConnection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="ems"
)

print(dbConnection)
print("Database Connected Successfully")

def register():
    