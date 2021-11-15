# rock paper scissor game

import random
import tkinter as tk

# declare variables
selection=""  # set selection for button choice
computer=""
res=""
win = 0
lose = 0
tie = 0

def lets_play():  # computer will choose random selection
    global computer
    choices = ['Rock', 'Paper', 'Scissor']
    computer = random.choice(choices)

def rock():
    global selection  # global reference
    global computer
    global tie
    global lose
    global win
    lets_play()  # called to evaluate
    selection = "Rock"
    if selection == computer:
        tie = tie + 1
        output.set("You Tied!")
        run_score.set("Total Games Tied " + str(tie))
    elif computer == 'Scissor':
        win = win + 1
        output.set("Computer choose: " + computer + "You Won!")
        run_score.set("Total Games Won " + str(win))
    elif computer == 'Paper':
        lose = lose + 1
        output.set("Computer choose: " + computer + "You Lose!")
        run_score.set("Total Games Lost " + str(lose))

def paper():
    global selection  # global reference
    global computer
    global tie
    global lose
    global win
    lets_play()  # called to evaluate
    selection = "Paper"
    if selection == computer:
        tie = tie + 1
        output.set("You Tied!")
        run_score.set("Total Games Tied " + str(tie))
    elif computer == 'Rock':
        win = win + 1
        output.set("You Win! Computer choose " + computer)
        run_score.set("Total Games Won " + str(win))
    elif computer == 'Scissor':
        lose = lose + 1
        output.set("You Lose! Computer choose " + computer)
        run_score.set("Total Games Lost " + str(lose))

def scissor():
    global selection  # global reference
    global computer
    global tie
    global lose
    global win
    lets_play()  # called to evaluate
    selection = "Scissor"
    if selection == computer:
        tie = tie + 1
        output.set("You Tied!")
        run_score.set("Total Games Tied " + str(tie))
    elif computer == 'Paper':
        win = win + 1
        output.set("You Win! Computer choose: " + computer)
        run_score.set("Total Games Won " + str(win))
    elif computer == 'Rock':
        lose = lose + 1
        output.set("You Lose! Computer choose: " + computer)
        run_score.set("Total Games Lost " + str(lose))

# create root window
root_window = tk.Tk()
root_window.configure(bg="#000000")  # black background for window
root_window.title("Rock Paper Scissor Game!")
root_window.minsize(width=450, height=180)

# frames for all widgets
# frame 1 - for outcome display
frame1 = tk.Frame(root_window, pady=3, bg="#000000")  # bg frame set to black, paddy set here not in button
frame1.pack(expand=True, fill="both")
# frame 2 - button for rock, paper, scissor
frame2 = tk.Frame(root_window, pady=3.5, bg="#000000")
frame2.pack(expand=True, fill='both')
# frame 3 - button for lets play
frame3 = tk.Frame(root_window, pady=3, bg="#000000")
frame3.pack(expand=True, fill="both")


output = tk.StringVar()  # for label to show output
# label for outcome
# frame 1
lbl_result = tk.Label(frame1,
                      relief=tk.SUNKEN,
                      border=10, font=("verdana", 15),
                      anchor="center",  # center text
                      bg="#5DADE2",
                      textvariable=output  # print output result
                      )
lbl_result.pack(expand=True, fill="both")

# button for rock
# frame 2
btn_rock = tk.Button(frame2, relief=tk.GROOVE,
                     text="Rock", font=("verdana", 15),
                     border=5, anchor="center",
                     bg="#A569BD", activebackground="#7B68EE",  # set bg to change color when clicked
                     command=rock
                     )
btn_rock.configure(font="bold")
btn_rock.pack(side=tk.LEFT, expand=True, fill='both')
# button for paper
# frame 2
btn_paper = tk.Button(frame2, relief=tk.GROOVE,
                    text="Paper", font=("verdana", 15),
                    border=5, anchor="center",
                    bg="#A569BD", activebackground="#7B68EE",
                    command=paper
                    )
btn_paper.configure(font="bold")
btn_paper.pack(side=tk.LEFT, expand=True, fill='both')

# button for scissor
# frame 2
btn_scissor = tk.Button(frame2, relief=tk.GROOVE,
                         text="Scissor", font=("verdana", 15),
                         border=5, anchor="center",
                         bg="#A569BD", activebackground="#7B68EE",
                         command=scissor
                         )
btn_scissor.configure(font="bold")
btn_scissor.pack(side=tk.LEFT, expand=True, fill='both')

# label for record
# frame 3
run_score = tk.StringVar()  # for label to show running record
lbl_score = tk.Label(frame3,
                      relief=tk.SUNKEN,
                      border=10, font=("verdana", 15),
                      anchor="center",  # center text
                      bg="#2E86C1",
                      textvariable=run_score  # print output result
                      )
lbl_score.pack(expand=True, fill="both")


root_window.mainloop()

