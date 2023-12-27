import os

class FileGenerator:
    def __init__(self, file_name, incoming_content):
        """
        This function initialize the FileGenerator with the provided parameters

        
        :param file_name: (str) The name for the text document
        :param incoming_content: (str) The content to be written in the generated file
        """
        self.file_name = file_name
        self.incoming_content = incoming_content

    def create_new_file(self):
        """
        This function creates a document
        """
        with open(self.file_name, 'x', encoding='utf-8') as f:
            pass

    def file_empty(self):
        """
        This function checks if a document is empty

        :returns: (bool) The emptiness of the document    
        """
        return os.path.getsize(self.file_name)
    
    def write_to_file(self):
        """
        This function writes self.incoming_content to self.file_name, it only works for empty documents
        """
        empty = self.file_empty()
        if empty:
            with open(self.file_name, 'w', encoding='utf-8') as f:
                f.write(self.incoming_content)

class ExistingFileGenerator(FileGenerator):
    def __init__(self, file_name, incoming_content):
        super().__init__(file_name, incoming_content)

    def append_to_file(self):
        """
        This function appends self.incoming_content to self.file_name
        """
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f"{self.incoming_content}")

    def overwrite_file(self):
        """
        This function overwrites the content of to self.file_name with self.incoming_content 
        """
        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write(self.incoming_content)
