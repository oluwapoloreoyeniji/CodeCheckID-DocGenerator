import os

def get_user_input(prompt):
    user_input = input(prompt)
    return user_input

def get_codecheck_content():
    code_check_url = get_user_input('Enter the code_check_url: ')
    code_id = get_user_input('Enter the code_check_id: ')
    return f"CodeCheckUrl: {code_check_url}\nCodeCheckId: {code_id}"

def path_creator(file_name, dir_name):
    file_path = os.path.join(file_name, dir_name)
    return file_path

def does_path_exist(file_path):
    return os.path.exists(file_path)