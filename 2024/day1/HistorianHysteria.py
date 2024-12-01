# part 1 solution
def difference_between_lists(left_list, right_list):
    count = 0
    for i in range(len(left_list)):
        result = left_list[i] - right_list[i]
        count += abs(result)
    return count


# part 2 solution
def similarity_score(left_list, right_list):
    count = 0
    for number in left_list:
        number_of_instances = right_list.count(number)
        count += (number * number_of_instances)
    return count


def main():
    left_list = list()
    right_list = list()

    with open("input.txt") as file:
        for line in file:
            index = line.index(" ")
            left_list.append(int(line[:index]))
            right_list.append(int(line[index:].strip()))

    left_list.sort()
    right_list.sort()

    final_result_part1 = difference_between_lists(left_list, right_list)
    final_result_part2 = similarity_score(left_list, right_list)
    return final_result_part2


print(main())
