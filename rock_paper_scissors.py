import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player, computer):
    if player == computer:
        return "tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "scissors" and computer == "paper") or \
       (player == "paper" and computer == "rock"):
        return "win"
    return "lose"


def play_game():
    wins = 0
    losses = 0
    ties = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player_choice = input("\nEnter your choice (rock, paper, or scissors): ").strip().lower()

        if player_choice not in ("rock", "paper", "scissors"):
            print("Invalid option! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "win":
            print("You win this round!")
            wins += 1
        elif result == "lose":
            print("You lose this round!")
            losses += 1
        else:
            print("It's a tie!")
            ties += 1

        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            break

    print("\n--- Game Over ---")
    print(f"Your score: {wins} win(s), {losses} loss(es), {ties} tie(s)")


if __name__ == "__main__":
    play_game()
