import pyodbc 
import pandas  as pd 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost;'
                      'Database=test;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
sql = 'SELECT * FROM dbo.SystemUser'
df=pd.read_sql(sql,conn)
print(df.head())
