import re
cnt = 1
class EnginePart:
    def __init__(self, prev_line, cur_line, next_line):
        self.prev_line = prev_line
        self.cur_line = cur_line
        self.next_line = next_line
        self.valid_numbers = []
        
    def find_numbers(self, line):
        numbers = []
        pattern = "[0-9]+"
        num_iterator = re.finditer(pattern, line)
        for each in num_iterator:
            numbers.append(each)
        return numbers
    
    def find_symbols(self, line):
        pattern = "[^\\w.\\n]"
        symbols = []
        sym_iterator = re.finditer(pattern, line)
        for each in sym_iterator:
            symbols.append(each)
        # print(symbols)
        return symbols
        
    def find_gear_symbols(self, line):
        pattern = "[*]"
        gear_symbols = []
        gs_iterator = re.finditer(pattern, line)
        for each in gs_iterator:
            gear_symbols.append(each)
        # print(gear_symbols)
        return gear_symbols
        
    def get_valid_numbers(self):
        numbers = self.find_numbers(self.cur_line)
        if self.prev_line:
            prev_line_symbols = self.find_symbols(self.prev_line)
        else:
            prev_line_symbols = []
        cur_line_symbols = self.find_symbols(self.cur_line)
        if self.next_line:
            next_line_symbols = self.find_symbols(self.next_line)
        else:
            next_line_symbols = []
        for each in numbers:
            if self.check_for_symbols_in_adjacent_line(each, prev_line_symbols):
               self.valid_numbers.append(int(each.group()))
            elif self.check_adjacent_symbols_in_cur_line(each, cur_line_symbols):
               self.valid_numbers.append(int(each.group()))
            elif self.check_for_symbols_in_adjacent_line(each, next_line_symbols):
               self.valid_numbers.append(int(each.group()))
        return self.valid_numbers
    
    def check_adjacent_symbols_in_cur_line(self, num_match, cur_line_symbols):
        if cur_line_symbols:
            start = num_match.start()
            end = num_match.end()
            for each in cur_line_symbols:
                # to check if the symbol is adjacent to the number on either side
                if (each.end() == start) or (each.start() == end):
                    return True
        return False
    
    def get_gear_ratio(self):
        gear_sym = self.find_gear_symbols(self.cur_line)
        gear_ratio = 0
        if self.prev_line:
            prev_numbers = self.find_numbers(self.prev_line)
        else:
            prev_numbers = []
        cur_numbers = self.find_numbers(self.cur_line)
        if self.next_line:
            next_numbers = self.find_numbers(self.next_line)
        else:
            next_numbers = []
        for each_sym in gear_sym:
            all_numbers = prev_numbers + cur_numbers + next_numbers
            gear_numbers = []
            for each_num in all_numbers:
                # this for numbers lying on left and right
                if each_sym.start() in range(each_num.start() -1, each_num.end() + 1):
                    gear_numbers.append(each_num.group())
            if len(gear_numbers) == 2:
                # print(cnt, each_sym.start(), each_sym.end())
                gear_ratio += int(gear_numbers[0]) * int(gear_numbers[1])
        return gear_ratio
        
    def check_for_symbols_in_adjacent_line(self, num_match, adj_line_symbols):
        if adj_line_symbols:
            for each in adj_line_symbols:
                match_start = num_match.start() - 1
                match_end = num_match.end()
                if each.start() >= match_start and each.start() <= match_end:
                    return True
        return False
        
            
def main():
    file = open("aoc_03.txt", "r")
    lines = file.readlines()
    valid_numbers = []
    sum_of_gear_ratios = 0
    for i in range(0, len(lines)):
        if i == 0:
            prev_line = None
        else:
            prev_line = lines[i - 1]
        cur_line = lines[i]
        if i == len(lines) - 1:
            next_line = None
        else:
            next_line = lines[i + 1]
        engine_part = EnginePart(prev_line, cur_line, next_line)
        # numbers = engine_part.get_valid_numbers()
        # valid_numbers.extend(numbers)
        gear_ratio = engine_part.get_gear_ratio()
        sum_of_gear_ratios += gear_ratio
    # print(sum(valid_numbers))
    print(sum_of_gear_ratios)
    
main()
