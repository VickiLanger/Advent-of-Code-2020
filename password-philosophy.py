"""
password-philosophy.py: from day_2.txt find out how many passwords are valid according to their policies; solve puzzle at https://adventofcode.com/2020/day/2
2 December 2020
@Vicki_Langer / @VickiLanger
"""

# read text file


def validate_passwords():
    num_valid_passwords = 0
    for line in open('inputs/day_2.txt').readlines():
        lower_upper, character, password = line.strip('\n').split()
        character = character[0]
        lower, upper = lower_upper.split('-')
        count = password.count(character)
        if (count >= int(lower)) & (count <= int(upper)):
            num_valid_passwords += 1
            print(num_valid_passwords)


validate_passwords()
