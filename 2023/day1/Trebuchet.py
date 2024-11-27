import re
from functools import reduce


# part 1 solution
def get_double_digit_number(mapline):
    digit_list = []
    for character in mapline:
        if character.isdigit():
            digit_list.append(character)
    number = digit_list[0] + digit_list[-1]
    return number


# part 2 solution

numbersDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def replace_as_int(raw_line):
    key_list = list(numbersDict.keys())
    for number in key_list:
        if number in raw_line:
            if raw_line.count(number) > 1:
                occurrences = re.finditer(number, raw_line)
                multi_indices = reduce(lambda x, y: x + [y.start()], occurrences, [])
                for i in range(len(multi_indices)):
                    index = multi_indices[i]
                    raw_line = raw_line[: index + 1] + str(numbersDict[number]) + raw_line[index + 2:]
            else:
                index = raw_line.find(number)
                raw_line = raw_line[: index + 1] + str(numbersDict[number]) + raw_line[index:]
    return raw_line


count = 0
with open("input.txt") as file:
    for line in file:
        updated_line = replace_as_int(line)
        count += int(get_double_digit_number(updated_line))
print(count)
