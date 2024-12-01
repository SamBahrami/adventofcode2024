input_file = "inputs/day1.txt"


def read_list(input):
    lines = input.split("\n")
    lists = {}
    for line in lines:
        if line == "":
            continue
        elements = line.split("   ")
        for i, element in enumerate(elements):
            if i not in lists:
                lists[i] = []
            lists[i].append(int(element))
    return lists


def compare_list_pair_distances(lista, listb):
    """Compare the distance between each element of lista and listb"""
    distances = []
    for i in range(len(lista)):
        distances.append(abs(lista[i] - listb[i]))
    return distances


# Create a hashmap of the second list
def count_element_frequency_in_list(number_list):
    frequency = {}
    for number in number_list:
        if number not in frequency:
            frequency[number] = 0
        frequency[number] += 1
    return frequency


# Read the input file as a string
with open(input_file, "r") as file:
    day1_input = file.read()

lists = read_list(day1_input)
lista, listb = sorted(lists[0]), sorted(lists[1])
distances = compare_list_pair_distances(lista, listb)
print(sum(distances))
listb_frequency = count_element_frequency_in_list(listb)
similarity_score = 0
for number in lista:
    if number in listb_frequency:
        similarity_score += listb_frequency[number] * number
print(similarity_score)
