import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_label = tk.Label(root, text="Your Choice:")
        self.user_choice_label.grid(row=0, column=0)

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("")

        choices = ["Rock", "Paper", "Scissors"]
        self.user_choice_menu = tk.OptionMenu(root, self.user_choice_var, *choices)
        self.user_choice_menu.grid(row=0, column=1)

        self.play_button = tk.Button(root, text="Play", command=self.play_game)
        self.play_button.grid(row=0, column=2)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=1, column=1)

        self.score_label = tk.Label(root, text="Score: User {} - {} Computer".format(self.user_score, self.computer_score))
        self.score_label.grid(row=2, column=1)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.grid(row=3, column=1)

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text="Result: {}".format(result))
        self.update_score(result)
        self.update_score_label()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

    def update_score_label(self):
        self.score_label.config(text="Score: User {} - {} Computer".format(self.user_score, self.computer_score))

    def play_again(self):
        self.user_choice_var.set("")
        self.result_label.config(text="")
        self.play_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
