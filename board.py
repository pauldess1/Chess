from visual import TAILLE_CASE
from pieces import *

BLACK = 'black'
WHITE = 'white'
PLAYERS = [WHITE, BLACK]

class Game():
    def __init__(self, board):
        self.board = board
        self.current_player = WHITE
        self.selected_piece = None
        self.checkmate = False
        self.kings = {WHITE: None, BLACK: None}
        self.game_over = False

        for piece in self.board.alive_pieces:
            if isinstance(piece, King):
                self.kings[piece.color] = piece
        

    def switch_turn(self):
        self.current_player = BLACK if self.current_player == WHITE else WHITE

    def is_current_player_piece(self, piece):
        return piece.color == self.current_player
    
    def process_move(self, target_position):
        if not self.selected_piece:
            print("No piece selected.")
            return

        valid, take = self.selected_piece.is_valid_move(target_position, self.board)

        if valid:
            if self.simulate_move(self.selected_piece, target_position):
                if self.selected_piece.move(target_position):
                    self.check_for_check_and_checkmate()
                    self.switch_turn()
                else:
                    print("Move execution failed. Try again.")
            else:
                print("This move would put your king in check. Invalid move.")
        else:
            print("Not a valid move according to the piece's rules.")
        self.selected_piece = None

    def handle_click(self, pos):
        """Handle player's click to select or move a piece, but only if the game is not over."""
        if self.game_over:
            print("Game is over. Please reset the game.")
            return

        x, y = pos[1] // TAILLE_CASE, pos[0] // TAILLE_CASE
        piece = self.board.positions[x][y]

        if self.selected_piece:
            self.process_move((x, y))
        else:
            if piece and self.is_current_player_piece(piece):
                self.selected_piece = piece
    
    def simulate_move(self, piece, target_pos):
        original_pos = piece.pos
        target_piece = next((p for p in self.board.alive_pieces if p.pos == target_pos), None)
        piece.pos = target_pos

        if target_piece:
            self.board.alive_pieces.remove(target_piece)

        self.board.update()

        king = self.kings[piece.color]
        in_check = self.is_in_check(king)

        piece.pos = original_pos
        if target_piece:
            self.board.alive_pieces.append(target_piece)
        self.board.update()

        return not in_check
    
    def is_in_check(self, king):
        enemy_pieces = self.board.get_enemy_pieces(king.color)
        for piece in enemy_pieces:
            if piece.is_valid_move(king.pos, self.board) == (True, True):
                return True
        return False
    
    def is_checkmate(self, king):
        if not self.is_in_check(king):
            return False

        player_pieces = [piece for piece in self.board.alive_pieces if piece.color == king.color]

        for piece in player_pieces:
            for move in piece.possible_moves(self.board):
                if self.simulate_move(piece, move):
                    return False
        return True
    
    def check_for_check_and_checkmate(self):
        king = self.kings[self.get_other_player()]
        if self.is_in_check(king):
            if self.is_checkmate(king):
                print(f"Checkmate! {self.get_other_player()} loses.")
                self.game_over = True
            else:
                print("Check!")
    
    def get_other_player(self):
        return BLACK if self.current_player == WHITE else WHITE

    def reset_game(self):
        self.board.reset()
        self.current_player = WHITE
        self.selected_piece = None
        self.checkmate = False
        self.game_over = False

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
        
    def get_enemy_pieces(self, player_color):
        return [piece for piece in self.alive_pieces if piece.color != player_color]
    
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