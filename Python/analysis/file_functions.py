class FileFunctions:

    def add_line(self, file_path: str, line: str) -> None:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(line + '\n')

    def read_lines(self, file_path: str) -> list:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
