oddelovac = "="*70

def main():
    win = False
    player1 = "O"
    positions = [*range(1, 10)]
    # úvod
    title(positions)

    while win is False:
        # vstup uživatele
        pl_input = player_input(player1)
        # hodnocení hrací plochy
        player1 = test_player_input(pl_input, player1, positions)
        # vyhodnocení hry
        win = testing_win(positions, win_player(player1))


def gameplan(nums):
    print("_____________")
    print(f"| {nums[0]} | {nums[1]} | {nums[2]} |")
    print("-------------")
    print(f"| {nums[3]} | {nums[4]} | {nums[5]} |")
    print("-------------")
    print(f"| {nums[6]} | {nums[7]} | {nums[8]} |")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print()


def player_input(player1):
    while True:
        print(f"{oddelovac}\n{oddelovac}")
        try:
            pl_input = int(input(f"Player {player1} | Please enter your position number: ")) - 1
            if -1 < pl_input < 9:
                return pl_input
            else:
                print(oddelovac)
                print("Please, insert only numbers between 1-9.")
        except:
            print(oddelovac)
            print("Please, insert only numbers.")


def test_player_input(pl_input, player1, pos):
    pl = player1
    if pos[pl_input] == "O" or pos[pl_input] == "X":
        print(oddelovac)
        print("Please, choose empty position.")
        return pl
    else:
        if player1 == "O":
            pos[pl_input] = "O"
            return "X"
        elif player1 == "X":
            pos[pl_input] = "X"
            return "O"


def testing_win(pos, win_player):
    gameplan(pos)
    if pos[0] == pos[1] == pos[2]:
        print(f"=======PLAYER {win_player} WINS!!!!=======")
        return True
    elif pos[3] == pos[4] == pos[5]:
        print(f"=======PLAYER {win_player} WINS!!!!=======")
        return True
    elif pos[6] == pos[7] == pos[8]:
        print(f"=======PLAYER {win_player} WINS!!!!=======")
        return True
    elif pos[0] == pos[3] == pos[6]:
        print(f"=======PLAYER {win_player} WINS!!!!=======")
        return True
    elif pos[1] == pos[4] == pos[7]:
        print(f"=======PLAYER {win_player} WINS!!!!=======")
        return True
    elif pos[2] == pos[5] == pos[8]:
        print(f"=======PLAYER {win_player} WINS!!!!=======")
        return True
    elif pos[0] == pos[4] == pos[8]:
        print(f"=======PLAYER {win_player} WINS!!!!=======")
        return True
    elif pos[2] == pos[4] == pos[6]:
        print(f"=======PLAYER {win_player} WINS!!!!=======")
        return True
    else:
        if all(isinstance(item, str) for item in pos):
            print("=======IT´S DRAW!!!=======")
            return True
        return False


def win_player(player):
    if player == "X":
        win_player = "O"
    else:
        win_player = "X"
    return win_player


def title(pos):
    print(oddelovac)
    print("Welcome to Tic Tac Toe\nGAME RULES:\n"
          "Each player can place one mark (or stone) per turn on the 3x3 grid\n"
          "The WINNER is who succeeds in placing three of their marks in a\n"
          "* horizontal,\n"
          "* vertical or\n"
          "* diagonal row\nLet's start the game\n")
    gameplan(pos)


main()