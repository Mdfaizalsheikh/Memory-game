import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Matching Game")
        self.root.resizable(False, False)

        # List of emoji images to use on the cards
        self.images = ["🍎", "🍌", "🍇", "🍓", "🍒", "🍍", "🥭", "🍉"]
        self.images *= 2  # Duplicate the list to create pairs of each image
        random.shuffle(self.images)  # Shuffle the list to randomize the card positions

        # Initialize the game state
        self.buttons = []
        self.flipped = []
        self.matched = []
        self.create_widgets()

    def create_widgets(self):
      
        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.root, text="❓", width=10, height=5, command=lambda i=i, j=j: self.flip_card(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def flip_card(self, i, j):
        
        if (i, j) in self.flipped or (i, j) in self.matched:
            return

        self.buttons[i][j].config(text=self.images[i * 4 + j])
        self.flipped.append((i, j))

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        i1, j1 = self.flipped[0]
        i2, j2 = self.flipped[1]

        if self.images[i1 * 4 + j1] == self.images[i2 * 4 + j2]:
            self.matched.extend(self.flipped)
        else:
            # Hide the cards again if they do not match
            self.buttons[i1][j1].config(text="❓")
            self.buttons[i2][j2].config(text="❓")

        self.flipped = []

        if len(self.matched) == len(self.images):
            messagebox.showinfo("Memory Matching Game", "Congratulations! You have matched all the cards!")
            self.reset_game()

    def reset_game(self):
         
        random.shuffle(self.images)
        for i in range(4):
            for j in range(4):
                self.buttons[i][j].config(text="❓")
        self.flipped = []
        self.matched = []

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryGame(root)
    root.mainloop()
