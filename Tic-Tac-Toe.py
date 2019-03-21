drawBoard = [["_"]*3,
             ["_"]*3,
             ["_"]*3]   # Setting up the board using a list of lists (matrix)


# Initialising the variables
Choice = ""
Count = 1
Letter = "X"
Rounds = 0

# Print that tells the user the game has started.
print ("The game has started. To stop the game write quit.")
print ("\n")

# While loop that contains everything within the game, so it keeps looping the drawBoard.
while(Choice != "Quit" or "quit"):
    if(Rounds == 9):    # If the drawBoard is full inform the player that the game has finished.
        print("The game has finished!")
        break   # If the drawBoard is not full continue loop.

    print ("      |       |")       # Prints out demonstration
    print ("(0, 0)| (0, 1)| (0, 2)")
    print ("------|-------|--------")
    print ("(1, 0)| (1, 1)| (1, 2)")
    print ("------|-------|--------")
    print ("(2, 0)| (2, 1)| (2, 2)")
    print ("      |       |")
    print ("\n")

    Choice = input("Make your move! (enter: Row, Column): ")    # Player input for Row & Column as a string
    print ("\n")
    Row = int(Choice[0])    # Gets 1st value in string from user input & converts to integer
    Column = int(Choice[3]) # Gets 4th value in string from user input & converts to integer

    if(drawBoard[Row][Column] == "_"):  # Check if row & column is empty
        drawBoard[Row][Column] = Letter  
        Rounds += 1     # Increment each turn by +1 

    if(Count == 1):  # If player 1 ("O") has finished, go to player 2
            Count = 2
            Letter = "O"
    else:			# If player 2 ("X") has finished, go back to player 1
            Count = 1
            Letter = "X"
    for i in drawBoard: 	# For the integer values (row & column) in drawBoard
        print (i)   	# Print the board.
        print ("\n")    
