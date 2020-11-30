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

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def Pos_score (board, color):
    empty = 0
    playerscore = 0
    rivalscore = 0
    boardVal = [[200,-10,10,10,10,10,-10,200],
                [-10,-10,1 ,1 ,1 ,1 ,-10,-10],
                [10 , 1 ,1 ,1 ,1 ,1 , 1 , 10],
                [10 , 1 ,1 ,1 ,1 ,1 , 1 , 10],
                [10 , 1 ,1 ,1 ,1 ,1 , 1 , 10],
                [10 , 1 ,1 ,1 ,1 ,1 , 1 , 10],
                [-10,-10,1 ,1 ,1 ,1 ,-10,-10],
                [200,-10,10,10,10,10,-10,200]]
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j]==color):
                empty +=1
                playerscore += boardVal[i][j]
            elif board[i][j]!=color and (board[i][j]==1 or board[i][j==2]):
                empty += 1
                rivalscore += boardVal[i][j]
    return playerscore-rivalscore


def compute_utility(board, color):
    return 0


############ MINIMAX ###############################

def minimax_min_node(board, color, start):
    Nboard = board
    cur_score = math.inf
    moves = get_possible_moves(board,color)
    end = time.time()
    if (len(moves)==0 or end-start>4.9):
        player, opponent = get_score(board)
        return (-1,-1),Pos_score(board, color)
    else:
        for x in moves:
            Nboard= play_move(board, color, x[0],x[1])
            if(color==1):
                next_color=2
            else:
                next_color=1
            Nmove, Nscore = minimax_max_node(Nboard, next_color,start)
            if Nscore<cur_score:
                cur_score= Nscore
                best_move = x
       
        return best_move, cur_score


def minimax_max_node(board, color, start):
    Nboard = board
    cur_score = - math.inf
    moves = get_possible_moves(board,color)
    end= time.time()
    if (len(moves)==0 or end-start >4.9):
        return (-1,-1),Pos_score(board, color)
    else:
        for x in moves:
            Nboard= play_move(board, color, x[0],x[1])
            if(color==1):
                next_color=2
            else:
                next_color=1
            Nmove, Nscore = minimax_min_node(Nboard, next_color, start)
            if Nscore>cur_score:
                cur_score= Nscore
                best_move = x
        return best_move, cur_score

    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    start_time = time.time()
    move, score = minimax_max_node(board, color, start_time)
    i,j= move[0], move[1]
    return i,j
    

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