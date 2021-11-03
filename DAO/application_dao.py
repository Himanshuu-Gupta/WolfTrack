from DAO.sql_helper import sql_helper

class application_dao:
    def add_application(self, email, company_name, location, job_profile, salary, username, password, security_question, security_answer, notes,
    date_applied):

        userId = self.__db.run_query("SELECT user_id FROM user WHERE email='"+email+"'")[0][0]
        
        self.__db.run_query("CALL CreateCompany('"+company_name+"');")
        companyId = self.__db.run_query("SELECT company_id FROM company WHERE company_name='"+company_name+"'")[0][0]

        self.__db.run_query("CALL CreateRoles('"+job_profile+"');")
        roleId = self.__db.run_query("SELECT role_id FROM roles WHERE role='"+job_profile+"'")[0][0]

        self.__db.run_query("CALL CreateRecruiter('"+job_profile+"');")

        return self.__db.run_query("CALL CreateApplication('userId','"+name+"','"+password+"');")

    def get_application(self):
        pass

    def update_application(self):
        pass

    def delete_application(self):
        pass

