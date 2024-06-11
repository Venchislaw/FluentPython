import random


"""
This project idea was taken from "The big book of small python projects"

In this game we have 10 attempts to guess three-digit number.
Programm will be giving us some feedback:

1. Pico - Right digit in wrong position
2. Fermi - Right digit in right position
3. Bagels - Digit is not in number
"""


# my solution to the problem

"""
Okay, we have to code simple game.
I think we can have an iterative solution through simple while loop.
We'll have 
"""


def bagels_game(n_digits, n_attempts):
    print(f"""Hello! I'm Bagels! \n Let's play a game!\n
             Rules: \n {'-' * 60} \n
             You'll have to guess {n_digits} number in
             {n_attempts} attempts. \n
             I give you feedback about your guess: \n
             1. Pico - Right digit in wrong position.
             2. Fermi - Right digit in right position
             3. Bagels - Digit is not in number \n
             
             You get it?
""")
    
    right_choices = 0
    total_choices = 0
    SECRET_NUMBER = get_random_num(n_digits)
    checked = set()
    
    while (total_choices <= n_attempts) and (right_choices < n_digits):
        digit = input("Enter digit: ")
        index = input("Enter index: ")
        
        if len(digit) != 1 or len(index) > n_digits:
            print("WTF are you doing?")
            continue
        
        feedback = feedback_func(digit, index, SECRET_NUMBER)
        print(feedback)
        
        if feedback == "Fermi" and digit not in checked:
            right_choices += 1
            checked.add(digit)
        
        total_choices += 1
        
    if right_choices == n_digits:
        print("You won!")
        replay_status = input("Replay? Y|N: ")
        
        if replay_status == "Y":
            return bagels_game(n_digits, n_attempts)
        
    else:
        print("You Lost!")
        replay_status = input("Replay? Y|N: ")
        
        if replay_status == "Y":
            return bagels_game(n_digits, n_attempts)
    
    return "Thanks for the game! GoodBye!"


def get_random_num(n_digits):
    digs = list("0123456789")
    random.shuffle(digs)
    return "".join(digs[:n_digits])
    

def feedback_func(digit, index, sec_n):
    if digit in sec_n and int(index)-1 != sec_n.index(digit):
        return "Pico"
    elif sec_n[int(index)-1] == digit:
        return "Fermi"
    else:
        return "Bagels"
    
    
print(bagels_game(3, 10))