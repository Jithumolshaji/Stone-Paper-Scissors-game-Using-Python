import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_name = input("Enter your name: ")
    print(f"Welcome to Rock, Paper, Scissors, {player_name}!")

    player_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))
    current_round = 1

    while current_round <= rounds:
        print(f"Round {current_round}")
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors"): 
             (player_choice == "paper" and computer_choice == "rock") 
             (player_choice == "scissors" and computer_choice == "paper")
             print(f"{player_name} wins this round!")
             player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Current Score - {player_name}: {player_score}, Computer: {computer_score}")
        current_round += 1

    print("Game Over!")
    if player_score > computer_score:
        print(f"The winner is {player_name} with a score of {player_score}! Congratulations!")
    elif player_score < computer_score:
        print(f"The computer wins with a score of {computer_score}!")
    else:
        print(f"It's a tie! {player_name} and the computer scored {player_score}!")

rock_paper_scissors()


