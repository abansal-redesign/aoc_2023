import re

class EnginePart:
    def __init__(self, prev_line, cur_line, next_line):
        self.prev_line = prev_line
        self.cur_line = cur_line
        self.next_line = next_line
        self.valid_numbers = []
        
    def find_numbers(self):
        numbers = []
        pattern = "[0-9]+"
        num_iterator = re.finditer(pattern, self.cur_line)
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
    
    def get_valid_numbers(self):
        numbers = self.find_numbers()
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
        numbers = engine_part.get_valid_numbers()
        valid_numbers.extend(numbers)
    print(sum(valid_numbers))
    
main()
