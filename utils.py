def read_file_as_string(input_file: str) -> str:
    with open(input_file, "r") as file:
        return file.read()