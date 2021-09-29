class Application:
    def add_new_application(request):
        company_name = request.form['company_name']
        location = request.form['location']
        job_profile = request.form['job_profile']
        salary = request.form['salary']
        user_name = request.form['user_name']
        password = request.form['password']
        security_question = request.form['security_question']
        security_answer = request.form['security_answer']
        notes = request.form['notes']
        date_applied = request.form['date_applied']
        status = request.form['status']
        user_id = 1
        company_id = 1
        role_id = 1

        insert_sql_query = "INSERT INTO `application` (`user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES ({},{},{},NULL,'{} 00:00:00','{}',{},NULL,{},'{} 05:00:00');"
        
