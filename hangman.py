import random

word = ["cat", "dog", "bird", "inu", "neko", "ooo"]
x = random.choice(word)

def hangman(x):
    wrong = 0
    stages = ["",
              "___________         ",
              "|                   ",
              "|          |        ",
              "|          O        ",
              "|         /|\       ",
              "|         / \       ",
              "|                   "
              ]
    rletters = list(x)
    board = ["_"] * len(x)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字予想してね！"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は　{}.".format(x))

hangman(x)
