"""
report-repair.rb: from input.txt find the two entries that sum to 2020 and then multiply those two numbers together; solve puzzle at https://adventofcode.com/2020/day/1
1 December 2020
@Vicki_Langer / @VickiLanger
"""


# read text file with list of numbers
expenses = File.readlines("inputs/day_1.txt")

# loop through list to find number
expenses.each do |expense_one|
    expenses.each do |expense_two|
        sum = expense_one.to_i + expense_two.to_i
		if sum == 2020
			puts "found it! " + expense_one.strip + ' + ' + expense_two.strip + ' = ' + sum.to_s
			answer = expense_one.to_i * expense_two.to_i
			puts "muliplied together, it's " + answer.to_s
            exit # end loop when it finds the answer (like a python break)
        end
    end
end