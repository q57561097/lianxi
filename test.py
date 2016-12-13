import mysql.connector
conn = mysql.connector.connect( user = 'root', passwd = 'password')
cursor=conn.cursor()
try:
    cursor.execute('create database yh')
except:
    print('Database addtest exists!')