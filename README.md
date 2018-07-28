Game Playing using MiniMax Algorithm and Alpha-Beta prunning
==========================================================

### Enviroment versions required:
Python: 2.7 

### Algorithm approach:
Implementing the Minimax Algorithm and Alpha-Beta Prunning to determine the depth-bounded minimax values of given game positions. The program takes the input from the file “input.txt” and prints out its output to the file “output.txt”. Each input file contains a game position (including the board state and the player to move), a search cut-off depth D , the values of board rows and the name of the algorithm to be used (Minimax or Alpha-Beta). The program outputs the corresponding information after running the specified search algorithm to depth D. That is, the leaf nodes of the corresponding game tree should be either a game position after exactly D moves (alternating between Star and Circle) or an end-game position after no more than D moves.
