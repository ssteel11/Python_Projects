#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 21:57:45 2025

@author: ssteel
"""
import numpy as np
import pandas as pd

def draw_board():
    column_names =['A','B', 'C', 'D', 'E', 'F', 'G']
    row_names= ['6','5', '4','3','2','1']
    grid = np.zeros((6, 7))
    int_grid=grid.astype(int)
    # Convert to DataFrame
    df = pd.DataFrame(int_grid, columns=column_names, index=row_names)

    
    return print(df),df

def is_integer(s):
    try:
        int(s) <=6
        return True
    except ValueError:
        return False
def contains_column_name(value, df):
    return any(col in value for col in df.columns)

def update_board(board,row_choice, col_choice,first_player, turn):
    board.loc[row_choice,col_choice]=1