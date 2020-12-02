"""
password-philosophy.rb: from day_2.txt find out how many passwords are valid according to their policies; solve puzzle at https://adventofcode.com/2020/day/2
2 December 2020
@Vicki_Langer
"""

read each line of txt file

# \d numerical digit
# \w alphanumeric characters
# * zero or more


use regex to .match
use .captures # returns array of matches
decide if valid with .between?