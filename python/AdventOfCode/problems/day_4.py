from time import sleep

class Card:
    
    def __init__(self, card_num, win_numbers, numbers):
        self.card_num = card_num
        self.win_numbers = win_numbers
        self.numbers = numbers
        self.amount = 1
    
    def __str__(self):
        return f"Card {self.card_num}: {self.win_numbers} | {self.numbers}"

    def get_points(self):
        points = 0

        for num in self.numbers:
            if num in self.win_numbers:
                if points == 0:
                    points += 1
                else:
                    points *= 2
        
        return points
    
    def get_matches(self):
        matches = 0

        for num in self.numbers:
            if num in self.win_numbers:
                matches += 1
        
        card_matches = [n + self.card_num for n in range(1,matches+1,1)]
        return card_matches
    

def day_four():
    
    file_input = open("InputFiles/day_four.txt")
    cards = []

    for line in file_input:

        temp_num, temp_numbers = line.split(":") 
        
        card_num = temp_num.replace("Card", "")
        card_num = card_num.strip()

        winning_nums, nums = temp_numbers.split("|")
        
        nums = [n.replace("\n","") for n in nums.split(" ")]

        winning_nums = [int(nums.strip()) for nums in winning_nums.split(" ") if nums.isdigit()]
        nums = [int(n.strip()) for n in nums if n.isdigit()]

        cards.append(Card(int(card_num), winning_nums, nums))
        
    for i in range(len(cards)):

        for m in cards[i].get_matches():
            if m > 218:
                break
            cards[m-1].amount += cards[i].amount


    print ("Resultado del dia 4 parte 1: ", sum([n.get_points() for n in cards]))
    print("Resultado del dia 4 parte 2", sum([n.amount for n in cards]))