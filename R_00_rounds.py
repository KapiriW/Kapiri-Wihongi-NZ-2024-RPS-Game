# Check that users have entered a valid
# option based on a list
def int_check(question):
    while True:
        error = "please enter an integer that is 1 or more."

        to_check = input(question)
        # check for infinite mode
        if question == "":
            return "infinite"
        try:
            response = int(to_check)
            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine Starts Here

# Initialize game variables
mode = "regular"
rounds_played = 0


print(" Rock / Paper / Scissors game ")
print()
# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")
    rounds_played += 1

    # rounds heading
    if mode == "infinite":
        rounds_played = f"\n Round {rounds_played + 1} of {num_rounds} "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    if user_choice == "xxx":
        break

    # if users are in inf mode increase number of rounds
    if mode == "infinite":
        num_rounds += 1
# Game history / Statistics area
