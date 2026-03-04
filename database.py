# Database Class for Bank System Application Created by: Felipe Tlusty

# This class provides methods for interacting with a MySQL database, including creating tables,
# inserting data, fetching data, modifying data, and printing data in a formatted manner.

# The Database class uses the pymysql library to connect to a MySQL database and perform various operations.
# Each method constructs and executes SQL queries based on the provided parameters to manage the data effectively.
# The class also includes error handling and ensures that the database connection is properly closed when done.
# The methods in this class are designed to be used in conjunction with the functions defined in the functions.py module
# to implement the functionality of the Bank System application.

import pymysql

class Database():
    # Initialize the database connection and create the database if it doesn't exist
    def __init__(self, dbName, serverName, username, password):
        self.dbName = dbName
        db = pymysql.connect(host=serverName, user=username, passwd=password)
        cursor=db.cursor()
        self.db = db
        self.cursor = cursor
        cursor.execute("CREATE DATABASE IF NOT EXISTS {};".format(dbName))
        cursor.execute("USE {};".format(dbName))

    # Create a table with specified columns and data types
    def createTable(self, tableName, **columns):
        sql = "CREATE TABLE IF NOT EXISTS {} (".format(tableName)
        for column, dataType in columns.items():
            sql += "{} {}, ".format(column, dataType)
        sql = sql[:-2] + ");"
        self.cursor.execute(sql)
        self.db.commit()

    # Insert data into a specified table
    def insertData(self, tableName, **data):
        sql = "INSERT INTO {} (".format(tableName)
        columns = []
        values = []
        for column, value in data.items():
            columns.append(column)
            values.append("'{}'".format(value))
        for i in columns:
            sql += "{}, ".format(i)
        sql = sql[:-2] + ") VALUES ("
        for v in values:
            sql += "{}, ".format(v)
        sql = sql[:-2] + ");"
        #print(sql)
        self.cursor.execute(sql)
        self.db.commit()

    # Fetch data from a specified table with optional conditions
    def fetchData(self, tableName, conditions=None):
        sql = "SELECT * FROM {} WHERE ".format(tableName)
        if conditions:
            for column, value in conditions.items():
                sql += "{}='{}' AND ".format(column, value)
            sql = sql[:-5] + ";"
        else:
            sql = "SELECT * FROM {};".format(tableName)
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    # Fetch a specific entry from a table based on conditions and return a specific column or all columns
    def fetchEntry(self, tableName, conditions, columnName = "*"):
        sql = "SELECT {} FROM {} WHERE ".format(columnName, tableName)
        for column, value in conditions.items():
            sql += "{}='{}' AND ".format(column, value)
        sql = sql[:-5] + ";"
        self.cursor.execute(sql)
        if columnName == "*":
            return str(self.cursor.fetchone())[1:-1]
        return str(self.cursor.fetchone())[1:-2]

    # Retrive all data from a specified table
    def viewData(self, tableName):
        sql = "SELECT * FROM {};".format(tableName)
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    # Delete data from a specified table based on conditions
    def deleteData(self, tableName, conditions):
        sql = "DELETE FROM {} WHERE ".format(tableName)
        for column, value in conditions.items():
            sql += "{}='{}' AND ".format(column, value)
        sql = sql[:-5] + ";"
        self.cursor.execute(sql)
        self.db.commit()

    # Delete a specified table from the database
    def deleteTable(self, tableName):
        sql = "DROP TABLE IF EXISTS {};".format(tableName)
        self.cursor.execute(sql)
        self.db.commit()
    
    # Delete the entire database
    def deleteDB(self):
        sql = "DROP DATABASE IF EXISTS {};".format(self.dbName)
        self.cursor.execute(sql)

    # Close the database connection
    def closeConnection(self):
        self.cursor.close()
        self.db.close()

    # Modify data in a specified table based on conditions and new values
    def modifyData(self, tableName, conditions, newValues):
        sql = "UPDATE {} SET ".format(tableName)
        for column, value in newValues.items():
            sql += "{}='{}', ".format(column, value)
        sql = sql[:-2] + " WHERE "
        for column, value in conditions.items():
            sql += "{}='{}' AND ".format(column, value)
        sql = sql[:-5] + ";"
        self.cursor.execute(sql)
        self.db.commit()
    
    # Print data from a specified table in a formatted manner with optional conditions
    def printData(self, tableName, conditions=None):
        data = self.fetchData(tableName, conditions)
        if data:
            widths = []
            columns = []
            tavnit = '|'
            separator = '+' 

            for cd in self.cursor.description:
                max_length = 0
                query = "SELECT MAX(LENGTH({})) FROM {};".format(cd[0], tableName)
                self.cursor.execute(query)
                max_length = self.cursor.fetchone()
                widths.append(max(max_length[0] if max_length else 0, len(cd[0])))
                columns.append(cd[0])

            for w in widths:
                tavnit += " %-"+"%ss |" % (w,)
                separator += '-'*w + '--+'
            
            print(separator)
            print(tavnit % tuple(columns))
            print(separator)
            for row in data:
                print(tavnit % row)
            print(separator)
        else:
            print("No data found in table '{}'.".format(tableName))
