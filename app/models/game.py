class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def check_winner(self):

        result = None

        # if both players have same hand
        if self.player_1.hand == self.player_2.hand:
            return result

        # rock beats scissors
        if self.player_1.hand == "rock":
            if self.player_2.hand == "scissors":
                #result += "Player 1 wins!"
                result = True
            else: 
                #result += "Player 2 wins"
                result = False

        # scissors beats paper
        if self.player_1.hand == "scissors":
            if self.player_2.hand == "paper":
                #result += "Player 1 wins!"
                result = True
            else: 
                #result += "Player 2 wins"
                result = False

        # paper beats rock
        if self.player_1.hand == "paper":
            if self.player_2.hand == "rock":
                #result += "Player 1 wins!"
                result = True
            else: 
                #result += "Player 2 wins"
                result = False
        
        return result    
