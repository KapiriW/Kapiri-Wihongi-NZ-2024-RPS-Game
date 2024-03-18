
# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:
        # get user response  and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instruction():
    print('''
to begin, choose the number of rounds (or press <enter> for infinite mode).
Then play against the computer You eed to choose R (rock), P (paper) or S (scissors).
The rules are as follows:
 Paper beats rock
Pock beats scissors
Scissors beats paper''')


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

rps_list = ["rock", "Paper", "scissors", "xxx"]


print(" Rock / Paper / Scissors game ")
print()
want_instructions = string_checker("Do you want to read the instructions?").lower()
# checks user enter y or n
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
# Game loop starts here
while rounds_played < num_rounds:
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)
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
