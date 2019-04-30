import pyodbc
connection = 'Microsoft SQL Server'
server = 'localhost,1433'
database = 'python_sql'
username = 'SA'
password = 'Passw0rd2018'

docker_python_sql = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = docker_python_sql.cursor()

def add_order_sort(food, quantity, price, origin):
    query = f"INSERT INTO food_order_table(name_of_food, quantity, price, origin) VALUES ('{food}','{quantity}','{price}','{origin}')"
    nocount = """SET NOCOUNT ON;"""
    cursor.execute(nocount + query)

add_order_sort('nachos', 1, 10.00, 'america')