import pyodbc
connection = 'Microsoft SQL Server'
server = 'localhost,1433'
database = 'python_sql'
username = 'SA'
password = 'Passw0rd2018'

docker_python_sql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = docker_python_sql.cursor()

def add_order_sort(food, quantity, price, origin):
    try:
        query = f"INSERT INTO food_order_table(name_of_food, quantity, price, origin) VALUES('{food}', {quantity}, {price}, '{origin}');"
        cursor.execute(query)
        docker_python_sql.commit()
        print('The table has been updated, 1 row affected')
    except:
        print('There has been a error, record has not been committed')

def add_spartan(name_of_student, phone_number, course, trainer):
    try:
            query = f"INSERT INTO sparta_table(name_of_student, phone_number, course, trainer) VALUES('{name_of_student}', {phone_number}, '{course}', '{trainer}');"
            cursor.execute(query)
            docker_python_sql.commit()
            print('The table has been updated, 1 row affected')
    except:
        print('There has been a error, record has not been committed')