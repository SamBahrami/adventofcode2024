import utils
import re

input_string = utils.read_file_as_string("inputs/day3.txt")

# Get parts of the text matching a regex
def get_parts_matching_regex(regex, text):
    return re.findall(regex, text)

parts = get_parts_matching_regex(r"mul\([0-9]+,[0-9]+\)", input_string)
total_mult = 0
for part in parts:
    # replace characters in a string 
    part = part.replace("mul(", "")
    part = part.replace(")", "")
    numbers = part.split(",")
    numbers = [int(number) for number in numbers]
    total_mult += numbers[0] * numbers[1]

print(total_mult)
pass