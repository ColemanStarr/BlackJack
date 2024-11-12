import random 

class Player:
    
    #Defines Basic Player Info 
    def __init__(self, name):
        self.name = name

    def set_balence(self):
        balence_value = False

        while not balence_value:
            self.balence = input("What is your balence?\n$")

            try:
                self.balence = int(self.balence)
                break
            except ValueError:
                print("Please type a number")

    def update_balence(self, bet, outcome):

        if outcome:
            self.balence += bet
        else:
            self.balence -= bet

        

class Casino:
    
    def choose_game(self):
        undecided = True

        while undecided:
            game = input("What game are you playing (Blackjack = 1, Roulette = 2, Slots = 3\n")
            try:
                if int(game) == 1:
                    print("Blackjack")
                    blackjack_game = Blackjack()
                    blackjack_game.play()
                    break
                elif int(game) == 2:
                    print("Roulette!")
                    break
                elif int(game) == 3:
                    print("Slots!")
                    break
                else:
                    print("Please input a number 1-3")
            except ValueError:
                print("Please input a number 1-3")

    def continue_game(self):
        keep_playing = True

        while keep_playing:
            stop = input("Keep Playing?\n")
            if stop.upper() == "Y":
                return True
            elif stop.upper() == "N":
                print("Thanks For Playing!")
                return False
            else:
                print("Please type in Y or N")

    def set_bet(self, balence):
        fair_bet = False

        while not fair_bet:
            self.bet = input(f"How Much would you like to bet? (player balence = {balence}$) \n$")

            try:
                if int(self.bet) > balence:
                    print("Please bet within your balence")
                elif int(self.bet) == balence:
                    print("All In!")
                    fair_bet = True
                    return int(self.bet)
                elif int(self.bet) < balence:
                    fair_bet = True
                    return int(self.bet)
            except ValueError:
                print("Please input a number")

#Get Basic Player Information / Starts Game
print("Welcome to The Casino!")
player_name = input("Whats Your Name?\n")
playing = True

#Creating Player and Casino classes
player = Player(player_name)
player.set_balence()
casino = Casino()

#Game Classes
class Blackjack:

    def __init__(self):
        self.dealer_points = 0
        self.player_points = 0

        print("Welcome to Blackjack!")
        self.bet = casino.set_bet(player.balence)

    def play(self):
        game = True
        card_values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
            "Ace": 11}
        
        dealer_card, dealer_point = random.choice(list(card_values.items()))
        player_card, player_point = random.choice(list(card_values.items()))

        while game:

            self.dealer_points += dealer_point
            self.player_points += player_point

            print(f"Dealer Drew a {dealer_card} worth {dealer_point} points, Dealer is at {self.dealer_points}")
            print(f"You Drew a {player_card} worth {player_point} points, You are at {self.player_points}")

            next_round = True

            while next_round:
                hit = input("Hit? (Y or N)")
                if hit.upper() == "Y":
                    player_card, player_point = random.choice(list(card_values.items()))
                    dealer_card, dealer_point = random.choice(list(card_values.items()))

                    self.dealer_points += dealer_point
                    self.player_points += player_point

                    print(f"You Drew a {player_card} worth {player_point} points, You are at {self.player_points}")
                    print(f"Dealer Drew a {dealer_card} worth {dealer_point} points, Dealer is at {self.dealer_points}")
                    
                    if self.player_points > 21 or self.dealer_points == 21:
                        print("Dealer Wins!")
                        player.update_balence(self.bet, False)
                        print(f"Remaining Balence: ${player.balence}")
                        next_round = False
                        game = False
                    elif self.player_points == 21 or self.dealer_points > 21:
                        print("You Win!")
                        player.update_balence(self.bet, True)
                        print(f"Remaining Balence: ${player.balence}")
                        next_round = False
                        game = False
            
                elif hit.upper() == "N":

                    dealer_card, dealer_point = random.choice(list(card_values.items()))

                    self.dealer_points += dealer_point

                    print(f"You stayed, your points are at {self.player_points}")
                    print(f"Dealer Drew a {dealer_card} worth {dealer_point} points, Dealer is at {self.dealer_points}")

                    if self.player_points > 21 or self.dealer_points == 21:
                        print("Dealer Wins!")
                        player.update_balence(self.bet, False)
                        print(f"Remaining Balence: ${player.balence}")
                        next_round = False
                        game = False
                    elif self.player_points == 21 or self.dealer_points > 21:
                        print("You Win!")
                        player.update_balence(self.bet, True)
                        print(f"Remaining Balence: ${player.balence}")
                        next_round = False
                        game = False
                else:
                    print("Please type in Y or N")



#Game Loop
while playing:

    casino.choose_game()

    playing = casino.continue_game()
    
    








