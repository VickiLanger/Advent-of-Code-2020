"""
report-repair.py: from input.text find the two entries that sum to 2020 and then multiply those two numbers together; solve puzzle at https://adventofcode.com/2020/day/1
1 December 2020
@Vicki_Langer
"""


# import text file with list of numbers
with open("inputs/day_1.txt") as raw_data:
    data = raw_data.read()
# put numbers into a list
expense_report_numbers = [int(number) for number in data.split('\n') if number]


year_number = 2020

for i, expense in enumerate(expense_report_numbers[:-1]):  # don't need the last number
    complementary_number = year_number - expense
    if complementary_number in expense_report_numbers[i+1:]:
        answer = complementary_number * expense
        print(f"Found them! {complementary_number} * {expense} is {answer}")
        break  # end loop when it finds the answer
else:
    print(f"no 2 numbers add up to {year_number}")
