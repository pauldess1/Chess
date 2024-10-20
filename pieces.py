from utils import pos_to_move

BLACK = 'black'
WHITE = 'white'
PLAYERS = [WHITE, BLACK]

class Piece():
    def __init__(self, pos, color, board) -> None:
        self.pos = pos
        self.color = color
        self.board = board
        self.firstMove = True
    
    def first_move_change(self):
        if self.firstMove :
            self.firstMove = False

    def kill(self):
        self.board.alive_pieces.remove(self)
        
class Pawn(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)
        self.firstMove = True

    def is_valid_move(self, new_pos, board):
        move = pos_to_move(new_pos, self.pos)
        box = board.positions[new_pos[0]][new_pos[1]]

        if self.color == WHITE:
            move = (-move[0], move[1])

        if move == (2, 0) and self.firstMove and box is None:
            return True, False
        if move == (1, 0) and box is None:
            return True, False
        if move in [(1, -1), (1, 1)] and box is not None:
            return True, True
        return False, False
    
    def move(self, target_pos):
        valid, take = self.is_valid_move(target_pos, self.board)
        if valid :
            if take :
                self.board.positions[target_pos[0]][target_pos[1]].kill()
            self.pos = target_pos
            self.board.update()
            self.first_move_change()
            self.promotion()
            return True
        else :
            print("Not possible")
            return False

    def check_for_promotion(self):
        if self.pos[0] == 0 or self.pos[0] == 7:
            print(self.pos[0] == (0 or 7))
            return True
        else :
            return False

    def promotion(self):
        print("CA MARCHE PAS")
        if self.check_for_promotion():
            print("MAIS UN PEU QUAND MEME")
            pos, color = self.pos, self.color
            print("Executed")
            self.kill()
            self.board.alive_pieces.append(Queen(pos, color, self.board))
            self.board.update()
            return True
        else :
            return False
            
class King(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)

class Queen(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)

class Queen(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)

class Rook(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)

class Bishop(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)

class Knight(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)
