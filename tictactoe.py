print(f"""---------
|       |
|       |
|       |
---------""")

m = "         "
matrix = [[m[0], m[1], m[2]], [m[3], m[4], m[5]], [m[6], m[7], m[8]]]

#(1, 3) (2, 3) (3, 3)
#(1, 2) (2, 2) (3, 2)
#(1, 1) (2, 1) (3, 1)

def matriks():
    print(f"""---------
| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |
| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |
| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |
---------""")

def the_game():
    playerX = 0
    playerO = 0
    x_wins = 0
    o_wins = 0

    while True:
        try:
            x, y = input("Enter the coordinates:").split()
            if 1 <= int(x) <= 3 and 1 <= int(y) <= 3:
                if int(x) == 1 and int(y) == 1:
                    if matrix[2][0] == " ":
                        if playerX == playerO:
                            matrix[2][0] = "X"
                            playerX += 1
                            matriks()
                        else:
                            matrix[2][0] = "O"
                            playerO += 1
                            matriks()
                    elif matrix[2][0] != " ":
                        print("This cell is occupied! Choose another one!")

                if int(x) == 2 and int(y) == 1:
                    if matrix[2][1] == " ":
                        if playerX == playerO:
                            matrix[2][1] = "X"
                            playerX += 1
                            matriks()
                        else:
                            matrix[2][1] = "O"
                            playerO += 1
                            matriks()
                    elif matrix[2][1] != " ":
                        print("This cell is occupied! Choose another one!")

                if int(x) == 3 and int(y) == 1:
                    if matrix[2][2] == " ":
                        if playerX == playerO:
                            matrix[2][2] = "X"
                            playerX += 1
                            matriks()
                        else:
                            matrix[2][2] = "O"
                            playerO += 1
                            matriks()
                    elif matrix[2][2] != " ":
                            print("This cell is occupied! Choose another one!")

                if int(x) == 1 and int(y) == 2:
                    if matrix[1][0] == " ":
                        if playerX == playerO:
                            matrix[1][0] = "X"
                            playerX += 1
                            matriks()
                        else:
                            matrix[1][0] = "O"
                            playerO += 1
                            matriks()
                    elif matrix[1][0] != " ":
                        print("This cell is occupied! Choose another one!")

                if int(x) == 2 and int(y) == 2:
                    if matrix[1][1] == " ":
                        if playerX == playerO:
                            matrix[1][1] = "X"
                            playerX += 1
                            matriks()
                        else:
                            matrix[1][1] = "O"
                            playerO += 1
                            matriks()
                    elif matrix[1][1] != " ":
                        print("This cell is occupied! Choose another one!")

                if int(x) == 3 and int(y) == 2:
                    if matrix[1][2] == " ":
                        if playerX == playerO:
                            matrix[1][2] = "X"
                            playerX += 1
                            matriks()
                        else:
                            matrix[1][2] = "O"
                            playerO += 1
                            matriks()
                    elif matrix[1][2] != " ":
                        print("This cell is occupied! Choose another one!")

                if int(x) == 1 and int(y) == 3:
                    if matrix[0][0] == " ":
                        if playerX == playerO:
                            matrix[0][0] = "X"
                            playerX += 1
                            matriks()
                        else:
                            matrix[0][0] = "O"
                            playerO += 1
                            matriks()
                    elif matrix[0][0] != " ":
                        print("This cell is occupied! Choose another one!")

                if int(x) == 2 and int(y) == 3:
                    if matrix[0][1] == " ":
                        if playerX == playerO:
                            matrix[0][1] = "X"
                            playerX += 1
                            matriks()
                        else:
                            matrix[0][1] = "O"
                            playerO += 1
                            matriks()
                    elif matrix[0][1] != " ":
                        print("This cell is occupied! Choose another one!")

                if int(x) == 3 and int(y) == 3:
                    if matrix[0][2] == " ":
                        if playerX == playerO:
                            matrix[0][2] = "X"
                            playerX += 1
                            matriks()
                        else:
                            matrix[0][2] = "O"
                            playerO += 1
                            matriks()
                    elif matrix[0][2] != " ":
                        print("This cell is occupied! Choose another one!")

                if int(x) not in range(1,4):
                    print("Coordinates should be from 1 to 3!")

                if int(y) not in range(1,4):
                    print("Coordinates should be from 1 to 3!")

                if matrix[1][1] == matrix[0][0] == matrix[2][2] == "X" or matrix[0][2] == matrix[1][1] == matrix[2][0] == "X":
                    x_wins += 1
                elif matrix[1][1] == matrix[0][0] == matrix[2][2] == "O" or matrix[0][2] == matrix[1][1] == matrix[2][0] == "O":
                    o_wins += 1
                else:
                    for i in range(3):
                        if matrix[i][0] == matrix[i][1] == matrix[i][2] == "X" or matrix[0][i] == matrix[1][i] == matrix[2][i] == "X":
                            x_wins += 1
                        elif matrix[i][0] == matrix[i][1] == matrix[i][2] == "X" or matrix[0][i] == matrix[1][i] == matrix[2][i] == "O":
                            o_wins += 1

                if abs(playerX - playerO) >= 2:
                    print("Impossible")
                    break

                elif x_wins and o_wins:
                    print("Impossible")
                    break

                elif x_wins:
                    print("X wins")
                    break

                elif o_wins:
                    print("O wins")
                    break

                elif not x_wins and not o_wins and playerX + playerO == 9:
                    print("Draw")
                    break

            else:
                print("Coordinates should be from 1 to 3!")

        except ValueError:
            print("You should enter numbers!")
the_game()
