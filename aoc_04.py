import re
won_scratch_card = {}
class WinningCard:
    def __init__(self, card_num, card_data):
        self.card = card_data.split(':')[1]
        self.card_num = card_num
        self.winning_numbers = []
        self.player_numbers = []
        self.player_winning_numbers = []
        self.card_point = 0
        self.find_winning_numbers()
        self.find_player_numbers()
        self.find_player_winning_numbers()
    
    def find_winning_numbers(self):
        winning_str = self.card.split('|')[0]
        self.winning_numbers = [int(num) for num in re.findall('[0-9]+', winning_str)]

    def find_player_numbers(self):
        player_str = self.card.split('|')[1]
        self.player_numbers = [int(num) for num in re.findall('[0-9]+', player_str)]

    def find_player_winning_numbers(self):
        for each_num in self.winning_numbers:
            if each_num in self.player_numbers:
                self.player_winning_numbers.append(each_num)
        for i in range(1, len(self.player_winning_numbers) + 1):
            multiplier = won_scratch_card.get(self.card_num)
            won_scratch_card[self.card_num + i] += multiplier
        print(self.player_winning_numbers)
        self.card_point = int(pow(2, len(self.player_winning_numbers) - 1))
        # print(self.card_point)
        
    
def main():
    file = open("aoc_04.txt", "r")
    cards = file.readlines()
    total_points = 0
    i = 1
    for each in range(0, len(cards)):
        won_scratch_card[i] = 1
        i += 1
    for card in range(0, len(cards)):
        card_num = card + 1
        card_data = cards[card]
        win_card = WinningCard(card_num, card_data)
        # total_points += win_card.card_point
    # print(total_points)
    print(won_scratch_card)
    print(sum(list([v for v in won_scratch_card.values()])))
        
    
    
main()
