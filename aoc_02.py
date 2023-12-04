import re
class ValidGame:
    def __init__(self, game_data):
        self.game_id = None
        self.game_data = game_data
        self.ball_count = {'red': 0, 'green': 0, 'blue': 0}
        self.allowed_game = {'red': 12, 'green': 13, 'blue': 14}
    
    def interpret_game_data(self):
        splits = self.game_data.split(':')
        self.game_id = int(re.search('[0-9]+', splits[0]).group())
        # find the number of balls showed by elf
        pattern = "([0-9]+|red|green|blue)"
        game_str = splits[1]
        number_list = re.findall(pattern, game_str)
        for i in range(1, len(number_list), 2):
            ball_color = number_list[i]
            ball_number = int(number_list[i-1])
            if self.ball_count.get(ball_color) < ball_number:
                self.ball_count[ball_color] = ball_number
    
    def is_valid_game(self):
        is_valid = True
        self.interpret_game_data()
        for (k,v) in self.ball_count.items():
            if self.allowed_game[k] < self.ball_count[k]:
                is_valid = False
        if is_valid:
            return self.game_id
        else:
            return 0
    
    def find_power_of_set(self):
        return(self.ball_count['green']*self.ball_count['red']*self.ball_count['blue'])
        
def main():
    file = open('aoc_02.txt', 'r')
    games_data = file.readlines()
    sum = 0
    sum_of_power_of_set = 0
    for game_data in games_data:
        valid_game = ValidGame(game_data)
        id = valid_game.is_valid_game()
        sum += id
        power = valid_game.find_power_of_set()
        sum_of_power_of_set += power
    print(sum)
    print(sum_of_power_of_set)
main()
    
