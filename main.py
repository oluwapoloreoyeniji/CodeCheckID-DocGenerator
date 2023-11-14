import os
import shutil

class TextDocumentGenerator:
    def __init__(self, code_check_url, code_check_id, file_name, destination_path):
        """
        This function initialize the TextDocumentGenerator with the provided parameters

        :param code_check_url: (str) The CodeCheck URL
        :param code_check_id: (str) The CodeCheck ID
        :param file_name: (str) The name for the text document
        :param destination_path: (str) The destination path for the generated text document
        """
        self.code_check_url = code_check_url
        self.code_check_id = code_check_id
        self.file_name = file_name
        self.destination_path = destination_path

    def create_text_document(self):
        """
        This function creates a text document with the CodeCheck URL and ID

        :returns: (str) The name of the generated text document
        """
        default_content = f"CodeCheckUrl: {self.code_check_url}\nCodeCheckId: {self.code_check_id}"
        file_name_with_extension = f"{self.file_name}.txt"

        with open(file_name_with_extension, "w", encoding="utf-8") as file:
            file.write(default_content)

        return file_name_with_extension

    def move_text_document(self, source_file):
        """
        This function moves the generated text document to the specified destination path

        :param source_file: (str) The source file to be moved
        """
        if not os.path.exists(self.destination_path):
            os.makedirs(self.destination_path)

        shutil.move(source_file, self.destination_path)

    def generate_and_move_document(self):
        """
        This function generates a text document and move it to the specified destination path 
        It then prints a message indicating the completion of the process.
        """
        source_file = self.create_text_document()
        self.move_text_document(source_file)
        print(f"'{source_file}' has been generated with provided CodeCheckUrl and ID. You can find it in '{self.destination_path}'.")

def main():
    """
    This is the main function to interact with the user and utilize the TextDocumentGenerator
    """
    code_check_url = input("Enter the CodeCheckUrl: ")
    code_check_id = input("Enter the CodeCheckId: ")
    file_name = input('Enter a name for the text document: ')
    destination_path = "C:/Users/HP/Desktop/kibo-real/2nd-term/prog-2/CodeCheck ID"

    generator = TextDocumentGenerator(code_check_url, code_check_id, file_name, destination_path)
    generator.generate_and_move_document()

if __name__ == "__main__":
    main()
