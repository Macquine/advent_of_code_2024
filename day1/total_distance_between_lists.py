import numpy as np

INPUT_FILE_PATH = "advent_of_code_day1_input.txt"


def get_lists() -> (list, list):
    """open the exercise input file which contains
       2 columns with numbers. Parse the file into
       two python lists of numbers and return those.
    """
    with open(INPUT_FILE_PATH) as f:
        list1 = []
        list2 = []    
        lines = f.readlines()
        for line in lines:
            numbers = line.split(" ")
            numbers = [int(item.replace("\n", "")) for item in numbers if item != '']
            list1.append(numbers[0])
            list2.append(numbers[1])

    return (list1, list2)


def find_distance_between_lists(list1: list, list2: list) -> int:
    """For two lists of numbers, sort the lists
       then get the pairwise distance (absolute) of each number
       in the first list and each number in the second list.
       SUM the total distance and return this total distance.
    """
    list1 = sorted(list1)
    list2 = sorted(list2)
    diffs = np.subtract(list1, list2)
    diffs = [abs(diff) for diff in diffs]

    summed_diffs = sum(diffs)

    return summed_diffs


def get_list_similarity(list1: list, list2: list) -> int:
    """get the total similarity between two lists: list1 and list2
       which is defined as, for every number in list1, multiply it
       by the number of occurences of that number in list2.
    """
    total_similarity_score = 0
    for item in list1:
        item_count_in_list2 = list2.count(item)
        total_similarity_score += (item * item_count_in_list2)

    return total_similarity_score
