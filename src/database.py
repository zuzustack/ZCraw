import psycopg2
from psycopg2 import Error

class Database:
    def __init__(self, user,password,host,database,port="5432"):
        try:
            self.connection = psycopg2.connect(user=user,
                                        password=password,
                                        host=host,
                                        port=port,
                                        database=database)


        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)


    def storeURL(self,data) :

        try:
            cursor = self.connection.cursor()
            
            query = """ INSERT INTO list_urls (url,title) VALUES (%s,%s)"""

            for dt in data:
                cursor.execute(query, (dt["url"],dt["title"]))
                self.connection.commit()

            print(len(data), "Record inserted successfully into list_urls table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into list_urls table: ", error)
        finally:
            cursor.close()


    def getURL(self):
        try:
            cursor = self.connection.cursor()
            query = """ SELECT * FROM list_url """

            cursor.execute(query)

            return cursor.fetchall()
        
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            cursor.close()