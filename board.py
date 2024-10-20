import pygame
from utils import pos_to_move
from visual import Visualizer, TAILLE_CASE
from pieces import *

BLACK = 'black'
WHITE = 'white'
PLAYERS = [WHITE, BLACK]

class Game():
    def __init__(self, board):
        self.board = board
        self.current_player = WHITE
        self.selected_piece = None

    def switch_turn(self):
        self.current_player = BLACK if self.current_player == WHITE else WHITE

    def is_current_player_piece(self, piece):
        return piece.color == self.current_player

    def handle_click(self, pos):
        x, y = pos[1] // TAILLE_CASE, pos[0] // TAILLE_CASE
        piece = self.board.positions[x][y]

        if self.selected_piece:
            target_position = (x, y)
            if self.selected_piece.move(target_position):
                self.switch_turn()
            self.selected_piece = None
        else:
            if piece and self.is_current_player_piece(piece):
                self.selected_piece = piece

class Board():
    def __init__(self) -> None:
        self.positions = [[None] * 8 for _ in range(8)]
        self.alive_pieces = []
        self.first_pos()
        self.player = WHITE
    
    def reset(self):
        self.empty_board()
        self.first_pos()

    def empty_board(self):
        self.positions = [[None] * 8 for _ in range(8)]

    def update(self):
        self.empty_board()
        for piece in self.alive_pieces :
            self.positions[piece.pos[0]][piece.pos[1]] = piece
        
    
    def first_pos(self):
        for i in range(8):
            self.alive_pieces.append(Pawn((1,i), BLACK, self))
            self.alive_pieces.append(Pawn((6,i), WHITE, self))
        
        self.alive_pieces.append(Rook((0,0), BLACK, self))
        self.alive_pieces.append(Rook((0,7), BLACK, self))
        self.alive_pieces.append(Rook((7,0), WHITE, self))
        self.alive_pieces.append(Rook((7,7), WHITE, self))

        self.alive_pieces.append(Knight((0,1), BLACK, self))
        self.alive_pieces.append(Knight((0,6), BLACK, self))
        self.alive_pieces.append(Knight((7,1), WHITE, self))
        self.alive_pieces.append(Knight((7,6), WHITE, self))

        self.alive_pieces.append(Bishop((0,2), BLACK, self))
        self.alive_pieces.append(Bishop((0,5), BLACK, self))
        self.alive_pieces.append(Bishop((7,2), WHITE, self))
        self.alive_pieces.append(Bishop((7,5), WHITE, self))

        self.alive_pieces.append(Queen((0,4), BLACK, self))
        self.alive_pieces.append(Queen((7,3), WHITE, self))

        self.alive_pieces.append(King((0,3), BLACK, self))
        self.alive_pieces.append(King((7,4), WHITE, self))

        self.update()
