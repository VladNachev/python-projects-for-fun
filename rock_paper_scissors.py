class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        moves = ["rock", "paper", "scissors"]
        p1_move = self.player1.move()
        p2_move = self.player2.move()
        print(f"Player 1 chose {p1_move}, and Player 2 chose {p2_move}")
        if p1_move == p2_move:
            print("Tie!")
        elif (p1_move == "rock" and p2_move == "scissors") or (p1_move == "paper" and p2_move == "rock") or (p1_move == "scissors" and p2_move == "paper"):
            print("Player 1 wins!")
            self.player1.score += 1
        else:
            print("Player 2 wins!")
            self.player2.score += 1

class HumanPlayer:
    def __init__(self):
        self.score = 0

    def move(self):
        move = input("Enter rock, paper, or scissors: ")
        while move not in ["rock", "paper", "scissors"]:
            move = input("Invalid input. Enter rock, paper, or scissors: ")
        return move

class ComputerPlayer:
    def __init__(self):
        self.score = 0

    def move(self):
        import random
        return random.choice(["rock", "paper", "scissors"])

def main():
    player1 = HumanPlayer()
    player2 = ComputerPlayer()
    game = Game(player1, player2)
    while True:
        game.play()
        print(f"Current score: Player 1 = {player1.score}, Player 2 = {player2.score}")
        if player1.score == 3 or player2.score == 3:
            break

if __name__ == "__main__":
    main()