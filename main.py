board = {1:"1",2:"2",3:"3",
         4:"4",5:"5",6:"6",
         7:"7",8:"8",9:"9"}
bot = "x"
user = "o"
while True:
    
        
    boardc = board.copy()
    boardcc = board.copy()
    mustplay = []
    realyplay = []
    justplay = []
    playthat = ""
    def playables(b):
        playables = []
        for i in b.items():
            if i[1] != "x" and i[1] != "o":
                playables.append(i[0])
        return playables

    def iswin(b):
        if b[1] == b[2] == b[3] == bot:
            return True
        elif b[4] == b[5] == b[6] == bot:
            return True
        elif b[7] == b[8] == b[9] == bot:
            return True
        elif b[1] == b[4] == b[7] == bot:
            return True
        elif b[2] == b[5] == b[8] == bot:
            return True
        elif b[3] == b[6] == b[9] == bot:
            return True
        elif b[1] == b[5] == b[9] == bot:
            return True
        elif b[3] == b[5] == b[7] == bot:
            return True
        else:
            return False

    def islose(b):
        if b[1] == b[2] == b[3] == user:
            return True
        elif b[4] == b[5] == b[6] == user:
            return True
        elif b[7] == b[8] == b[9] == user:
            return True
        elif b[1] == b[4] == b[7] == user:
            return True
        elif b[2] == b[5] == b[8] == user:
            return True
        elif b[3] == b[6] == b[9] == user:
            return True
        elif b[1] == b[5] == b[9] == user:
            return True
        elif b[3] == b[5] == b[7] == user:
            return True
        else:
            return False
    playable = playables(board)
    for i in playable:
        boardc[i] = bot
        
        if iswin(boardc):
            mustplay.append(i)
            boardc = board.copy()
        else:
            for a in playables(boardc):
                boardc[a] = user
                if islose(boardc):
                    if a not in realyplay:
                        realyplay.append(a)
                boardc = board.copy()
    boardc = board.copy()
    if mustplay == []:
        for i in playables(board):
            boardc[i] = bot
            for a in playables(boardc):
                boardc[a] = bot
                if iswin(boardc):
                    
                    if i not in justplay:
                        justplay.append(i)
                boardc = board.copy()
                boardc[i] = bot



    if mustplay != []:
        playthat = mustplay[0]

    elif realyplay != [] and justplay != []:
        just = set(justplay)
        realy = set(realyplay)
    
        if (just & realy):
            playthat = list(just & realy)[0]
        else:
            playthat = realyplay[0]
    elif realyplay != [] and justplay == []:
        print(realyplay[0])

    else:
        if 5 in playables(board):
            playthat = 5
        elif 2 in playables(board):
            playthat = 2
        elif 4 in playables(board):
            playthat = 4
        elif 6 in playables(board):
            playthat = 6
        elif 8 in playables(board):
            playthat = 8
        else:
            playthat = playables(board)[0]
    board[playthat] = bot
    
    print(f"{board[1],board[2],board[3]}\n{board[4],board[5],board[6]}\n{board[7],board[8],board[9]}")
    if iswin(board):
        print("You lose")
        break
    elif playables(board) == []:
        print("Draw")
        break
    while True:
        move = int(input("Your move: "))
        if board[move] != "x" and board[move] != "o":
            board[move] = user
            break
        else:
            print("Illegal Move!")
    if islose(board):
        print(f"{board[1],board[2],board[3]}\n{board[4],board[5],board[6]}\n{board[7],board[8],board[9]}")
        print("You win")
        break
    elif playables(board) == []:
        print(f"{board[1],board[2],board[3]}\n{board[4],board[5],board[6]}\n{board[7],board[8],board[9]}")
        print("Draw")
        break

    
    