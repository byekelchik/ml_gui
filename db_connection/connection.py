import pyodbc
import os

class get_data():
    def __init__(self) -> None:
        self

    def get_credentials():
        """
        Get connection creds for database
        """
        server = os.environ.get() 
        usr = os.environ.get() 
        pwd = os.environ.get()
        return server, usr, pwd
    
    def connect_to_db(usr,pwd,server):
        """
        connect to database using pyodbc
        """
        conn_string = f"""DRIVER=MySQL ODBC 8.0 ANSI Driver;UID={usr};PWD={pwd};Server{server}=:3306;Database=testdb;Port=3306"""
        db_connection = pyodbc.connect(conn_string)
        return db_connection
    
    def select_db(db_connection):
        """
        Select from a table
        """
        return

    def insert_db(db_connection):
        """
        insert in to a table
        """
        return

