import pymysql

dbConnection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="sms"
    )
print(dbConnection)
print("Connected Successfully")

curObj = dbConnection.cursor()

curObj.execute(
    """create table if not exists student(
    id int primary key,
    name varchar(20) not null,
    email varchar(50) unique not Null,
    password varchar(100)
)
"""
)

curObj.execute("SELECT * FROM student")
allStuData = curObj.fetchall()


def dashboard(stud):
    print("1: Edit Profile")
    print("2: Delete Profile")
    print("3: View Profile")

    op = int(input("Select desired option:"))

    def deleteProfile(id):
        q = "delete from student where id = %s"
        data = (id, )
        curObj.execute(q, data)
        dbConnection.commit()
        print("Deleted Successfully")

    def viewProfile(id):
        q = "select * from student where id = %s"
        data = (id, )
        curObj.execute(q, data)
        sData = curObj.fetchone()
        print("You got your data", sData)

    def editProfile(id):
        e = input("Enter modifies email:")
        curObj.execute(
            """
                update student
                set email = %s
                where id = %s
            """, (e, id))
        dbConnection.commit()

        print(f"Student with id {id} got Updated")

    if op == 1:
        editProfile(stud[0])

    elif op == 2:
        deleteProfile(stud[0])

    elif op == 3:
        viewProfile(stud[0])


def login():
    while True:
        curObj.execute("SELECT * FROM student")
        allStuData = curObj.fetchall()
        print(allStuData, "All Students data")

        eLogin = input("Enter email: ")
        pLogin = input("Enter password: ")

        for i in allStuData:
            if i[2] == eLogin:
                if i[3] == pLogin:
                    print("Login Successful ")
                    dashboard(i)
                    return
                else:
                    print("Invalid Password.....Try Again!!!!")
                    break
        else:
            print("Student not Found")
            print("Try Again!!!!")


def register():
    n = input("Enter name here:")
    e = input("Enter email here: ")
    p = input("Enter password here:")
    cp = input("Enter Confirm password:")

    totalStuCount = len(allStuData)

    if p == cp:
        query = "insert into student(id,name,email,password,course) values(%s,%s,%s,%s,%s)"
        data = (totalStuCount+1, n, e, p)

        curObj.execute(query, data)
        dbConnection.commit()

        print("Student registerd successfully....")
    else:
        print("p and cp must be same")


print("1: Register")
print("2: Login")
option = int(input("Select Option:"))

if option == 1:
    register()
if option == 2:
    login()
