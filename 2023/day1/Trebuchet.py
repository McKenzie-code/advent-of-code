def get_double_digit_number(mapline):
    digit_list = []
    for character in mapline:
        if character.isdigit():
            digit_list.append(character)
    number = digit_list[0] + digit_list[-1]
    return number


count = 0
with open("input.txt") as file:
    for line in file:
        count += int(get_double_digit_number(line.rstrip()))
print(count)
