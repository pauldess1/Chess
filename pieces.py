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
    
    def possible_moves(self, board):
        moves = []
        x, y = self.pos
        for i in range(8):
            if i != x:
                new_pos = (i, y)
                if self.is_valid_move(new_pos, board):
                    moves.append(new_pos)
            if i != y:
                new_pos = (x, i)
                if self.is_valid_move(new_pos, board):
                    moves.append(new_pos)
        return moves
    
        
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
        if move in [(1, -1), (1, 1)] and (box is not None and box.color!=self.color):
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
            return True
        else :
            return False

    def promotion(self):
        if self.check_for_promotion():
            pos, color = self.pos, self.color
            self.kill()
            self.board.alive_pieces.append(Queen(pos, color, self.board))
            self.board.update()
            return True
        else :
            return False
            
class King(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)
        self.firstMove = True

    def is_valid_move(self, new_pos, board):
        move = pos_to_move(new_pos, self.pos)
        box = board.positions[new_pos[0]][new_pos[1]]

        if abs(move[0])<2 and abs(move[1])<2:
            if box is not None :
                if box.color != self.color :
                    return True, True
                else :
                    return False, False
            else :
                return True, False
        else :
            return False, False
                
    def move(self, target_pos):
        valid, take = self.is_valid_move(target_pos, self.board)
        if valid :
            if take :
                self.board.positions[target_pos[0]][target_pos[1]].kill()
            self.pos = target_pos
            self.board.update()
            self.first_move_change()
            return True
        else :
            print("Not possible")
            return False
        
class Queen(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)

    def is_valid_move(self, new_pos, board):
        move = pos_to_move(new_pos, self.pos)
        box = board.positions[new_pos[0]][new_pos[1]]

        if move[0] == 0:
            direction = 1 if move[1] > 0 else -1
            for y in range(self.pos[1] + direction, new_pos[1], direction):
                if board.positions[self.pos[0]][y] is not None:
                    return False, False
            return True, (box is not None and box.color!=self.color)

        elif move[1] == 0:
            direction = 1 if move[0] > 0 else -1
            for x in range(self.pos[0] + direction, new_pos[0], direction):
                if board.positions[x][self.pos[1]] is not None:
                    return False, False
            return True, (box is not None and box.color!=self.color)
        
        elif abs(move[0]) == abs(move[1]):
            direction_x = 1 if move[0] > 0 else -1
            direction_y = 1 if move[1] > 0 else -1
            x, y = self.pos
            for i in range(1, abs(move[0])):
                x += direction_x
                y += direction_y

                if board.positions[x][y] is not None:
                    return False, False 

            if box is not None :
                if box.color!=self.color :
                    return True, True
                else :
                    return False, False
            else :
                return True, False
        else:
            return False, False
    
    def move(self, target_pos):
        valid, take = self.is_valid_move(target_pos, self.board)
        if valid :
            if take :
                self.board.positions[target_pos[0]][target_pos[1]].kill()
            self.pos = target_pos
            self.board.update()
            return True
        else :
            print("Not possible")
            return False
    

class Rook(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)

    def is_valid_move(self, new_pos, board):
        move = pos_to_move(new_pos, self.pos)
        box = board.positions[new_pos[0]][new_pos[1]]

        if move[0] == 0:
            direction = 1 if move[1] > 0 else -1
            for y in range(self.pos[1] + direction, new_pos[1], direction):
                if board.positions[self.pos[0]][y] is not None:
                    return False, False
            return True, (box is not None and box.color!=self.color)

        elif move[1] == 0:
            direction = 1 if move[0] > 0 else -1
            for x in range(self.pos[0] + direction, new_pos[0], direction):
                if board.positions[x][self.pos[1]] is not None:
                    return False, False
            return True, (box is not None and box.color!=self.color)

        else:
            return False, False
        
    def move(self, target_pos):
        valid, take = self.is_valid_move(target_pos, self.board)
        if valid :
            if take :
                self.board.positions[target_pos[0]][target_pos[1]].kill()
            self.pos = target_pos
            self.board.update()
            return True
        else :
            print("Not possible")
            return False

class Bishop(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)

    def is_valid_move(self, new_pos, board):
        move = pos_to_move(new_pos, self.pos)
        box = board.positions[new_pos[0]][new_pos[1]]
        direction_x = 1 if move[0] > 0 else -1
        direction_y = 1 if move[1] > 0 else -1
        if abs(move[0]) == abs(move[1]):
            x, y = self.pos
            for i in range(1, abs(move[0])):
                x += direction_x
                y += direction_y

                if board.positions[x][y] is not None:
                    return False, False 

            if box is not None :
                if box.color!=self.color :
                    return True, True
                else :
                    return False, False
            else :
                return True, False
        else:
            return False, False
        
    def move(self, target_pos):
        valid, take = self.is_valid_move(target_pos, self.board)
        if valid :
            if take :
                self.board.positions[target_pos[0]][target_pos[1]].kill()
            self.pos = target_pos
            self.board.update()
            return True
        else :
            print("Not possible")
            return False

class Knight(Piece):
    def __init__(self, pos, color, board) -> None:
        super().__init__(pos, color, board)
    
    def is_valid_move(self, new_pos, board):
        move = pos_to_move(new_pos, self.pos)
        box = board.positions[new_pos[0]][new_pos[1]]

        if (abs(move[0])==2 and abs(move[1])==1) or (abs(move[0])==1 and abs(move[1])==2) :
            if box is not None:
                if box.color != self.color:
                    return True, True
                else :
                    return False, False
            else :
                return True, False
        else :
            return False, False
        
    def move(self, target_pos):
        valid, take = self.is_valid_move(target_pos, self.board)
        if valid :
            if take :
                self.board.positions[target_pos[0]][target_pos[1]].kill()
            self.pos = target_pos
            self.board.update()
            return True
        else :
            print("Not possible")
            return False
