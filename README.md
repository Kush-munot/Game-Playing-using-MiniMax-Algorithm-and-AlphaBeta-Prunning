Game Playing using MiniMax Algorithm and Alpha-Beta prunning
==========================================================

### Enviroment versions required:
Python: 2.7 

### Algorithm approach:
Implementing the Minimax Algorithm and Alpha-Beta Prunning to determine the depth-bounded minimax values of given game positions. The program takes the input from the file “input.txt” and prints out its output to the file “output.txt”. Each input file contains a game position (including the board state and the player to move), a search cut-off depth D , the values of board rows and the name of the algorithm to be used (Minimax or Alpha-Beta). The program outputs the corresponding information after running the specified search algorithm to depth D. That is, the leaf nodes of the corresponding game tree should be either a game position after exactly D moves (alternating between Star and Circle) or an end-game position after no more than D moves.

### Python command for executing DPLL Algorithm

* * *

Exceuting MiniMax Algorithm and Alpha-Beta prunning using _“Prasad\_Bhagwat\_MiniMax_AlphaBeta.py”_ file

    python Prasad_Bhagwat_DPLL.py <input file path>
    

where,  
_1. 'input file path'_ corresponds to the absolute path of input file  

Example usage of the above command is as follows:

     ~/Desktop Prasad_Bhagwat_MiniMax_AlphaBeta.py /home/prasad/workspace/input.txt
    

Note : _Output file_ named _‘output.txt’_ is generated at the location from where the program is run.


### Input file format:
_PLAYER:_​ The player to choose “Star” or “Circle”.  
_ALGORITHM:_​ Algorithm to use, which will either be “MINIMAX” or “ALPHABETA” and determines the algorithm that you must use to come up with next move  
_DEPTH LIMIT:_​ Depth of tree, which is a number up to 10 and determines the maximum depth of your minimax or alpha/beta pruning tree  
_CURRENT BOARD STATE:_​ Contains 8 lines where each line includes 8 square indicators separated by a comma “,”. These 8 lines represent the rows of the board from H to A. A square indicator could be “S{i}”, “C{i}”, or “0” where {i} indicates the number of pieces (Star or Circle) at that square, and “0” indicates that no pieces are on that square. Note that only squares of row H (for Star) and row A (for Circle) can have more than one Star or Circle piece, respectively. The initial board state will contain at least one piece for each player. Further, the initial board state may not necessarily happen as a result of playing a game from the beginning.  
_ROW VALUES:_​ Contains one line including 8 increasing numbers separated by a comma “,’. This line indicates the values of rows A to H for player Star and the values of rows H to A for player Circle.  
