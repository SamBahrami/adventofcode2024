def read_file_as_string(input_file: str) -> str:
    with open(input_file, "r") as file:
        return file.read()
    
def read_file_as_string_and_split(input_file: str, delimiter: str = "\n") -> list:
    with open(input_file, "r") as file:
        return file.read().split(delimiter)