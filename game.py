import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]
    
    # Validate player input
    while player_choice not in options:
        player_choice = input("Invalid choice! Please enter rock, paper, or scissors: ").lower()
    
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a Tie!"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! You win!"
    elif player == "rock" and computer == "paper":
        return "Paper covers rock! You lose!"
    elif player == "paper" and computer == "rock":
        return "Paper covers rock! You win!"
    elif player == "paper" and computer == "scissors":
        return "Scissors cuts paper! You lose!"
    elif player == "scissors" and computer == "rock":
        return "Rock smashes scissors! You lose!"
    elif player == "scissors" and computer == "paper":
        return "Scissors cuts paper! You win!"

# Main game execution
if __name__ == "__main__":
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)