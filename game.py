import tkinter as tk
import random

user_score = 0
computer_score = 0
rounds_won_user = 0
rounds_won_computer = 0
current_round = 1

def display_rules():
    rules_text = """RULES
    - Rock beats scissors.
    - Scissors beat paper.
    - Paper beats rock."""
    rules_label.config(text=rules_text,font=("Times New Roman",12))

def start_game():
    start_button.pack_forget()
    rules_label.pack_forget()  
    instructions_label.pack()
    rock_button.pack()
    paper_button.pack()
    scissors_button.pack()
    quit_button.pack(pady=20)
    feedback_label.pack()  
    feedback_entry.pack()
    submit_button.pack()
    update_round_info()

def determine_winner(user_choice, computer_choice):
    global rounds_won_user, rounds_won_computer, current_round
    
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        rounds_won_user += 1
    else:
        result = "Computer wins!"
        rounds_won_computer += 1
    
    result_label.config(text=result)
    update_scores() 

    if rounds_won_user >= 2:
        game_result = f"You win the series {rounds_won_user}-{rounds_won_computer}!"
        game_over(game_result)
    elif rounds_won_computer >= 2:
        game_result = f"Computer wins the series {rounds_won_user}-{rounds_won_computer}!"
        game_over(game_result)
    else:
        current_round += 1
        update_round_info()

def update_scores():
    user_score_label.config(text=f"Your score: {rounds_won_user}")
    computer_score_label.config(text=f"Computer score: {rounds_won_computer}")


def update_round_info():
    round_label.config(text=f"Round {current_round}")

def play_again():
    instructions_label.config(text="Want to play more?")

def quit_game():
    window.destroy()

def submit_feedback():
    feedback_text = feedback_entry.get()
    feedback_label.config(text="Thank you for your feedback!",font=("Aerial",12))

def game_over(result):
    instructions_label.config(text=result,font=("Aerial",20))
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)
    quit_button.config(text="Exit")



def get_user_choice(choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    user_label.config(text=f"You chose: {choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    determine_winner(choice, computer_choice)

window = tk.Tk()
window.title("Rock Paper Scissors Game")

window.configure(bg="#ab00ff")

#window.geometry("800x600")

rules_label = tk.Label(window, text="", justify=tk.CENTER, bg="#F0E68C")
rules_label.pack()

display_rules()

start_button = tk.Button(window, text="START", command=start_game, bg= "green", fg="white", font=("Arial", 12))
start_button.pack()

round_label = tk.Label(window, text="", font=("Arial", 16))
round_label.pack()

instructions_label = tk.Label(window, text="CHOOSE ONE",pady=10)
rock_button = tk.Button(window, text="ROCK", command=lambda: get_user_choice('rock'), width=10, height=2,bg="#87CEFA",fg="black",font=("Comic Sans MS", 12))
paper_button = tk.Button(window, text="PAPER", command=lambda: get_user_choice('paper'), width=10, height=2,bg="#87CEFA",fg="black",font=("Comic Sans MS", 12))
scissors_button = tk.Button(window, text="SCISSORS", command=lambda: get_user_choice('scissors'), width=10, height=2,bg="#87CEFA",fg="black",font=("Comic Sans MS", 12))
quit_button = tk.Button(window, text="QUIT", command=quit_game, width=20, height=2, bg="red", fg="yellow",font=("Arial", 12))

user_label = tk.Label(window, text="",font=("Arial", 12))
user_label.pack()

computer_label = tk.Label(window, text="",font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(window, text="",font=("Arial", 12))
result_label.pack()

score_frame = tk.Frame(window)
score_frame.pack()

user_score_label = tk.Label(score_frame, text="Your score: 0",bg="#FFD700", font=("Arial", 12))
user_score_label.pack(side=tk.LEFT)

computer_score_label = tk.Label(score_frame, text="Computer score: 0",bg="#2F4F4F",fg="white",font=("Arial", 12))
computer_score_label.pack(side=tk.RIGHT)

feedback_label = tk.Label(window, text="Enter your feedback:",font=("Arial", 10))
feedback_label.pack()

feedback_entry = tk.Entry(window, width=50, bg="#D8BFD8",font=("Arial", 10))
feedback_entry.pack()

submit_button = tk.Button(window, text="Submit Feedback", command=submit_feedback,bg="#20B2AA",fg="black",font=("Arial", 10))
submit_button.pack()

variable = tk.StringVar()

window.mainloop()
