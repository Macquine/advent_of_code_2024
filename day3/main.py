import re

input_path = "./day3/input.txt"

def read_input():
    with open(input_path) as f:
        return f.read()
    
def find_instructions(contents:str, mul="enabled"):
    """function to find the sum of multiplications recursively accounting for instructions.

       this function divides and conquers the problem by beginning with the whole string,
       having multiplications enabled for this first part by default. Once an instruction is found,
       it calls itself with a smaller string, everything from after the instruction to get the
       summed multiplication of everything after the instructions. For the part before the
       instruction, if the multiplications are disabled for this part, this part is ignored.
       If instructions are enabled for this part, it is added to the return value and the recursive
       call to this function. The base case is when no instructions can be found anymore.
    """

    # base case, there is no don't or do left in the content anymore
    if (contents.find("don't()") == -1) and (contents.find("do()") == -1):
        return calculate_sum_of_multiplications(contents[:])
    if mul == "enabled":
        # if multiplications are enabled, find the index from where we are stopping again,
        # add the multiplications of within the substring for which multiplications are enabled
        # to a recursive call to this function with a smaller substring from where the calculations
        # are disabled again.
        index = contents.find("don't()")
        return calculate_sum_of_multiplications(contents[:index]) + find_instructions(contents[index:], mul="disabled")
    if mul == "disabled":
        # if multiplications are disabled, we do not have to add the multiplications of the current substring 
        # but we do want to continue with the substring from where multiplications are enabled again.
        index = contents.find("do()")
        return find_instructions(contents=contents[index:], mul="enabled")
    
def calculate_sum_of_multiplications(contents:str):
    """Find and sum all multiplications in a string.

        this function finds all the instances in a string following the 
        "mul(1-3 digits,1-3 digits)" pattern using a regular expression and adds
        those multiplications together.
    """
    multiplications = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', contents)
    summed_multiplications = 0
    for multiplication_string in multiplications:
        numbers = re.findall(r'[0-9]{1,3},[0-9]{1,3}', multiplication_string)
        numbers = numbers[0].split(",")
        multiplied = int(numbers[0]) * int(numbers[1])
        summed_multiplications += multiplied

    return summed_multiplications

# answer to the first challenge:
print(calculate_sum_of_multiplications(contents=read_input()))
# answer to the second challenge:
print(find_instructions(contents=read_input()))
