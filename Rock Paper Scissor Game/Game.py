import numpy as np

def result(n): 
    options = ["Rock", "Paper", "Scissors"]
    if n < 1 or n > len(options):
        print("Invalid Choice!")
        return -1
    user_choice = options[n-1]
    cpu_choice = np.random.choice(options)
    print("CPU Choose:", cpu_choice)
    
    win = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
    if cpu_choice == win[user_choice]:
        print(">---CPU Wins!---<")
        return "cpu"
    elif user_choice == win[cpu_choice]:
        print(">---You Win!---<")
        return "user"
    else:
        print(">---Draw!---<")
        return "draw"

def play_game():
    print("Do you want to play the game?")
    want = int(input("0 For Quit\n1 For Play\nEnter your choice: "))
    rounds = 3
    user_score, cpu_score = 0, 0
    
    while want and rounds > 0:
        print("1 For Rock\n2 For Paper\n3 For Scissors\n0 For Quit")
        n = int(input("Enter Your Choice: ")) 
        if n == 0:
            break
        res = result(n)
        if res == "user":
            user_score += 1
        elif res == "cpu":
            cpu_score += 1
        elif res == "draw":
            user_score += 1
            cpu_score += 1
        print(f"Score - User: {user_score}, CPU: {cpu_score}")
        if 1 <= n <= 3:
            rounds -= 1
    
    if want == 0:
        print("As your wish!")
    elif user_score > cpu_score:
        print("Congratulations! You win the game!")
    elif user_score < cpu_score:
        print("You lose! Better luck next time.")
    else:
        print("Game Draw")

play_game()