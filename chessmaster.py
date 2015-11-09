#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chess"""


import time


class ChessPiece(object):
    """asdasdasdasdas"""
    def __init__(self, position):
        prefix = ''
        moves = []

    def algebraic_to_numeric(self, tile=''):
        x_table = 'abcdefgh'
        y_table = range(1,9)
        if (tile[0] in x_table) and (int(tile[1]) in y_table):
            x = x_table.index(tile[0])
            y = int(tile[1]) - 1
            return (x,y)
        else:
            return None
    def is_legal_move(self, position):
        if self.algebraic_to_numeric(position) is True:
            return True
        else:
            return False
        
    def move(self, position):
        if self.is_legal_move(position) is not None:
            oldposition = position
            newposition = position
            timestamp = time.time()
            tup = ((prefix + oldposition), (preifx + newposition), timestamp)
            self.moves.append(tup)
            return prefix
        else:
            False

class Rook(ChessPiece):
    prefix = 'R'
    pos = (0,0)
    def is_legal_move(self, position):
        if self.algebraic_to_numeric(position) is not None:
            current_p = position
            new_p = position
        else:
            return False

class Bishop(ChessPiece):
    prefix = 'B'
    pos = (1,0)
    def is_legal_move(self, position):
        if self.algebraic_to_numeric(position) is not None:
            current_p = position
            new_p = position
        else:
            return False
        
class King(ChessPiece):
    prefix = 'K'
    def is_legal_move(self, position):
        if self.algebraic_to_numeric(position) is not None:
            current_p = position
            new_p = position
        else:
            return False   


        
        
