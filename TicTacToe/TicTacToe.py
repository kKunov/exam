import random


def printer(table):
    print("  1   2   3")

    for index, line in enumerate(table):
        print("%s %s | %s | %s" % (index+1, line[0], line[1], line[2]))

        if index < 2:
            print("  _________")


def no_more_moves(table):
    for line in table:

        for col in line:

            if col == " ":
                return False

    return True


def is_good_input(row, col, table):
    if row < 1 or row > 3 or col < 1 or col > 3:
        return False

    if table[row-1][col-1] == ' ':
        return True

    else:
        return False


def is_game_ended(table):
    for i in range(3):

        if table[i][0] == table[i][1] == table[i][2] == "x":
            print("The Player wins!!!")
            return [True, 1]

        elif table[i][0] == table[i][1] == table[i][2] == "o":
            print("The Computer wins!!!")
            return [True, 2]

        elif table[0][i] == table[1][i] == table[2][i] == "x":
            print("The Player wins!!!")
            return [True, 1]

        elif table[0][i] == table[1][i] == table[2][i] == "o":
            print("The Computer wins!!!")
            return [True, 2]

    if table[0][0] == table[1][1] == table[2][2] == "x":
        print("The Player wins!!!")
        return [True, 1]

    elif table[0][0] == table[1][1] == table[2][2] == "o":
        print("The Computer wins!!!")
        return [True, 2]

    if table[0][2] == table[1][1] == table[2][0] == "x":
        print("The Player wins!!!")
        return [True, 1]

    elif table[0][2] == table[1][1] == table[2][0] == "o":
        print("The Computer wins!!!")
        return [True, 2]

    elif no_more_moves(table):
        print("Draw!!!")
        return [True, 0]

    else:
        return [False, 0]


def check_rows(table, possible_wins, simbol):

    for row in range(3):
        first_simbol = False

        for col in range(3):

            if table[row][col] == simbol and first_simbol is False:
                first_simbol = col

            elif table[row][col] == simbol and first_simbol == 0:

                if col == 1 and table[row][2] == ' ':
                    possible_wins.append([row, 2])

                elif col == 2 and table[row][1] == ' ':
                    possible_wins.append([row, 1])

            elif (table[row][col] == simbol and first_simbol == 1 and
                    table[row][0] == ' '):
                possible_wins.append([row, 0])

    return possible_wins


def check_col(table, possible_wins, simbol):

    for col in range(3):
        first_simbol = False

        for row in range(3):

            if table[row][col] == simbol and first_simbol is False:
                first_simbol = row

            elif (table[row][col] == simbol and first_simbol == 0):

                if row == 1 and table[2][col] == ' ':
                    possible_wins.append([2, col])

                elif row == 2 and table[1][col] == ' ':
                    possible_wins.append([1, col])

            elif (table[row][col] == simbol and first_simbol == 1 and
                    table[0][col] == ' '):
                possible_wins.append([0, col])

    return possible_wins


def check_diagonals(table, possible_wins, simbol):
    first_simbol = False

    for i in range(3):

        if table[i][i] == simbol and first_simbol is False:
            first_simbol = i

        elif table[i][i] == simbol and first_simbol == 0:

            if i == 1 and table[2][2] == ' ':
                possible_wins.append([2, 2])

            elif i == 2 and table[1][1] == ' ':
                possible_wins.append([1, 1])

        elif (table[i][i] == simbol and first_simbol == 1 and
                table[0][0] == ' '):
            possible_wins.append([0, 0])

    first_simbol = False

    if table[0][2] == simbol:
        first_simbol = 0

    if table[1][1] == simbol and first_simbol is False:
        first_simbol = 1

    elif table[1][1] == simbol and first_simbol == 0 and table[2][0] == ' ':
        possible_wins.append([2, 0])

    if table[2][0] == simbol and first_simbol == 0 and table[1][1] == ' ':
        possible_wins.append([1, 1])

    elif table[2][0] == simbol and first_simbol == 1 and table[0][2] == ' ':
        possible_wins.append([0, 2])

    return possible_wins


def can_someone_win(table, simbol):
    possible_wins = []
    possible_wins = check_rows(table, possible_wins, simbol)
    possible_wins = check_col(table, possible_wins, simbol)
    possible_wins = check_diagonals(table, possible_wins, simbol)

    return possible_wins


def count_free(table):
    free_pos = 0

    for row in table:

        for pos in row:

            if pos == ' ':
                free_pos += 1

    return free_pos


def free_pos_8(table, free_pos):
    if free_pos == 8:
        corners = [[0, 0], [0, 2], [2, 0], [2, 2]]

        if table[1][1] == 'x':
            return random.choice(corners)

        else:
            return [1, 1]

    else:
        return False


def free_pos_6(table):

    if ((table[0][0] == 'x' and table[2][2]) or
            (table[0][2] == 'x' and table[2][0] == 'x')):
        return random.choice([[1, 2], [1, 0], [0, 1], [2, 1]])

    if ((table[0][1] == 'x' and table[2][1] == 'x') or
            (table[1][0] == 'x' and table[1][2])):
        return random.choice([[0, 0], [0, 2], [2, 0], [2, 2]])

    if ((table[0][0] == 'x' and table[1][2] == 'x') or
            (table[0][1] == 'x' and table[2][2] == 'x')):
        return [0, 2]

    elif ((table[0][2] == 'x' and table[2][1] == 'x') or
            (table[1][2] == 'x' and table[2][0])):
        return [2, 2]

    elif ((table[2][2] == 'x' and table[1][0] == 'x') or
            (table[0][0] == 'x' and table[2][1])):
        return [2, 0]

    elif ((table[2][0] == 'x' and table[0][1] == 'x') or
            (table[0][2] == 'x' and table[1][0])):
        return [0, 0]


def free_pos_func(table):
    free = []

    for row in range(3):

        for col in range(3):

            if table[row][col] == ' ':
                free.append([row, col])

    return free


def no_one_can_win(table, free_pos):

    for free in free_pos:
        table[free[0]][free[1]] = 'o'

        can_pc_win = can_someone_win(table, 'o')

        if can_pc_win == []:
            table[free[0]][free[1]] = ' '

        else:
            table[free[0]][free[1]] = 'o'
            return free

    return random.choice(free_pos)


def pc(table):
    free_pos = count_free(table)
    pos_check_8 = free_pos_8(table, free_pos)

    if pos_check_8 is not False:
        return pos_check_8

    can_pc_win = can_someone_win(table, 'o')  # returns possible wins
        #in that format
        #[[row, cow], [row, col]]

    if can_pc_win != []:
        can_pc_win = random.choice(can_pc_win)
        return can_pc_win

    can_human_win = can_someone_win(table, 'x')

    if can_human_win != []:
        can_human_win = random.choice(can_human_win)
        return can_human_win

    if free_pos == 6 and table[1][1] == 'o':
        return free_pos_6(table)

    free_pos_from_func = free_pos_func(table)

    return no_one_can_win(table, free_pos_from_func)


def the_game():
    again = True
    number_of_games = 0
    pc_wins = 0
    human_wins = 0
    chance_for_pc_mistake = 1/100

    while again is True:
        player = 1
        table = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
        printer(table)
        while is_game_ended(table)[0] is False:

            if player % 2 == 1:
                row = int(input("chose row:"))
                col = int(input("chose col:"))

                while is_good_input(row, col, table) is False:
                    print("Bad input, Try again!")
                    row = int(input("chose row:"))
                    col = int(input("chose col:"))

                table[row-1][col-1] = 'x'

            else:
                if random.random() < chance_for_pc_mistake:
                    pc_chose = random.choice(free_pos_func(table))
                else:
                    pc_chose = pc(table)
                print(pc_chose)
                table[pc_chose[0]][pc_chose[1]] = 'o'
                printer(table)

            player += 1

        number_of_games += 1

        if is_game_ended(table)[1] == 1:
            human_wins += 1

        elif is_game_ended(table)[1] == 2:
            pc_wins += 1

        ask_for_one_more = input("Do you want to play again? ")

        if ask_for_one_more == 'n' or ask_for_one_more == 'no':
            again = False

        while (ask_for_one_more != 'y' and ask_for_one_more != 'yes' and
                ask_for_one_more != 'n' and ask_for_one_more != 'no'):
            print("Bad input, pleace tipe yes or no!")
            ask_for_one_more = input("Do you want to play again? ")

    print("You play %s games!" % number_of_games)
    print("You win %s games!" % human_wins)
    print("Computer win %s games!" % pc_wins)
    print("%s games was Draw!" % (number_of_games - human_wins - pc_wins))


def main():
    the_game()


if __name__ == '__main__':
    main()
