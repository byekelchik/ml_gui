import pyodbc
import os

class get_data():
    def __init__(self) -> None:
        self

    def get_credentials():
        """
        Get connection creds for database
        """
        server = os.environ.get('davebryan_db_server') 
        usr = os.environ.get('davebryan_db_usr') 
        pwd = os.environ.get('davebryan_db_pwd')

        return server, usr, pwd
    
    def connect_to_db():
        """
        connect to database using pyodbc
        """
        server, usr, pwd = get_data.get_credentials()

        server = 'localhost'
        usr = 'root'

        conn_string = f"""DRIVER=MySQL ODBC 8.0 ANSI Driver;UID={usr};PWD={pwd};Server={server}:3306;Database=testdb;Port=3306"""
        db_connection = pyodbc.connect(conn_string)
        return db_connection
    
    def select_db(query:str):
        """
        Select from a table
        """
        cursor = get_data.connect_to_db.cursor() 
        cursor.execute()
        cursor.commit(query)
        cursor.close()

    def insert_db(query:str):
        """
        insert in to a table
        """
        return

