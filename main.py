import tkinter as tk
import random


class ColorGame:
    """
    A simple color-based typing game using Tkinter.
    """

    def __init__(self, root):
        """
        Initialize the ColorGame.

        Parameters:
            root (Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("RANDOM COLOR GAME")
        self.root.geometry("475x295")

        self.colours = [
            "Red",
            "Blue",
            "Green",
            "Pink",
            "Black",
            "Yellow",
            "Orange",
            "Grey",
            "White",
            "Purple",
            "Brown",
        ]
        self.score = 0
        self.timeleft = 45

        # Top heading label text.
        self.instructions = tk.Label(
            root,
            text="Type the color of the displayed word, not the actual word text!",
            font=("Helvetica", 12),
        )
        self.instructions.pack()

        self.score_label = tk.Label(
            root,
            bd=2,
            relief="solid",
            text="Press enter to start",
            font=("Helvetica", 14),
        )
        self.score_label.pack()

        self.label = tk.Label(root, font=("Helvetica", 30))
        self.label.pack()

        self.entry = tk.Entry(root, font=("courier", 15, "bold"))
        self.entry.focus_set()
        self.entry.pack()

        self.label = tk.Label(root, font=("Helvetica", 45, "bold"))
        self.label.pack()

        # Time remaining label text.
        self.time_label = tk.Label(
            root, text=f"Time left: {self.timeleft}", font=("Helvetica", 12)
        )
        self.time_label.pack()

        self.entry.bind("<Return>", self.start_game)

    def start_game(self, event):
        """
        Start the color game when the Enter key is pressed.

        Parameters:
            event (tk.Event): The Tkinter event object.
        """
        if self.timeleft == 45:
            self.countdown()

        self.next_colour()

    def next_colour(self):
        """
        Choose and display the next color.

        This method is called during the game to update
        the color and handle user input.
        """
        if self.timeleft > 0:
            self.entry.focus_set()

            if self.entry.get().lower() == self.colours[1].lower():
                self.score += 1

            self.entry.delete(0, tk.END)
            random.shuffle(self.colours)

            self.label.config(fg=str(self.colours[1]), text=str(self.colours[0]))

            self.score_label.config(text=f"Score: {self.score}")

    def countdown(self):
        """
        Start the countdown timer.

        This method is called at the beginning of the game to initiate the timer.
        """
        if self.timeleft > 0:
            self.timeleft -= 1
            self.time_label.config(text=f"Time left: {self.timeleft}")
            self.time_label.after(1000, self.countdown)


def main():
    """
    The main function to run the color game.
    """
    root = tk.Tk()
    color_game = ColorGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()  # running the main application.
