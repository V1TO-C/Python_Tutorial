import random
oddelovac = "="*40


def main():
    win = False
    turns = 0
    generated_number = num_gen()
    # vygenerovat číslo
    print("Hi there!\nI've generated a random 4 digit number for you.")

    while win is False:
        bulls_count = testing_nums(player_input(), generated_number)
        # zadání čísla uživatelem
        # kontrola zadaného čísla
        # test shody vloženého a generovaného čísla
        win = testing_win_condition(bulls_count)
        # test ukončení
        turns += 1
        turns_counting(turns, win)
        # hodnocení hry


def num_gen():
    nums = [*range(10)]
    num = (random.sample(nums, 4))
    return num


def player_input():
        while True:
            try:
                print(oddelovac)
                ls = list(map(int, input("Enter a four digit number: ")))
                if not len(ls) == 4:
                    print("Please insert only 4 digits number.\n")
                else:
                    break
            except:
                print("Please insert only numbers.\n")
        return ls


def testing_nums(try_numbers, generated_numbers):
    bulls = 0
    cows = 0
    for num in generated_numbers:
        if num in try_numbers:
            cows += 1
    for num in enumerate(generated_numbers):
        if num in enumerate(try_numbers):
            bulls += 1
            cows -= 1
    print(f"You have {bulls} bulls and {cows} cows.")
    return bulls


def testing_win_condition(int1):
    if int1 == 4:
        return True
    else:
        print("Try again!\n")
        return False


def turns_counting(turns, win):
    while win is True:
        if turns < 2:
            return print(f"You made it in {turns} turn, You are amazing!!!")
        elif turns < 7:
            return print(f"You made it in {turns} turns, You are amazing!!!")
        elif turns < 10:
            return print(f"You made it in {turns}, Good work!!!")
        elif turns < 15:
            return print(f"You made it in {turns}, Not so bad!!!")
        elif turns < 20:
            return print(f"You made it in {turns}, Work hard, play hard!!!")
        else:
            return print(f"You made it in {turns}, Try to think next time!!!")


main()