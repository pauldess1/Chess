import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 135, 150)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

TAILLE_ECHIQUIER = 8
TAILLE_CASE = 60
TAILLE_FENETRE = TAILLE_CASE * TAILLE_ECHIQUIER

class Visualizer:
    def __init__(self, board, game):
        pygame.init()
        self.board = board
        self.game = game
        self.fenetre = pygame.display.set_mode((TAILLE_FENETRE, TAILLE_FENETRE + 200))
        pygame.display.set_caption("Chessboard")
        
        
        self.font = pygame.font.Font(None, 36)

        self.images = {
            'pawn_w': pygame.transform.scale(pygame.image.load('images/wp.png'), (TAILLE_CASE, TAILLE_CASE)),
            'rook_w': pygame.transform.scale(pygame.image.load('images/wR.png'), (TAILLE_CASE, TAILLE_CASE)),
            'knight_w': pygame.transform.scale(pygame.image.load('images/wN.png'), (TAILLE_CASE, TAILLE_CASE)),
            'bishop_w': pygame.transform.scale(pygame.image.load('images/wB.png'), (TAILLE_CASE, TAILLE_CASE)),
            'queen_w': pygame.transform.scale(pygame.image.load('images/wQ.png'), (TAILLE_CASE, TAILLE_CASE)),
            'king_w': pygame.transform.scale(pygame.image.load('images/wK.png'), (TAILLE_CASE, TAILLE_CASE)),
            'pawn_b': pygame.transform.scale(pygame.image.load('images/bp.png'), (TAILLE_CASE, TAILLE_CASE)),
            'rook_b': pygame.transform.scale(pygame.image.load('images/bR.png'), (TAILLE_CASE, TAILLE_CASE)),
            'knight_b': pygame.transform.scale(pygame.image.load('images/bN.png'), (TAILLE_CASE, TAILLE_CASE)),
            'bishop_b': pygame.transform.scale(pygame.image.load('images/bB.png'), (TAILLE_CASE, TAILLE_CASE)),
            'queen_b': pygame.transform.scale(pygame.image.load('images/bQ.png'), (TAILLE_CASE, TAILLE_CASE)),
            'king_b': pygame.transform.scale(pygame.image.load('images/bK.png'), (TAILLE_CASE, TAILLE_CASE)),
        }

    def draw_board(self):
        for x in range(TAILLE_ECHIQUIER):
            for y in range(TAILLE_ECHIQUIER):
                rect = pygame.Rect(y * TAILLE_CASE, x * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.fenetre, LIGHT_BROWN, rect)
                else:
                    pygame.draw.rect(self.fenetre, DARK_BROWN, rect)

    def draw_frame(self):
        frame_rect = pygame.Rect(0, 0, TAILLE_ECHIQUIER * TAILLE_CASE, TAILLE_ECHIQUIER * TAILLE_CASE)
        pygame.draw.rect(self.fenetre, BLACK, frame_rect, 5)

    def show_pieces(self):
        from board import Board, Pawn, Rook, Knight, Bishop, Queen, King
        for piece in self.board.alive_pieces:
            x, y = piece.pos
            piece_image = self.images[f"{piece.__class__.__name__.lower()}_{piece.color[0]}"]

            if self.game.selected_piece == piece:
                center_x = y * TAILLE_CASE + TAILLE_CASE // 2
                center_y = x * TAILLE_CASE + TAILLE_CASE // 2
                pygame.draw.circle(self.fenetre, GRAY, (center_x, center_y), TAILLE_CASE // 2)
                
            self.fenetre.blit(piece_image, (y * TAILLE_CASE, x * TAILLE_CASE))

    def display_current_player(self):
        current_player_text = f"{self.game.current_player}'s turn"
        text_surface = self.font.render(current_player_text, True, BLACK)
        self.fenetre.blit(text_surface, (10, TAILLE_ECHIQUIER * TAILLE_CASE + 10))

    def display_dead_pieces(self):
        white_dead = [piece for piece in self.board.dead_pieces if piece.color == 'white']
        black_dead = [piece for piece in self.board.dead_pieces if piece.color == 'black']

        for index, piece in enumerate(white_dead):
            piece_image = self.images[f"{piece.__class__.__name__.lower()}_w"]
            self.fenetre.blit(piece_image, (10 + index * (TAILLE_CASE + 5), TAILLE_ECHIQUIER * TAILLE_CASE + 60))

        for index, piece in enumerate(black_dead):
            piece_image = self.images[f"{piece.__class__.__name__.lower()}_b"]
            self.fenetre.blit(piece_image, (10 + index * (TAILLE_CASE + 5), 10))

    def update(self):
        self.fenetre.fill(GRAY)
        self.draw_frame()
        self.draw_board()
        self.show_pieces()
        self.display_current_player()
        self.display_dead_pieces()
        pygame.display.flip()
            
    def run(self, game):
        active = True
        while active:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    game.handle_click(pos)
                if event.type == pygame.QUIT:
                    active = False
            self.update()
        self.quit()
