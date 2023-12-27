import generator
from helpers import get_user_input, get_codecheck_content, path_creator, does_path_exist

# Constants
WRITE_TO_NEW_FILE = '1'
OVERWRITE_EXISTING_FILE = '2'
APPEND_TO_EXISTING_FILE = '3'
CHOICES = [WRITE_TO_NEW_FILE, OVERWRITE_EXISTING_FILE, APPEND_TO_EXISTING_FILE]

# Prompts
FILE_OPERATION_PROMPT = '''
Do you want to write to a new file, overwrite an existing file or append to an existing file?
Type '1' to create a new file 
Type '2' to overwrite an existing file
Type '3' to append to an exiting file: '''
FILE_NAME_PROMPT = "Enter the file name: "
DIRECTORY_NAME_PROMPT = "Enter the directory name: "
WARNING_PROMPT = "Enter y to continue, enter n to stop"

def main():
    """
    This is the main function to interact with the user and utilize the FileGenerator
    """
    while True:
        user_input = get_user_input(FILE_OPERATION_PROMPT)
        content = get_codecheck_content()

        if user_input not in CHOICES:
            print("Invalid choice. Please select a valid option.")
            continue

        if user_input == WRITE_TO_NEW_FILE:
            file_name = get_user_input(FILE_NAME_PROMPT)
            dir_name = get_user_input(DIRECTORY_NAME_PROMPT)

            file_path = path_creator(file_name, dir_name)
            path_exists = does_path_exist(file_path)

            if path_exists:
                print("Error: File already exists. Please choose a different file name.")
                continue

            if not content:
                print("Error: No content provided.")
                continue

            creator = generator.FileGenerator(file_name=file_path, incoming_content=content)
            creator.create_new_file()
            creator.write_to_file()
            print(f"Success, File: {file_name} has been created and content has been written to it.")
            break

        elif user_input == OVERWRITE_EXISTING_FILE or user_input == APPEND_TO_EXISTING_FILE:
            file_name = get_user_input(FILE_NAME_PROMPT)
            dir_name = get_user_input(DIRECTORY_NAME_PROMPT)

            file_path = path_creator(file_name, dir_name)
            path_exists = does_path_exist(file_path)

            if not path_exists:
                print("Error: File does not exist.")
                continue

            if not content:
                print("Error: No content provided.")
                continue

            creator = generator.ExistingFileGenerator(file_name=file_path, incoming_content=content)

            if user_input == OVERWRITE_EXISTING_FILE:
                print(f"WARNING!!! File: {file_name} will be overwritten")
                warning_choice = get_user_input(WARNING_PROMPT)
                if warning_choice == 'y':
                    creator.overwrite_file()
                    print(f"Success, File: {file_name} has been overwritten with content.")

            elif user_input == APPEND_TO_EXISTING_FILE:
                print(f"WARNING!!! Content will be appended to File: {file_name}")
                warning_choice = get_user_input(WARNING_PROMPT)
                if warning_choice == 'y':
                    creator.append_to_file()
                    print(f"Success, Content has been appended to File: {file_name}.")
            break

if __name__ == '__main__':
    main()
