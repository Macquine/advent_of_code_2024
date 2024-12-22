INPUT_PATH = "./day2/input.txt"

from typing import Literal
from copy import deepcopy

def get_reports(input_path: str) -> list[list[int]]:
    """loads in the input file

    loads the reports from the input file, removing the
    newline character, splitting every line on the space
    to get each report as a list of strings and then
    casts all the numbers in each report to actual integers.
    """

    with open(input_path) as f:
        contents = f.readlines()
        contents = [line.replace("\n", "") for line in contents]
        reports = [report.split() for report in contents]
        reports = [[int(number) for number in report] for report in reports]

    return reports

def determine_slope(report) -> Literal["positive", "negative"]:
    """Determine if the numbers in a report are decreasing or increasing.

       goes over the list until it finds out if the numbers are
       decreasing or increasing. (if one i == (i+1)), we continue
       with the next pair of numbers in the list until we find
       the numbers being decreasing/increasing.
    """
    
    for i in range(len(report)-1):
        if (report[i] < report[i+1]):
            return "positive"
        elif (report[i] > report[i+1]):
            return "negative"
        else:
            if i == len(report)-1:
                raise (ValueError("the numbers are neither increasing nor decreasing."))
            continue


def report_is_monotonic(report: list[int]) -> bool:
    """check if all the numbers in a report are either
       increasing or decreasing. 
    """

    if len(report) <= 1:
        return True
    
    slope = determine_slope(report)
    if slope == "positive":
        for i in range(len(report)-1):
            if report[i] > report[i+1]:
                return False
        return True
    if slope == "negative":
        for i in range(len(report)-1):
            if report[i] < report[i+1]:
                return False
        return True
    else:
        raise ValueError("Slope has taken on an illegal value")

def check_adjacent_diff_valid(report) -> bool:
    """check if two adjacent numbers differ by minimally 1 and maximally 3.

       returns: True if adjacent numbers adhere to the rule, false otherwise.
    """

    if len(report) <= 1:
        return True
    
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

def get_n_safe_reports(reports: list[list[int]], allow_one_violation: bool) -> int:
    """For all reports, get the number which are safe.

    Safe is being defined as:
        - the numbers in a report are either increasing or decreasing
        - the difference between the i and i+1 in a report must be
            minimally 1 and maximally 3

        returns: the number of reports which are safe
    """
    safe_count = 0
    for report in reports:
        # check if the report is sage without having to remove one value.
        if (check_adjacent_diff_valid(report) and report_is_monotonic(report)):
            safe_count +=1
        else:
            # check if the report can be made safe by removing exactly one if the numbers.
            # try to remove each number one by one. If a safe report is found, stop and go to the next report.
            if allow_one_violation is True:
                for i in range(len(report)):
                    report_copy = deepcopy(report)
                    report_copy.pop(i)
                    if check_adjacent_diff_valid(report_copy) and report_is_monotonic(report_copy):
                        safe_count+=1
                        break
                
    return safe_count

reports = get_reports(INPUT_PATH)
print(get_n_safe_reports(reports, allow_one_violation=True))

# NOTE: it would be possible to make some improvements.
# 1. the difference between each adjacent number needs to
#    be at least 1, if we check for this condition first
#    we do not need to raise an error in the determine slope
#    function when every number is the same because this is not
#    possible for the remaining items.
# 2. if we do #1. for the same reason we do not have to loop over
#    the list anymore to find the slope but we can just check the
#    first two items to determine the slope and then check if the slope
#    holds for the whole list.
# 3. instead of passing back whether the slope is negative or positive
#    we could pass back the >, < operators directly so that we only need
#    one for loop to check with this operator and no condition at all. 
#    the operators can be imported from the operator module:
#    from operator import ge, le, gt, lt
# 4. we could loop over the list one time to both get the slope
#    and determine for the whole list if the slope holds if 
#    we would only check the slope in the first iteration of the loop.