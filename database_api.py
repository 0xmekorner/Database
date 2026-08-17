import sqlite3

class SQLite:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()


    def create_table(self, table_name, column_names_and_types):
        try:
            self.cursor.execute(f"CREATE TABLE {table_name} ({', '.join(column_names_and_types)})")
        except sqlite3.Error as err:
            print("faild creation table: {}".format(err))
            return False
        return True

    def write_column(self, table_name, data):
        try:
            self.cursor.execute(f"INSERT INTO {table_name} VALUES {data}")
        except sqlite3.Error as err:
                print("faild writing data: {}".format(err))
                return False
        return True

    def execute_query(self, query, args = None):
        if args:
            result = self.cursor.execute(query, args).fetchall()
        else:
            result = self.cursor.execute(query).fetchall()
        return result


    def close(self):
         self.conn.commit()
         self.conn.close()

if __name__ == "__main__":
    db = SQLite(r"C:\Users\hiwot\Git projects\Database\mystore.db")
    table_name = "users"
    db.create_table(table_name, ['username TEXT', 'password TEXT'])
    db.write_column(table_name, ("ozmyman123", "123456"))

    query = "SELECT * FROM users WHERE username=? AND password=?"
    args = ("ozmyman123", "123456")
    data = db.execute_query(query, args)
    print(data)
    
    db.close()
    
        