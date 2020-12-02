"""
password-philosophy.rb: from day_2.txt find out how many passwords are valid according to their policies; solve puzzle at https://adventofcode.com/2020/day/2
2 December 2020
@Vicki_Langer
"""

valid_passwords = 0

passwords_with_policies = File.readlines("inputs/day_2.txt")

# \d numerical digit
# \w alphanumeric characters
# * zero or more

passwords_with_policies. each do |line|
    low, high, character, password = line.match(/(\d*)-(\d*) (\w): (\w*)/).captures  # each () goes to the respective variable and is the captured in an array
        if password.count(character).between?(low.to_i, high.to_i)
            valid_passwords += 1
        end
    puts valid_passwords
end