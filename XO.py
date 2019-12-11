from __future__ import print_function

Gameover = False
P1_finished = False
P2_finished = False
Pattern1 = [["▢ ", "▢ ", "▢ "],
            ["▢ ", "▢ ", "▢ "],
            ["▢ ", "▢ ", "▢ "]]

mark = 0

win_patter1 = ["✘ ", "✘ ", "✘ "] or ["⚪ ", "⚪ ", "⚪ "]


def print_pattern():
    finished = False
    ps = 0
    while finished is False:
        print(*Pattern1[ps], sep='')
        ps += 1
        if ps == 3:
            finished = True

while Gameover is False:

    if Gameover is True:
        break

    # P1 THIS GAME IS MADE BY HENRI RUBEN
    P1_finished = False
    while P1_finished is False:
        print("P1")
        posY = input("Position Y:\nY= ")
        print("________")
        posX = input("Position X:\nX= ")
        print("________")

        if int(posY) >= 4:
            print("Y: " + posY + " is not under 4!\n________\n________\n________")
            continue
        if int(posX) >= 4:
            print("X: " + posX + " is not under 4!\n________\n________\n________")
            continue

        markY = int(posY) - 1
        markX = int(posX) - 1
        mark_pos = int(posX) * int(posY)

        if Pattern1[int(markY)][int(markX)] == "✘ ":
            print("This spot is already filled!")
            continue
        if Pattern1[int(markY)][int(markX)] == "⚪ ":
            print("This spot is already filled!")
            continue

        mark = "✘ "
        (Pattern1[markY][markX]) = mark
        print_pattern()
        P1_finished = True

        # Wins THIS GAME IS MADE BY HENRI RUBEN
        if Pattern1[0] == win_patter1:
            print("P1 Wins")
            Gameover = True
        if Pattern1[1] == win_patter1:
            print("P1 Wins")
            Gameover = True
        if Pattern1[2] == win_patter1:
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][0] == mark and Pattern1[1][0] == mark and Pattern1[2][0] == mark:  # !--
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][1] == mark and Pattern1[1][1] == mark and Pattern1[2][1] == mark:  # -!-
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][2] == mark and Pattern1[1][2] == mark and Pattern1[2][2] == mark:  # --!
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][0] == mark and Pattern1[1][1] == mark and Pattern1[2][2] == mark:  # \
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][2] == mark and Pattern1[1][1] == mark and Pattern1[2][0] == mark:  # /
            print("P1 Wins")
            Gameover = True
        if "▢ " not in Pattern1[0]:
            if "▢ " not in Pattern1[1]:
                if "▢ " not in Pattern1[2]:
                    print("DRAW!")
                    Gameover = True

    if Gameover is True:
        break

    # P2 THIS GAME IS MADE BY HENRI RUBEN
    while P2_finished is False:
        print("P2")
        posY = input("Position Y:\nY= ")
        print("________")
        posX = input("Position X:\nX= ")
        print("________")

        if int(posY) >= 4:
            print("Y: " + posY + " is not under 4!\n________\n________\n________")
            continue
        if int(posX) >= 4:
            print("X: " + posX + " is not under 4!\n________\n________\n________")
            continue

        markY = int(posY) - 1
        markX = int(posX) - 1

        if Pattern1[int(markY)][int(markX)] == "⚪ ":
            print("This spot is already filled!")
            continue
        if Pattern1[int(markY)][int(markX)] == "✘ ":
            print("This spot is already filled!")
            continue

        mark = "⚪ "
        (Pattern1[markY][markX]) = mark
        print_pattern()
        P2_finished = True

        # Wins THIS GAME IS MADE BY HENRI RUBEN
        if Pattern1[0] == win_patter1:
            print("P1 Wins")
            Gameover = True
        if Pattern1[1] == win_patter1:
            print("P1 Wins")
            Gameover = True
        if Pattern1[2] == win_patter1:
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][0] == mark and Pattern1[1][0] == mark and Pattern1[2][0] == mark:  # !--
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][1] == mark and Pattern1[1][1] == mark and Pattern1[2][1] == mark:  # -!-
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][2] == mark and Pattern1[1][2] == mark and Pattern1[2][2] == mark:  # --!
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][0] == mark and Pattern1[1][1] == mark and Pattern1[2][2] == mark:  # \
            print("P1 Wins")
            Gameover = True
        if Pattern1[0][2] == mark and Pattern1[1][1] == mark and Pattern1[2][0] == mark:  # /
            print("P1 Wins")
            Gameover = True
        if "▢ " not in Pattern1[0]:
            if "▢ " not in Pattern1[1]:
                if "▢ " not in Pattern1[2]:
                    print("DRAW!")
                    Gameover = True

    P2_finished = False


print("Gameover!")
