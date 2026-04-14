import mysql.connector

print("Program started")

try:
    db = mysql.connector.connect(
        host="127.0.0.1",   # ✅ avoid localhost
        user="root",
        password="root",
        port=3306,
        auth_plugin='mysql_native_password',  # 🔥 force old auth
        connection_timeout=5
    )

    print("Connected Successfully")

except Exception as e:
    print("ERROR:", e)