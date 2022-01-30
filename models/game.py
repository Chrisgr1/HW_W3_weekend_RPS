from models.player import Player
class Game():

    def __init__(self, player_one_choice, player_two_choice):
        self.player_one_choice = Player(player_one_choice)
        self.player_two_choice = Player(player_two_choice)

    def play_game(player_one_choice, player_two_choice):
        if player_one_choice == "rock":
            if player_two_choice == "rock":
                return "It's a draw"
            elif player_two_choice =="scissors":
                return "Player 1 wins"
            elif player_two_choice =="paper": 
                return "Player 2 wins"
            else: 
                return "Something weird has happened"
        elif player_one_choice == "scissors":
            if player_two_choice == "rock":
                return "Player 2 wins"
            elif player_two_choice =="scissors":
                return "It's a draw"
            elif player_two_choice =="paper": 
                return "Player 1 wins"
            else: 
                return "Something weird has happened"
        elif player_one_choice == "paper":
            if player_two_choice == "rock":
                return "Player 1 wins"
            elif player_two_choice =="scissors":
                return "Player 2 wins"
            elif player_two_choice =="paper": 
                return "It's a draw"
            else: 
                return "Something weird has happened"
        else: 
            return "Something weird has happened"