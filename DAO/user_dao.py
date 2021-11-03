from DAO.sql_helper import sql_helper

class user_dao:
    def __init__(self):
        self.__db = sql_helper()

    def create_user(self, name, email, password):
        if(self.__db.run_query("SELECT count(*) FROM user WHERE email='"+email+"'")[0][0]==1):
            return 0
        return self.__db.run_query("CALL CreateUser('"+email+"','"+name+"','"+password+"');")
         
    def get_user(self, email, password):
        data = {}
        result = self.__db.run_query("SELECT count(*),user_id,email,full_name FROM user WHERE email='"+email+"'")
        if(result[0][0]==0):
            return 0
        if(email == result[0][2]):
            if(password == self.__db.run_query("SELECT password FROM user_login WHERE user_id="+str(result[0][1]))[0][0]):
                data["full_name"] = str(result[0][3])
                return data
            else:
                return 2
    
    def get_user_id(self, email):
        pass     

    def update_details(self):
        pass

    def delete_user(self):
        pass

