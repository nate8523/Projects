import tkinter as tk
import random

# Constants
WIDTH = 800  # Increased width for landscape layout
HEIGHT = 400
INFO_HEIGHT = 40

# ASCII Art for gestures
GESTURES = {
    1: """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    2: """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    3: """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
}

# Mirrored ASCII Art for computer's gestures
MIRRORED_GESTURES = {
    1: """
    _______
  (____   '--- 
 (_____)
 (_____)
  (____)
   (___)__.---
    """,
    2: """
       _______
  ____(____    '--- 
 (______
(_______
 (_______
  (__________.---
    """,
    3: """
       _______
  ____(____    '--- 
 (______
(__________
     (____)
      (___)__.---
    """
}

COLORS = {1: "green", 2: "yellow", 3: "red"}

class RockPaperScissors(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=WIDTH, height=HEIGHT + INFO_HEIGHT, background='black')
        self.master = master
        self.player_choice = None
        self.computer_choice = None
        self.in_game = False
        self.result_screen = False
        self.player_score = 0
        self.computer_score = 0
        self.point_multiplier = 1  # Points set to 1

        self.pack()
        self.bind_all("<KeyPress>", self.on_key_press)

        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')

        self.score_text = self.create_text(WIDTH / 2, HEIGHT + INFO_HEIGHT / 2, text=f"You: {self.player_score} vs Computer: {self.computer_score}", fill="white", font="TkDefaultFont 14")

        self.show_main_menu()

    def show_main_menu(self):
        self.delete(tk.ALL)
        self.in_game = False
        self.result_screen = False
        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 50,
            text="Main Menu", fill="white", font="TkDefaultFont 24"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 10,
            text="Press 1: Start Game", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 20,
            text="Press 2: Instructions", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 50,
            text="Press Q: Quit", fill="white", font="TkDefaultFont 16"
        )

    def show_instructions(self):
        self.delete(tk.ALL)
        self.in_game = False
        self.result_screen = False
        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 90,
            text="Instructions", fill="white", font="TkDefaultFont 24"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 50,
            text="Use keys 1, 2, 3 to choose Rock, Paper, Scissors respectively.", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 20,
            text="Rock beats Scissors, Scissors beats Paper, Paper beats Rock.", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 80,
            text="Press M: Main Menu", fill="white", font="TkDefaultFont 16"
        )

    def start_game(self):
        self.in_game = True
        self.result_screen = False
        self.delete(tk.ALL)
        self.show_game_screen()

    def show_game_screen(self):
        self.delete(tk.ALL)
        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')
        self.score_text = self.create_text(WIDTH / 2, HEIGHT + INFO_HEIGHT / 2, text=f"You: {self.player_score} vs Computer: {self.computer_score}", fill="white", font="TkDefaultFont 14")
        self.create_text(
            WIDTH / 2, HEIGHT / 2 - 50,
            text="Press 1: Rock", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, HEIGHT / 2 - 10,
            text="Press 2: Paper", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, HEIGHT / 2 + 30,
            text="Press 3: Scissors", fill="white", font="TkDefaultFont 16"
        )

    def on_key_press(self, event):
        if self.in_game:
            if event.keysym in ['1', '2', '3']:
                self.player_choice = int(event.keysym)
                self.computer_choice = random.randint(1, 3)
                self.start_countdown()
        elif self.result_screen:
            if event.keysym.lower() == 'm':
                self.show_main_menu()
            elif event.keysym == 'Return':
                self.play_again(event)
        else:
            if event.keysym == '1':
                self.start_game()
            elif event.keysym == '2':
                self.show_instructions()
            elif event.keysym.lower() == 'm':
                self.show_main_menu()
            elif event.keysym.lower() == 'q':
                self.master.quit()

    def start_countdown(self):
        self.delete(tk.ALL)
        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')
        self.after(500, lambda: self.display_countdown("Rock!"))
        self.after(1000, lambda: self.display_countdown("Paper!"))
        self.after(1500, lambda: self.display_countdown("Scissors!"))
        self.after(2000, lambda: self.display_countdown("Go!"))
        self.after(2500, self.show_result)

    def display_countdown(self, text):
        self.delete("countdown")
        self.create_text(WIDTH / 2, HEIGHT / 2, text=text, fill="white", font="TkDefaultFont 24", tags="countdown")

    def show_result(self):
        self.delete(tk.ALL)
        self.in_game = False
        self.result_screen = True
        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')
        self.score_text = self.create_text(WIDTH / 2, HEIGHT + INFO_HEIGHT / 2, text=f"You: {self.player_score} vs Computer: {self.computer_score}", fill="white", font="TkDefaultFont 14")
        self.create_text(
            WIDTH / 4, HEIGHT / 2 - 100,
            text=f"You chose:", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 4, HEIGHT / 2 - 40,
            text=GESTURES[self.player_choice], fill=COLORS[self.player_choice], font=("Courier", 12), anchor="n"
        )
        self.create_text(
            3 * WIDTH / 4, HEIGHT / 2 - 100,
            text=f"Computer chose:", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            3 * WIDTH / 4, HEIGHT / 2 - 40,
            text=MIRRORED_GESTURES[self.computer_choice], fill=COLORS[self.computer_choice], font=("Courier", 12), anchor="n"
        )
        result_text, explanation = self.get_result_text()
        self.create_text(
            WIDTH / 2, HEIGHT / 2 + 80,
            text=result_text, fill="white", font="TkDefaultFont 24"
        )
        self.create_text(
            WIDTH / 2, HEIGHT / 2 + 110,
            text=explanation, fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, HEIGHT / 2 + 140,
            text="Press Enter to play again", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, HEIGHT / 2 + 170,
            text="Press M: Main Menu", fill="white", font="TkDefaultFont 16"
        )

    def get_result_text(self):
        if self.player_choice == self.computer_choice:
            return "It's a Tie!", ""
        elif (self.player_choice == 1 and self.computer_choice == 3):
            self.player_score += self.point_multiplier
            return "You Win!", "Rock beats Scissors"
        elif (self.player_choice == 2 and self.computer_choice == 1):
            self.player_score += self.point_multiplier
            return "You Win!", "Paper beats Rock"
        elif (self.player_choice == 3 and self.computer_choice == 2):
            self.player_score += self.point_multiplier
            return "You Win!", "Scissors beats Paper"
        elif (self.player_choice == 3 and self.computer_choice == 1):
            self.computer_score += self.point_multiplier
            return "You Lose!", "Rock beats Scissors"
        elif (self.player_choice == 1 and self.computer_choice == 2):
            self.computer_score += self.point_multiplier
            return "You Lose!", "Paper beats Rock"
        elif (self.player_choice == 2 and self.computer_choice == 3):
            self.computer_score += self.point_multiplier
            return "You Lose!", "Scissors beats Paper"

    def play_again(self, event):
        self.start_game()

    def game_over(self):
        self.in_game = False
        self.result_screen = False
        self.delete(tk.ALL)
        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 20,
            text="GAME OVER", fill="white", font="TkDefaultFont 20"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 20,
            text="Press Enter to return to main menu", fill="white", font="TkDefaultFont 14"
        )
        self.master.bind("<Return>", self.reset)

    def reset(self, event):
        self.in_game = False
        self.result_screen = False
        self.player_score = 0
        self.computer_score = 0
        self.show_main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rock Paper Scissors Game")
    game = RockPaperScissors(root)
    root.mainloop()
