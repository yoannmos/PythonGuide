import sqlite3
from sqlite3 import Error
import datetime

class MyDatabase():

    def __init__(self, db_path):
        self.db_path = db_path
        self.create_connection()
    
    def create_connection(self):
        """ create a database connection to a SQLite database 
        """

        try:
            self.con = sqlite3.connect(self.db_path) #dB browser for sqlite needed
            print("sqlite3.version :", sqlite3.version)
            print("CONNEXION OPENED to", self.db_path)
        except Error as e:
            print(e)
        # finally:
        #     self.con.close()
        #     print("CONNEXION CLOSED to", self.db_path)
        
    def create_table(self, title, param_list, references={}):
        """ create a table from the create_table_sql statement
            :title : Table title
            :paramlist : list of dictionnary [{"col_name":"", "col_type":"", "col_attribute":""},...]
            :references : dictionnary {"foreign_key":"", "ref_table":"", "param":""}
            :return:
        """

        table_text = " CREATE TABLE IF NOT EXISTS "+title+" ("   # Insert the tittle

        for col_dict in param_list:   # Insert Collumns
            if col_dict["col_name"] and col_dict["col_type"] != "":
                param_text = "{col_name} {col_type} {col_attribute}, ".format(**col_dict)
                table_text += param_text
            else:
                raise ValueError("Your list countain a dictionnary with an empty 'col_name' or 'col_type'")

        table_text = table_text[:-2]   # Suppress last coma and last space

        if references:   # Add reference if exist
            if not all(references.values()):   # If all values exist too
                raise ValueError("Your dictionnary countain an empty value")
            else:
                ref_text = ", FOREIGN KEY ({foreign_key}) REFERENCES {ref_table} ({param})".format(**references)
                table_text += ref_text
        
        table_text += ");"

        # print(table_text)
        try:
            c = self.con.cursor()
            c.execute(table_text)
        except Error as e:
            print(e)


    # def find(self):
    #     cur = self.con.cursor()
    #     # cur.execute("ATTACH "+self.db_path+" AS my_db")
    #     cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    
    #     rows = cur.fetchall()
    
    #     for row in rows:
    #         print(row)


if __name__ == "__main__":
    db_path = r"mydatabase.db"
    d = MyDatabase(db_path)

    title1 = "project"
    param_list1 = [{"col_name":"id", "col_type":"integer", "col_attribute":"PRIMARY KEY"},
                  {"col_name":"name", "col_type":"text", "col_attribute":"NOT NULL"},
                  {"col_name":"begin_date", "col_type":"text", "col_attribute":""},
                  {"col_name":"end_date", "col_type":"text", "col_attribute":""}]
    
    d.create_table(title1, param_list1)

    title2 = "tasks"
    param_list2 = [{"col_name":"id", "col_type":"integer", "col_attribute":"PRIMARY KEY"},
                   {"col_name":"name", "col_type":"text", "col_attribute":"NOT NULL"},
                   {"col_name":"priority", "col_type":"integer", "col_attribute":""},
                   {"col_name":"status_id", "col_type":"integer", "col_attribute":"NOT NULL"},
                   {"col_name":"project_id", "col_type":"integer", "col_attribute":"NOT NULL"},
                   {"col_name":"begin_date", "col_type":"text", "col_attribute":""},
                   {"col_name":"end_date", "col_type":"text", "col_attribute":""}]
    references2 = {"foreign_key":"project_id", "ref_table":"projects", "param":"id"}
 
    d.create_table(title2, param_list2, references2)