import utils

input_grid = utils.read_file_as_string_and_split("inputs/day4.txt")

def word_search(text_grid: list[list[str]], x: int, y: int, current_str: str, direction_x: int, direction_y:int):
    next_letter = text_grid[x][y]
    current_str += next_letter
    if "XMAS".startswith(current_str):
        if current_str == "XMAS":
            return 1
    else:
        return 0
    if next_letter == "X" or next_letter == "M" or next_letter == "A":
        if 0 <= x+direction_x < len(text_grid) and 0 <= y+direction_y < len(text_grid[0]):
            return word_search(text_grid, x+direction_x, y+direction_y, current_str, direction_x, direction_y)
        else: 
            return 0
    else:
        return 0
    
xmas_counter = 0
for i in range(len(input_grid)):
    for j in range(len(input_grid[i])):
        if input_grid[i][j] == "X":
            for xinc in range(-1, 2):
                for yinc in range(-1, 2):
                    # word_search(input_grid, 0, 5, "", 0, 1)
                    if word_search(input_grid, i, j, "", xinc, yinc):
                        xmas_counter += 1
                        print (i, j, xinc, yinc)

print(xmas_counter)