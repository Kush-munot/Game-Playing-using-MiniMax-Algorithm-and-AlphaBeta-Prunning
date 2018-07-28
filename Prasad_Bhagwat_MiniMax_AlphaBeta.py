import copy
import sys

# Used for mapping the positions of Star & Circle pieces
row_alphabets = 'HGFEDCBA'

# Class definition for a Node
class node():
    def __init__(self, curr_state, pos_of_S, pos_of_C, player, next_move, eval_value, curr_depth):
        self.curr_state = copy.deepcopy(curr_state)
        self.player = player
        self.curr_depth = curr_depth
        self.eval_value = eval_value
        self.children = []
        self.next_move = None
        self.pos_of_S = copy.deepcopy(pos_of_S)
        self.pos_of_C = copy.deepcopy(pos_of_C)

# Return opponent for given input player
def ret_opponent(player1):
    player2 = 'Circle' if player1 == 'Star' else 'Star'
    return player2,

# Sort positions of list in given preference
def sort_positions(pos_list):
    moves = []
    for pos in pos_list:
        gen_tuple = list(pos)
        moves.append((gen_tuple[0], gen_tuple[1]))
    moves.sort(key=lambda k: (k[0], -int(k[1])), reverse=True)
    new_moves = []
    for (x,y) in moves:
        new_moves.append(x + y)
    return new_moves

# Map input board state to positions of Star & Circle
def mapboard(curr_node):
    for row in range(8):
        for column in range(8):
            position = curr_node.curr_state[row][column]
            if position.startswith('S'):
                for i in range(int(position[1])):
                    curr_node.pos_of_S.append(row_alphabets[row] + str(column + 1))
            elif position.startswith('C'):
                for i in range(int(position[1])):
                    curr_node.pos_of_C.append(row_alphabets[row] + str(column + 1))

# Valid moves for given node state
def valid_moves(curr_node):
    global star_pass, circle_pass, terminate, num_nodes, algorithm
    # For Star getting valid moves
    if (curr_node.player == 'Star'):
        for pos in curr_node.pos_of_S:
            if not (pos.startswith('H')):
                move_row = chr(ord(pos[0]) + 1)
                jump_row = chr(ord(pos[0]) + 2)
                right_move_col = int(pos[1]) + 1
                left_move_col = int(pos[1]) - 1
                right_jump_col = int(pos[1]) + 2
                left_jump_col = int(pos[1]) - 2

                left_jump_path_circle = move_row + str(left_move_col)
                left_jump_move = jump_row + str(left_jump_col)
                if left_jump_path_circle in curr_node.pos_of_C and left_jump_col > 0 and \
                        left_jump_move not in curr_node.pos_of_C and jump_row <= "H" and \
                        (left_jump_move not in curr_node.pos_of_S or jump_row == "H"):
                    new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C,
                                    ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
                    new_node.pos_of_C.remove(left_jump_path_circle)
                    new_node.pos_of_S.remove(pos)
                    new_node.pos_of_S.append(left_jump_move)
                    new_node.pos_of_S = sort_positions(new_node.pos_of_S)
                    curr_node.children.append(new_node)
                    new_node.next_move = pos + '-' + left_jump_move
                    if start_player == 'Star' and algorithm == 'ALPHABETA':
                        new_node.eval_value = -float('inf')
                    else:
                        new_node.eval_value = float('inf')

                right_jump_path_circle = move_row + str(right_move_col)
                right_jump_move = jump_row + str(right_jump_col)
                if right_jump_path_circle in curr_node.pos_of_C and right_jump_col < 9 and \
                        right_jump_move not in curr_node.pos_of_C and jump_row <= "H" and \
                        (right_jump_move not in curr_node.pos_of_S or jump_row == "H"):
                    new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C,
                                    ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
                    new_node.pos_of_C.remove(right_jump_path_circle)
                    new_node.pos_of_S.remove(pos)
                    new_node.pos_of_S.append(right_jump_move)
                    new_node.pos_of_S = sort_positions(new_node.pos_of_S)
                    curr_node.children.append(new_node)
                    new_node.next_move = pos + '-' + right_jump_move
                    if start_player == 'Star' and algorithm == 'ALPHABETA':
                        new_node.eval_value = -float('inf')
                    else:
                        new_node.eval_value = float('inf')

                left_move = move_row + str(left_move_col)
                if left_move_col > 0 and left_move not in curr_node.pos_of_C and (
                        left_move not in curr_node.pos_of_S or left_move in curr_node.pos_of_S and move_row == "H"):
                    new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C,
                                    ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
                    new_node.pos_of_S.remove(pos)
                    new_node.pos_of_S.append(left_move)
                    new_node.pos_of_S = sort_positions(new_node.pos_of_S)
                    curr_node.children.append(new_node)
                    new_node.next_move = pos + '-' + left_move
                    if start_player == 'Star' and algorithm == 'ALPHABETA':
                        new_node.eval_value = -float('inf')
                    else:
                        new_node.eval_value = float('inf')

                right_move = move_row + str(right_move_col)
                if right_move_col < 9 and right_move not in curr_node.pos_of_C and (
                        right_move not in curr_node.pos_of_S or right_move in curr_node.pos_of_S and move_row == "H"):
                    new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C,
                                    ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
                    new_node.pos_of_S.remove(pos)
                    new_node.pos_of_S.append(right_move)
                    new_node.pos_of_S = sort_positions(new_node.pos_of_S)
                    curr_node.children.append(new_node)
                    new_node.next_move = pos + '-' + right_move
                    if start_player == 'Star' and algorithm == 'ALPHABETA':
                        new_node.eval_value = -float('inf')
                    else:
                        new_node.eval_value = float('inf')

        if (bool(curr_node.children) == False) and (bool(curr_node.pos_of_S) == True):
            # print curr_node.pos_of_S, curr_node.pos_of_C
            # print "Adding pass for star",curr_node.next_move
            new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C,
                            ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
            curr_node.children.append(new_node)
            new_node.next_move = 'pass'
    # For Circle getting valid moves        
    else:
        for pos in curr_node.pos_of_C:
            if not (pos.startswith('A')):
                move_row = chr(ord(pos[0]) - 1)
                jump_row = chr(ord(pos[0]) - 2)
                right_move_col = int(pos[1]) + 1
                left_move_col = int(pos[1]) - 1
                right_jump_col = int(pos[1]) + 2
                left_jump_col = int(pos[1]) - 2

                left_move = move_row + str(left_move_col)
                if left_move_col > 0 and left_move not in curr_node.pos_of_S and (
                        left_move not in curr_node.pos_of_C or left_move in curr_node.pos_of_C and move_row == "A"):
                    new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C, \
                                    ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
                    new_node.pos_of_C.remove(pos)
                    new_node.pos_of_C.append(left_move)
                    new_node.pos_of_C = sort_positions(new_node.pos_of_C)
                    curr_node.children.append(new_node)
                    new_node.next_move = pos + '-' + left_move
                    if start_player == 'Circle' and algorithm == 'ALPHABETA':
                        new_node.eval_value = -float('inf')
                    else:
                        new_node.eval_value = float('inf')

                right_move = move_row + str(right_move_col)
                if right_move_col < 9 and right_move not in curr_node.pos_of_S and (
                        right_move not in curr_node.pos_of_C or right_move in curr_node.pos_of_C and move_row == "A"):
                    new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C,
                                    ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
                    new_node.pos_of_C.remove(pos)
                    new_node.pos_of_C.append(right_move)
                    new_node.pos_of_C = sort_positions(new_node.pos_of_C)
                    curr_node.children.append(new_node)
                    new_node.next_move = pos + '-' + right_move
                    if start_player == 'Circle' and algorithm == 'ALPHABETA':
                        new_node.eval_value = -float('inf')
                    else:
                        new_node.eval_value = float('inf')

                left_jump_path_star = move_row + str(left_move_col)
                left_jump_move = jump_row + str(left_jump_col)
                if left_jump_path_star in curr_node.pos_of_S and left_jump_col > 0 and \
                        left_jump_move not in curr_node.pos_of_S and jump_row >= "A" and \
                        (left_jump_move not in curr_node.pos_of_C or jump_row == "A"):
                    new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C,
                                    ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
                    new_node.pos_of_S.remove(left_jump_path_star)
                    new_node.pos_of_C.remove(pos)
                    new_node.pos_of_C.append(left_jump_move)
                    new_node.pos_of_C = sort_positions(new_node.pos_of_C)
                    curr_node.children.append(new_node)
                    new_node.next_move = pos + '-' + left_jump_move
                    if start_player == 'Circle' and algorithm == 'ALPHABETA':
                        new_node.eval_value = -float('inf')
                    else:
                        new_node.eval_value = float('inf')

                right_jump_path_star = move_row + str(right_move_col)
                right_jump_move = jump_row + str(right_jump_col)
                if right_jump_path_star in curr_node.pos_of_S and right_jump_col < 9 and \
                        right_jump_move not in curr_node.pos_of_S and jump_row >= "A" and \
                        (right_jump_move not in curr_node.pos_of_C or jump_row == "A"):
                    new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C,
                                    ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
                    new_node.pos_of_S.remove(right_jump_path_star)
                    new_node.pos_of_C.remove(pos)
                    new_node.pos_of_C.append(right_jump_move)
                    new_node.pos_of_C = sort_positions(new_node.pos_of_C)
                    curr_node.children.append(new_node)
                    new_node.next_move = pos + '-' + right_jump_move
                    if start_player == 'Circle' and algorithm == 'ALPHABETA':
                        new_node.eval_value = -float('inf')
                    else:
                        new_node.eval_value = float('inf')

        if (bool(curr_node.children) == False) and (bool(curr_node.pos_of_S) == True):
            # print "Adding pass for circle"
            # print curr_node.pos_of_S, curr_node.pos_of_C
            new_node = node(curr_node.curr_state, curr_node.pos_of_S, curr_node.pos_of_C,
                            ret_opponent(curr_node.player), None, 0, curr_node.curr_depth + 1)
            curr_node.children.append(new_node)
            new_node.next_move = 'pass'

# Return whether current node is leaf node in the game tree
def is_leaf_state(curr_node):
    global terminate, star_pass, circle_pass
    return (bool(curr_node.pos_of_S) == False) or curr_node.curr_depth == max_depth or \
           (bool(curr_node.pos_of_C) == False)

# Maximizing function for both Alpha-Beta & Minimax algorithm
def max_calc(curr_node, is_parent_pass, alpha, beta):
    global algorithm, num_nodes
    num_nodes += 1
    pass_move = False
    if is_leaf_state(curr_node):
        return util_func(curr_node)
    max_val = -float('inf')
    valid_moves(curr_node)
    
    for move in curr_node.children:
        if move.next_move == 'pass':
            pass_move = True
            #print "pass"

    if pass_move and is_parent_pass:
        num_nodes += 1
        return util_func(curr_node)

    for move in curr_node.children:
        max_val = max(max_val, min_calc(move, pass_move, alpha, beta))
        curr_node.eval_value = max_val
        alpha = max(alpha, max_val)
        if algorithm == "ALPHABETA" and alpha >= beta:
            return max_val
    return max_val

# Minimizing function for both Alpha-Beta & Minimax algorithm
def min_calc(curr_node, is_parent_pass, alpha, beta):
    global algorithm, num_nodes
    num_nodes += 1
    pass_move = False
    if is_leaf_state(curr_node):
        return util_func(curr_node)
    min_val = float('inf')
    valid_moves(curr_node)

    for move in curr_node.children:
        if move.next_move == 'pass':
            pass_move = True
            #print "pass"

    if pass_move and is_parent_pass:
        num_nodes += 1
        return util_func(curr_node)

    for move in curr_node.children:
        min_val = min(min_val, max_calc(move, pass_move, alpha, beta))
        curr_node.eval_value = min_val
        beta = min(beta, min_val)
        if algorithm == "ALPHABETA" and alpha >= beta:
            return min_val
    return min_val

# Return utility value for board state
def util_func(curr_node):
    global start_player
    sum_star_weights, sum_circle_weights = 0, 0
    for pos in curr_node.pos_of_S:
        sum_star_weights += star_weights[row_alphabets.index(pos[0])]
    for pos in curr_node.pos_of_C:
        sum_circle_weights += circle_weights[row_alphabets.index(pos[0])]

    if start_player == 'Star':
        return sum_star_weights - sum_circle_weights
    else:
        return sum_circle_weights - sum_star_weights

# Reading file and variable assignment
def read_file():
    global max_depth, star_weights, circle_weights, board_map, num_nodes
    num_rows = 0
    num_cols = 0
    board_state = [['.' for x in range(8)] for y in range(8)]
    board_rows = ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

    with open("input.txt", "r") as f:
        data = f.read().strip().split('\n')
        player = data[0]                                        # Player
        algorithm = data[1]                                     # Algorithm to use
        max_depth = int(data[2])                                # Maximum depth of game tree
        for num_lines in data[3:11]:
            num_cols = 0
            for character in num_lines.split(","):
                board_state[num_rows][num_cols] = str(character)    # Board state
                num_cols += 1
            num_rows += 1
        star_weights = [int(x) for x in data[11].strip().split(",")]
        circle_weights = star_weights[:]
        star_weights = circle_weights[::-1]

        board_map = dict(zip(board_rows, board_state))

    return player, algorithm, board_state

# Writing results to file
def write_file(next_move, next_move_util, final_util):
    global num_nodes
    with open("output.txt", "w") as f:
        f.write(next_move)
        f.write("\n")
        f.write(str(next_move_util))
        f.write("\n")
        f.write(str(final_util))
        f.write("\n")
        f.write(str(num_nodes))

# Main function
def main():
    global start_player, num_nodes, star_pass, circle_pass, terminate, algorithm
    player, algorithm, root_state = read_file()
    start_player = player
    star_pass, circle_pass, terminate = 0, 0, 0

    root = node(root_state, [], [], player, None, 0, 0)         # Creating root node of game tree    
    num_nodes = 0
    mapboard(root)
    # print root.pos_of_S, root.pos_of_C
    # print root.player, root.children, root.curr_state, root.curr_depth
    final_util = max_calc(root, False, -float('inf'), float('inf'))      # Algorithm call

    if not root.children:                                                # If no childrent for root i.e. Input board is not valid game
        with open("output.txt", "w") as f:
            sys.exit(0)
    else:
        #print "Final Util", final_util
        for child in root.children:
            #print "Child Move", child.next_move, "Score", child.eval_value
            if (child.next_move == 'pass') or (child.eval_value in [-float('inf'), float("inf")]):
                child.eval_value = final_util
            if child.eval_value == final_util:
                next_move_util = util_func(child)
                next_move = child.next_move
                break
        write_file(next_move, next_move_util, final_util)

# Entry point of the program
if __name__ == '__main__':
    main()