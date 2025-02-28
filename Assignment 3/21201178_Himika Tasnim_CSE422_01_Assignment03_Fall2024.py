import random
import math

#Task-1
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []  

    def add_child(self, child):
        self.children.append(child)  


def game_tree_create(depth, branching_factor):
    if depth == 0:
        rand = random.choice([-1, 1])
        return Node(value=rand)
    root = Node()
    for i in range(branching_factor):
        child = game_tree_create(depth - 1, branching_factor)
        root.add_child(child)
    return root


def alpha_beta_pruning(node, depth, state, alpha, beta):
    if depth == 0:
        return node.value

    if state == "Max":
        value = -math.inf
        for child in node.children:
            child_value = alpha_beta_pruning(child, depth - 1, "Min", alpha, beta)  
            value = max(value, child_value)  
            node.value=value
            alpha = max(alpha, value)
            if alpha >= beta:
                break 
        return value
    
    else:
        value = math.inf
        for child in node.children:
            child_value = alpha_beta_pruning(child, depth - 1, "Max", alpha, beta) 
            value = min(value, child_value)  
            node.value=value
            beta = min(beta, value)
            if alpha >= beta:
                break  
        return value


def play_round(starting_player):
    max_depth = 5
    branching_factor = 2

    game_tree = game_tree_create(max_depth, branching_factor)

    state = "Max" 

    result = alpha_beta_pruning(game_tree, max_depth, state, -math.inf, math.inf)
    
    if starting_player==1:
        if  result == 1:
            winner = "Sub-Zero" 
        else:
            winner = "Scorpion"

    else: 
        if  result == 1:
            winner = "Scorpion"
        else:
            winner = "Sub-Zero"

    return winner


def MortaKombat(starting_player):
    total_rounds = 3  
    current_player = starting_player
    scorpion = 0
    sub_zero = 0

    winner_list = []

    for r in range(1, total_rounds + 1):
        winner = play_round(current_player)
        winner_list.append(winner)
        if winner == "Scorpion":
            scorpion += 1
        else:
            sub_zero += 1
        current_player = 1 - current_player

    final_winner = ""
    if scorpion > sub_zero:
        final_winner = "Scorpion" 
    else:
        final_winner = "Sub-Zero"

    print(f"Game Winner: {final_winner}")
    print("Total Rounds Played: 3")

    for w in range(len(winner_list)):
        print(f"Winner of Round {w + 1}: {winner_list[w]}")


starting_player = int(input())
MortaKombat(starting_player)




#Task-2
scores = [3, 6, 2, 3, 7, 1, 2, 0]
idx = 0

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def game_tree_create(depth, branching_factor):
    global scores, idx  
    if depth == 0:
        temp = scores[idx]
        idx += 1
        return Node(value=temp)
    root = Node() 
    for i in range(branching_factor):
        child = game_tree_create(depth - 1, branching_factor)
        root.add_child(child)
    return root


def play_normal(node, depth, state, alpha, beta):
    if depth == 0:
        return node.value

    if state == "Max":
        value = -math.inf
        for child in node.children:
            child_value = play_normal(child, depth - 1, "Min", alpha, beta)
            value = max(value, child_value)
            node.value=value
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = math.inf
        for child in node.children:
            child_value = play_normal(child, depth - 1, "Max", alpha, beta)
            value = min(value, child_value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


def play_magic(node, depth, alpha, beta):
    if depth == 0:
        return node.value

    value = -math.inf
    for child in node.children:
        child_value = play_magic(child, depth - 1, alpha, beta)
        value = max(value, child_value)
        node.value=value
        alpha = max(alpha, value)
        if beta <= alpha:
            break
    return value


def pacman_game(c):
    max_depth = 3
    branching_factor = 2

    game_tree = game_tree_create(max_depth, branching_factor)

    result_normal = play_normal(game_tree, max_depth, "Max", -math.inf, math.inf)
    result_magic = play_magic(game_tree, max_depth, -math.inf, math.inf)

    x=""
    if game_tree.children[0].value == result_magic:
        x = "left"
    else:
        x = "right"

    result_magic -= int(c)
    if result_magic > result_normal:
        print(f"The new minimax value is {result_magic}. Pacman goes {x} and uses dark magic")
    else:
        print(f"The minimax value is {result_normal}. Pacman does not use dark magic")


c = input()
pacman_game(c)


