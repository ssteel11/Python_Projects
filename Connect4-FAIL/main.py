#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 19:50:31 2025

@author: ssteel
"""
import numpy as np 
import pandas as pd
import math
from helpers import draw_board,is_integer,contains_column_name
import random
############################################################################
######################## Generating Connect Four Game#######################
############################################################################


#Generate a Matrix to express the possible slots of the Red and Blue Player 
#In Connect 4, 6 Rows and 7 columns. A 6 X 7 Matrix made up of ones will suffice

print("Lets play Connect Four")
print("Player 1 will use the Number 1(RED), and Player 2 will use the number 2 (BLUE).")

player_red=1
player_blue=2

players = ['Red', 'Blue']
first_player = random.choice(players)
print(f"{first_player} goes first!")
playing= True
complete=0
turn=0

if first_player=='Red':
    turn= 2*turn
    

board_tuple=draw_board()
board=board_tuple[1]

while playing:
    #Letting 
    if turn==0 and first_player=='Red':
        #Print Red goes First. Enter row number: ")
        row_choice='1'
        print("Enter column letter as depicted in board. ")
        col_choice=input()
        if is_integer(row_choice) and contains_column_name(col_choice, board):
            board.loc[row_choice,col_choice]=1
            print(board)
            turn+=1
        #Letting player decide to quit or not
        elif row_choice=='q' or col_choice=='q':
            playing==False
            
    elif turn==0 and first_player == 'Blue':
        #Print Blue is First
        print("Blue goes First. Enter row number.")
        row_choice='1'
        print("Enter column letter as depicted in board.")
        col_choice=input()
        if is_integer(row_choice) and contains_column_name(col_choice, board):
            board.loc[row_choice,col_choice]=2
            print(board)
        turn+=1
    elif turn % 2 !=0 and first_player=='Red' and turn < 8:
        print("Blues Turn. Enter row number.")
        row_choice=input()
        print("Enter column letter as depicted in board.")
        col_choice=input()
        if is_integer(row_choice) and contains_column_name(col_choice, board):
            board.loc[row_choice,col_choice]=2
            print(board)
        turn+=1
    else:
        #Print Red turn
        print("Blues Turn. Enter row number.")
        row_choice=input()
        print("Enter column letter as depicted in board. ")
        col_choice=input()
        if is_integer(row_choice) and contains_column_name(col_choice, board):
            board.loc[row_choice,col_choice]=1
            print(board)
            turn+=1
        #Letting player decide to quit or not
        elif row_choice=='q' or col_choice=='q':
            playing==False
        
        
        
        
        
        
        # if choice not in df
        # turn+=1
        
        