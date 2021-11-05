from DAO.sql_helper import sql_helper

class application_dao:
    def __init__(self):
        self.__db = sql_helper()

    def add_application(self, email, company_name, location, job_profile, salary, username, password, security_question, security_answer, notes,
    date_applied):
        status = "TO_DO"
        userId = self.__db.run_query("SELECT user_id FROM user WHERE email='"+email+"'")[0][0]
        
        self.__db.run_query("INSERT into company (company_name) values ('"+company_name+"');")
        companyId = self.__db.run_query("SELECT company_id FROM company WHERE company_name='"+company_name+"'")[0][0]

        self.__db.run_query("INSERT INTO roles (role) values ('"+job_profile+"');")
        roleId = self.__db.run_query("SELECT role_id FROM roles WHERE role='"+job_profile+"'")[0][0]

        return self.__db.run_query("INSERT INTO application (user_id, company_id, role_id, application_date, job_description, salary, location, status) values ("+str(userId)+", "+str(companyId)+", "+str(roleId)+", "+date_applied+", '"+job_profile+"', "+str(salary)+", '"+location+"', '"+status+"');")

    def get_application(self, email, application_status):
        userId = self.__db.run_query("SELECT user_id FROM user WHERE email='"+email+"'")[0][0]
        res = self.__db.run_query("SELECT company_name, status, application_date FROM application JOIN company ON company.company_id = application.company_id WHERE user_id="+str(userId))

        print(res)
        return res

    def update_application(self):
        pass

    def delete_application(self):
        pass

