# PART-1
# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
# PART-2
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
import re

class CalibrationDocument:
    def __init__(self, doc_path):
        self.doc_path = doc_path
        self.calibration_lines = []
        self.calibration_values = []
        self.number_names = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        self.pattern = self.create_search_pattern()
    
    def read_doc_file(self):
        doc_file = open(self.doc_path, 'r')
        self.calibration_lines = doc_file.readlines()
        
    def find_number(self, line):
        """return the number from a single line in the document"""
        match = self.find_all_matches(line)
        matched_num = []
        for each in match:
            if each.isnumeric():
                matched_num.append(int(each))
            else:
                matched_num.append(self.number_names[each])
        first_num = matched_num[0]
        last_num = matched_num[-1]
        return int(f"{first_num}{last_num}")
    
    def find_all_matches(self, line):
        """find all matches even if names are overlapping ex. nineight"""
        numbers = []
        substr = re.search(self.pattern, line)
        while substr!=None:
            # if we find any occurrence then append it
            num = substr.group()
            numbers.append(num)
             
            # find next occurrence just after previous 
            # sub-string
            # for first occurrence nine, substr.start()=1
            # substr.end()=4
            # if the number found is numeric then don't consider the current substring
            # otherwise for overlapping characters need to start from (end - 1)
            if not num.isnumeric():
                line = line[(substr.end()-1):]
                substr = re.search(self.pattern, line)
            else:
                line = line[(substr.end()):]
                substr = re.search(self.pattern, line)
        return numbers
        
    def find_all_numbers(self):
        """find all the numbers from the calibration document"""
        for each_line in self.calibration_lines:
            print(each_line)
            number = self.find_number(each_line)
            print(number)
            self.calibration_values.append(number)
    
    def find_sum_of_values(self):
        """find the sum of all the calibration values"""
        self.find_all_numbers()
        return (sum(self.calibration_values))
    
    def create_search_pattern(self):
        """create search pattern to find all digits and names"""
        pattern = f"([0-9]|"
        num_keys = list(self.number_names.keys())
        for i in range(0, 9):
            each = num_keys[i]
            if i == 8:
                pattern = pattern + f"{each})"
            else:
                pattern = pattern + f"{each}|"
        return pattern

def main():
    doc_path = "aoc_01.txt"
    cal_doc = CalibrationDocument(doc_path)
    cal_doc.read_doc_file()
    final_value = cal_doc.find_sum_of_values()
    print(final_value)
    
main()
    
    
                
                
                
