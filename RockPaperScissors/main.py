import random
import sys

class RPS:
    def __init__(self):
        print("Welcome to RPS 9000!")

        self.moves: dict = {
            "rock": '🪨',
            "paper": '📃',
            "scissors": "✂︎"
        }
        self.valid_moves: list[str] = list(self.moves.keys())

        self.user_score: int = 0
        self.ai_score: int = 0

    def play_game(self):
        user_move: str = input("Rock, Paper, or scissors? >> ").lower()

        if user_move == 'exit':
            print("Thanks for playing!")
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move.")
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print("------")
        print(f"You played {self.moves[user_move]}")
        print(f"AI played {self.moves[ai_move]}")
        print("------")


    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print("It's a tie!")
        elif user_move == 'rock' and ai_move == 'scissors':
            print("You win!")
            self.user_score += 1
        elif user_move == 'paper' and ai_move == 'rock':
            print("You win!")
            self.user_score += 1
        elif user_move == 'scissors' and ai_move == 'paper':
            print("You win!")
            self.user_score += 1
        else:
            print("AI WINS!")
            self.ai_score += 1

if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()
        print(f"Score: You {rps.user_score} | AI {rps.ai_score}")