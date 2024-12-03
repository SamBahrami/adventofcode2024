input_file = "inputs/day2.txt"

def read_list(input:str) -> list:
    lines = input.split("\n")
    lists = []
    for line in lines:
        if line == "":
            continue
        elements = line.split(" ")
        elements = [int(element) for element in elements]
        lists.append(elements)
    return lists

def check_list_safety(test_list: list):
    """The engineers are trying to figure out which reports are safe. 
    The Red-Nosed reactor safety systems can only tolerate levels that are either 
    gradually increasing or gradually decreasing. So, a report only counts as safe 
    if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    """
    increasing = None
    for i in range(1, len(test_list)):
        diff = test_list[i] - test_list[i-1]
        if increasing is None:
            increasing = diff > 0
        if diff > 3:
            return False
        elif diff == 0:
            return False
        elif not increasing and diff < -3:
            return False
        elif increasing and diff < 0:
            return False
        elif not increasing and diff > 0:
            return False
    return True

# Read the input file as a string
with open(input_file, "r") as file:
    input_txt = file.read()
input_lists = read_list(input_txt)

valid_lists = 0
for input_list in input_lists:
    # Check every input_list with a single element removed
    for i in range(len(input_list)):
        if check_list_safety(input_list[:i] + input_list[i+1:]):
            valid_lists += 1
            break
print(valid_lists)
