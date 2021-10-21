from DAO.sql_helper import sql_helper

class user_dao:
    def __init__(self):
        self.__db = sql_helper()

    def create_user(self, name,email,password):
        return self.__db.run_query("INSERT INTO `details_User` (`name`, `email`,`password`) VALUES ('"+name+"','"+ email +"','"+ password+"');")
    def get_user(self):
        pass

    def update_details(self):
        pass

    def delete_user(self):
        pass

