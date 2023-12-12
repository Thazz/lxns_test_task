import os
import psycopg2
from items import EstateItem

class DbHandler:
    def __init__(self):
        self.table_name = "estates"
        self.dbname = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PWD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.connection = None
       
        
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to the database.")
        except psycopg2.Error as e:
            print(f"Unable to connect to the database. Error: {e}")
       
    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            print("Disconnected from the database.")    
            
    def create_items_table(self):
        if self.connection is None or self.connection.closed:
            print("Not connected to the database.")
            return   
            
        print("Connection OK.")     
        create_query = f"CREATE TABLE IF NOT EXISTS {self.table_name} (\
                id SERIAL PRIMARY KEY,\
                name TEXT,\
                price TEXT,\
                locality TEXT,\
                image_urls TEXT[])"  
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(create_query)
                self.connection.commit()
                print(f"Table {self.table_name} created.")
        except psycopg2.Error as e:
            print(f"Error creating the table: {e}")
                    
    def delete_items(self):
        if self.connection is None or self.connection.closed:
            print("Not connected to the database.")
            return
        query = f"DELETE FROM {self.table_name}"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")
            
            
    def select_items(self) -> list:
        if self.connection is None or self.connection.closed:
            print("Not connected to the database.")
            return
        
        query = f"SELECT * FROM {self.table_name}"
        try:
            print(f"Executing query: {query}")
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                items = cursor.fetchall()
                return items
        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")


    def insert_item(self,  item: EstateItem):
        if self.connection is None or self.connection.closed:
            print("Not connected to the database.")
            return
        
        query = f"INSERT INTO {self.table_name} (name, price, locality, image_urls) VALUES (%s, %s, %s, %s)"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query,(item["name"], item["price"], item["locality"], item["image_urls"]))
                self.connection.commit()
        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")
            