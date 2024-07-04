import tkinter as tk
import random

# Constants
WIDTH = 400
HEIGHT = 400
SEG_SIZE = 20
INFO_HEIGHT = 40

class Snake(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=WIDTH, height=HEIGHT + INFO_HEIGHT, background='black')
        self.master = master
        self.snake_segments = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        self.direction = 'Right'
        self.in_game = False
        self.score = 0
        self.speed = 100
        self.difficulty = 'Normal'
        self.point_multiplier = 2
        self.difficulty_menu = False

        self.pack()
        self.bind_all("<KeyPress>", self.on_key_press)

        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')

        self.score_text = self.create_text(50, HEIGHT + INFO_HEIGHT / 2, text=f"Score: {self.score}", fill="white", font="TkDefaultFont 14")
        self.difficulty_text = self.create_text(WIDTH - 80, HEIGHT + INFO_HEIGHT / 2, text=f"Difficulty: {self.difficulty}", fill="white", font="TkDefaultFont 14")

        self.show_main_menu()

    def show_main_menu(self):
        self.difficulty_menu = False
        self.delete(tk.ALL)
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
            text="Press 2: Change Difficulty", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 50,
            text="Press 3: Instructions", fill="white", font="TkDefaultFont 16"
        )

    def show_difficulty_menu(self):
        self.difficulty_menu = True
        self.delete(tk.ALL)
        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 50,
            text="Select Difficulty", fill="white", font="TkDefaultFont 24"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 10,
            text="Press 1: Easy", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 20,
            text="Press 2: Normal", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 50,
            text="Press 3: Hard", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 80,
            text="Press M: Main Menu", fill="white", font="TkDefaultFont 16"
        )

    def show_instructions(self):
        self.difficulty_menu = False
        self.delete(tk.ALL)
        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 90,
            text="Instructions", fill="white", font="TkDefaultFont 24"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 50,
            text="Use arrow keys to move the snake.", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 - 20,
            text="Eat food to grow and earn points.", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 10,
            text="Avoid running into walls or yourself.", fill="white", font="TkDefaultFont 16"
        )
        self.create_text(
            WIDTH / 2, (HEIGHT + INFO_HEIGHT) / 2 + 80,
            text="Press M: Main Menu", fill="white", font="TkDefaultFont 16"
        )

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if difficulty == 'Easy':
            self.speed = 150
            self.point_multiplier = 1
        elif difficulty == 'Normal':
            self.speed = 100
            self.point_multiplier = 2
        elif difficulty == 'Hard':
            self.speed = 50
            self.point_multiplier = 3
        self.show_main_menu()

    def start_game(self):
        self.delete(tk.ALL)
        self.create_objects(hide_food=True)
        self.countdown(3)

    def countdown(self, count):
        if count > 0:
            self.delete("countdown")
            self.create_text(
                WIDTH / 2, HEIGHT / 2,
                text=str(count), fill="white", font="TkDefaultFont 48", tag="countdown"
            )
            self.after(1000, self.countdown, count - 1)
        else:
            self.delete("countdown")
            self.in_game = True
            self.create_objects(hide_food=False)
            self.move_snake()

    def create_objects(self, hide_food=False):
        self.create_rectangle(0, HEIGHT, WIDTH, HEIGHT + INFO_HEIGHT, fill='blue', outline='')
        self.create_text(50, HEIGHT + INFO_HEIGHT / 2, text=f"Score: {self.score}", fill="white", font="TkDefaultFont 14")
        self.create_text(WIDTH - 80, HEIGHT + INFO_HEIGHT / 2, text=f"Difficulty: {self.difficulty}", fill="white", font="TkDefaultFont 14")
        for x, y in self.snake_segments:
            self.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill='green')
        if not hide_food:
            self.create_rectangle(self.food[0], self.food[1], self.food[0] + SEG_SIZE, self.food[1] + SEG_SIZE, fill='red')

    def move_snake(self):
        if self.in_game:
            head_x, head_y = self.snake_segments[0]

            if self.direction == 'Left':
                new_head = (head_x - SEG_SIZE, head_y)
            elif self.direction == 'Right':
                new_head = (head_x + SEG_SIZE, head_y)
            elif self.direction == 'Up':
                new_head = (head_x, head_y - SEG_SIZE)
            elif self.direction == 'Down':
                new_head = (head_x, head_y + SEG_SIZE)

            self.snake_segments = [new_head] + self.snake_segments[:-1]

            if self.check_collision():
                self.game_over()
            else:
                self.delete(tk.ALL)
                self.create_objects()

                if self.snake_segments[0] == self.food:
                    self.snake_segments.append(self.snake_segments[-1])
                    self.food = self.create_food()
                    self.score += self.point_multiplier
                    self.itemconfigure(self.score_text, text=f"Score: {self.score}")

                self.create_text(50, HEIGHT + INFO_HEIGHT / 2, text=f"Score: {self.score}", fill="white", font="TkDefaultFont 14")
                self.create_text(WIDTH - 80, HEIGHT + INFO_HEIGHT / 2, text=f"Difficulty: {self.difficulty}", fill="white", font="TkDefaultFont 14")

                if self.in_game:
                    self.after(self.speed, self.move_snake)

    def create_food(self):
        while True:
            x = random.randint(0, (WIDTH // SEG_SIZE) - 1) * SEG_SIZE
            y = random.randint(0, (HEIGHT // SEG_SIZE) - 1) * SEG_SIZE
            food = (x, y)
            if food not in self.snake_segments:
                return food

    def on_key_press(self, event):
        if not self.in_game:
            if self.difficulty_menu:
                if event.keysym == '1':
                    self.set_difficulty('Easy')
                elif event.keysym == '2':
                    self.set_difficulty('Normal')
                elif event.keysym == '3':
                    self.set_difficulty('Hard')
                elif event.keysym.lower() == 'm':
                    self.show_main_menu()
            else:
                if event.keysym == '1':
                    self.start_game()
                elif event.keysym == '2':
                    self.show_difficulty_menu()
                elif event.keysym == '3':
                    self.show_instructions()
                elif event.keysym.lower() == 'm':
                    self.show_main_menu()
        else:
            new_direction = event.keysym
            all_directions = ('Left', 'Right', 'Up', 'Down')
            opposites = ({'Up', 'Down'}, {'Left', 'Right'})

            if new_direction in all_directions:
                if {new_direction, self.direction} not in opposites:
                    self.direction = new_direction

    def check_collision(self):
        head_x, head_y = self.snake_segments[0]

        return (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            len(self.snake_segments) != len(set(self.snake_segments))
        )
    
    def game_over(self):
        self.in_game = False
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
        self.direction = 'Right'
        self.snake_segments = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        self.score = 0
        self.show_main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snake Game")
    game = Snake(root)
    root.mainloop()