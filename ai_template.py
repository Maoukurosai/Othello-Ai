#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
An AI player for Othello. This is the template file that you need to  
complete and submit for the competition. 

@author: YOUR NAME
"""

import random
import sys
import time
import math

#Weight for each board position
board_weights = [[50, 30, 29, 28, 28, 29, 30, 50],
                 [30, 25, 20, 15, 15, 20, 25, 30],
                 [29, 20, 15, 10, 10, 15, 20, 29],
                 [28, 15, 10,  5,  5, 10, 15, 28],
                 [28, 15, 10,  5,  5, 10, 15, 28],
                 [29, 20, 15, 10, 10, 15, 20, 29],
                 [30, 25, 20, 15, 15, 20, 25, 30],
                 [50, 30, 29, 28, 28, 29, 30, 50]]

#Depth of minimax search
DEPTH = 3

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    #Returns the score based on claimed positions
    #For now just uses weight on the board
    
    score = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == color:
                score += board_weight[i][j]
    return score


############ MINIMAX ###############################

def minimax_min_node(board, depth, color):
    #Returns next move in (i, j) tuple and the value of it
    cur_board = board
    cur_min = math.inf
    moves = get_possible_moves(board, color)
    if depth == 0 or len(moves) == 0:
        #Return the heuristic value of the current node
        return (-1, -1), compute_utility(board, color)
    for i in moves:
        cur_board = play_move(board, color, i[0], i[1])
        if color == 1:
            next_color = 2
        else:
            next_color = 1
        next_move, score = minimax_max_node(cur_board, depth - 1, next_color)
        if score < cur_min:
            cur_min = score
            best_move = i
    return best_move, cur_min


def minimax_max_node(board, depth, color):
    #Returns next move in (i, j) tuple and the value of it
    cur_board = board
    cur_max = -math.neginf
    moves = get_possible_moves(board, color)
    if depth == 0 or len(moves) == 0:
        #Return the heuristic value of the current node
        return (-1, -1), compute_utility(board, color)
    for i in moves:
        cur_board = play_move(board, color, i[0], i[1])
        if color == 1:
            next_color = 2
        else:
            next_color = 1
        next_move, score = minimax_min_node(cur_board, depth - 1, next_color)
        if score > cur_max:
            cur_max = score
            best_move = i
    return best_move, cur_max

    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    movei, movej = minimax_max_node(board, DEPTH, color)
    return movei, movej
    

def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_minimax(board, color)
           
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()