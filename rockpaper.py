import random 


def get_choices():
    machine_choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice rock, paper or scissors: ")
    machine_choice = random.choice(machine_choices)

    choices = {"player": player_choice, "machine": machine_choice}
    return check_win(choices["player"], choices["machine"])


def check_win(player, machine):
    if player == machine:
        return "tie"
    elif player == "rock" and machine == "scissors":
        return "you win, rock smashes scissors"
    elif player == "paper" and machine == "rock":
        return "you win, paper covers rock"
    elif player == "scissors" and machine == "paper":
        return "you win, scissors cut paper"
    else:
        return f"you lose, {machine} drestroyed {player}"
choices = get_choices()
print(choices)





