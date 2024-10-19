import pygame

BLACK = 'black'
WHITE = 'white'

class Piece():
    def __init__(self, pos, color) -> None:
        self.pos = pos
        self.color = color
    
class Pawn(Piece):
    def __init__(self, pos, color) -> None:
        super().__init__(pos, color)

    def is_valid_move(self, new_pos, board):
        print("On y est")
        valid = True
        if new_pos[1] == self.pos[1]:
            if new_pos[0] == new_pos[0]+1 and board.positions[new_pos[0]][new_pos[1]] == None:
                print('OK')
        elif abs(new_pos[1]-self.pos[1]) == 1:
            if new_pos[0] == new_pos[0]+1 and board.positions[new_pos[0]][new_pos[1]] != None:
                print('OK')

        else :
            print('NON OK')


class King(Piece):
    def __init__(self, pos, color) -> None:
        super().__init__(pos, color)

class Queen(Piece):
    def __init__(self, pos, color) -> None:
        super().__init__(pos, color)

class Queen(Piece):
    def __init__(self, pos, color) -> None:
        super().__init__(pos, color)

class Rook(Piece):
    def __init__(self, pos, color) -> None:
        super().__init__(pos, color)

class Bishop(Piece):
    def __init__(self, pos, color) -> None:
        super().__init__(pos, color)

class Knight(Piece):
    def __init__(self, pos, color) -> None:
        super().__init__(pos, color)

class Board():
    def __init__(self) -> None:
        self.positions = [[None] * 8 for _ in range(8)]
        self.alive_pieces = []
        self.first_pos()

    def update(self):
        for piece in self.alive_pieces :
            self.positions[piece.pos[0]][piece.pos[1]] = piece
    
    def first_pos(self):
        for i in range(8):
            self.alive_pieces.append(Pawn((1,i), BLACK))
            self.alive_pieces.append(Pawn((6,i), WHITE))
        
        self.alive_pieces.append(Rook((0,0), BLACK))
        self.alive_pieces.append(Rook((0,7), BLACK))
        self.alive_pieces.append(Rook((7,0), WHITE))
        self.alive_pieces.append(Rook((7,7), WHITE))

        self.alive_pieces.append(Knight((0,1), BLACK))
        self.alive_pieces.append(Knight((0,6), BLACK))
        self.alive_pieces.append(Knight((7,1), WHITE))
        self.alive_pieces.append(Knight((7,6), WHITE))

        self.alive_pieces.append(Bishop((0,2), BLACK))
        self.alive_pieces.append(Bishop((0,5), BLACK))
        self.alive_pieces.append(Bishop((7,2), WHITE))
        self.alive_pieces.append(Bishop((7,5), WHITE))

        self.alive_pieces.append(Queen((0,4), BLACK))
        self.alive_pieces.append(Queen((7,3), WHITE))

        self.alive_pieces.append(King((0,3), BLACK))
        self.alive_pieces.append(King((7,4), WHITE))

        self.update()
