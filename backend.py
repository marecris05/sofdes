import pymysql
import time


class UserDatabase:
    def __init__(self):
        self.con = None
        self.mycursor = None

    def connect(self):
        try:
            self.con = pymysql.connect(host='localhost', user='root', password='1234', database='ums')
            self.mycursor = self.con.cursor()
            self.mycursor.execute("""CREATE TABLE IF NOT EXISTS user (
                                    ID INT AUTO_INCREMENT PRIMARY KEY,
                                    Name VARCHAR(50),
                                    Phone VARCHAR(15),
                                    Email VARCHAR(50),
                                    Address VARCHAR(100),
                                    Gender VARCHAR(10),
                                    DOB VARCHAR(15),
                                    Date VARCHAR(15),
                                    Time VARCHAR(15))""")
            self.con.commit()
            return "Success", "Database Connected Successfully"
        except Exception as e:
            return "Error", f"Database Connection Failed: {str(e)}"

    def add_user(self, data):
        try:
            query = """INSERT INTO user (Name, Phone, Email, Address, Gender, DOB, Date, Time)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            self.mycursor.execute(query, data)
            self.con.commit()
            return "Success", "User Added Successfully"
        except Exception as e:
            return "Error", f"Failed to Add User: {str(e)}"

    def fetch_users(self):
        try:
            query = "SELECT * FROM user"
            self.mycursor.execute(query)
            return "Success", self.mycursor.fetchall()
        except Exception as e:
            return "Error", f"Failed to Fetch Data: {str(e)}"

    def update_user(self, user_id, data):
        try:
            query = """UPDATE user SET Name=%s, Phone=%s, Email=%s, Address=%s, Gender=%s, DOB=%s
                       WHERE ID=%s"""
            self.mycursor.execute(query, data + (user_id,))
            self.con.commit()
            return "Success", "User Updated Successfully"
        except Exception as e:
            return "Error", f"Failed to Update User: {str(e)}"

    def delete_user(self, user_id):
        try:
            query = "DELETE FROM user WHERE ID=%s"
            self.mycursor.execute(query, (user_id,))
            self.con.commit()
            return "Success", "User Deleted Successfully"
        except Exception as e:
            return "Error", f"Failed to Delete User: {str(e)}"
