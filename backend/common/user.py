from typing import Dict, List
import json

class User():
    def __init__(self,user_id,email,password,first_name,last_name,icon=None):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.icon = icon

    @classmethod
    def from_email(cls,conn,email):
        sql_stmt = "SELECT user_id,email,password,first_name,last_name,icon FROM users WHERE email = ?"
        cursor = conn.cursor()

        cursor.execute(sql_stmt, (email,))
        
        usr = cursor.fetchone()
        if usr is None:
            return None
        return cls(usr[0],usr[1],usr[2],usr[3],usr[4],usr[5])

    def to_dict(self)->Dict:
        di = {"userId":self.user_id,
                "email":self.email,
                "password":self.password,
                "firstName":self.first_name,
                "lastName":self.last_name,
                "icon":self.icon,
        }
        return di

    def to_json(self)->str:
        return json.dumps(self.to_dict())
    
