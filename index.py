import os
import mysql.connector
from dotenv import load_dotenv
import pandas as pd
import time

load_dotenv(".env.database")  

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


print(DB_PASSWORD)





def get_db_connection():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    return conn

def get_cursor():
    mydb = get_db_connection()
    mycursor = mydb.cursor()
    return mycursor, mydb




cursor , db = get_cursor()



query = "select * from ecommerce_py.users join login_signup_1.users;"
try:
    cursor.execute(query)            
    result = cursor.fetchall()
    
    columns = []
    for column_name in cursor.description:
        columns.append(column_name[0])
        

    df = pd.DataFrame(result, columns=columns)

    fname = f"{time.time()}data.xlsx"
    df.to_excel(fname, index=False)

    
        
except mysql.connector.Error as err:
    print(f"Error: {err}")
    error = err

finally:
    cursor.close()
    db.close() 









# Create table users (id int primary key AUTO_INCREMENT , username varchar(100) unique not null , password varchar(200) not null , time_created bigint not null);
# Create table blogs (id int primary key AUTO_INCREMENT , title varchar(200) not null , body text not null , image varchar(200) null , created_by int not null , time_created bigint not null , time_modified bigint not null);