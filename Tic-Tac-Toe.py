drawBoard = [["_"]*3,
             ["_"]*3,
             ["_"]*3]   # Setting up the board using a list of lists (matrix)


# Initialising the variables
stringChoice = ""
intCount = 1
stringLetter = "X"
intRounds = 0
winCombos = [["0,0", "0,1", "0,2"], ["1,0", "1,1", "1,2"], ["2,0", "2,1", "2,2"],   # Horizontal wins
             ["0,0", "1,0", "2,0"], ["0,1", "1,1", "2,1"], ["0,2", "1,2", "2,2"],   # Vertical wins
             ["0,0", "1,1", "2,2"], ["0,2", "1,1", "2,0"]]  # Diagonal wins


# Print that tells the user the game has started.
print ("The game has started. To stop the game write quit.")
print ("\n")

# While loop that contains everything within the game, so it keeps looping the game. Until the condition is met.
while(stringChoice != "Quit" or "quit"):
    if(intRounds == 9):    # If the drawBoard is full inform the player that the game has finished.
        print("The game has now ended.")
        break   # If the drawBoard is not break condition.

    print ("      |       |")       # Prints out demonstration
    print ("(0, 0)| (0, 1)| (0, 2)")
    print ("------|-------|--------")
    print ("(1, 0)| (1, 1)| (1, 2)")
    print ("------|-------|--------")
    print ("(2, 0)| (2, 1)| (2, 2)")
    print ("      |       |")
    print ("\n")

    stringChoice = input("Make your move! (enter: Row, Column): ")    # Player input for Row & Column as a string
    print ("\n")
    Row = int(stringChoice[0])    # Gets 1st value in string from user input & converts to integer
    Column = int(stringChoice[3]) # Gets 4th value in string from user input & converts to integer

    if(drawBoard[Row][Column] == "_"):  # Check if row & column is empty
        drawBoard[Row][Column] = stringLetter   # Replace empty value with player's letter
        intRounds += 1     # Increment +1 to rounds


    for i in drawBoard: 	# For the integer values (row & column) in drawBoard
        print (i)   	# Print the board.
        print ("\n")    

    for j in winCombos:     # For loop to parse winning values within list of lists
        firstCombo = drawBoard[int(j[0][0])][int(j[0][2])]
        secondCombo = drawBoard[int(j[1][0])][int(j[1][2])]
        thirdCombo = drawBoard[int(j[2][0])][int(j[2][2])]

        if(firstCombo == secondCombo and firstCombo == thirdCombo and firstCombo != "_"):   # If statement that compiles winning combinations
            print ("Congrats Player " + str(intCount) + "! You have won the game!")
            print ("\n")
            intRounds = 9   # Rounds set to 9 to indicate board is full - so it ends game.
            break
        
    if(intCount == 1):  # If player 1 ("X") has finished, go to player 2
            intCount = 2
            stringLetter = "O"
    else:			# If player 2 ("O") has finished, go back to player 1
            intCount = 1
            stringLetter = "X"

