import pygame

# Constantes pour les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 135, 150)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

# Dimensions
TAILLE_ECHIQUIER = 8
TAILLE_CASE = 60
TAILLE_FENETRE = TAILLE_CASE * TAILLE_ECHIQUIER

class Visualizer:
    def __init__(self, board, game):
        pygame.init()
        self.board = board
        self.game = game
        self.fenetre = pygame.display.set_mode((TAILLE_FENETRE, TAILLE_FENETRE))
        pygame.display.set_caption("Chessboard")
        
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
                rect = pygame.Rect(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.fenetre, LIGHT_BROWN, rect)
                else:
                    pygame.draw.rect(self.fenetre, DARK_BROWN, rect)

    def show_pieces(self):
        from board import Board, Pawn, Rook, Knight, Bishop, Queen, King
        for piece in self.board.alive_pieces:
            x, y = piece.pos
            piece_image = None
            if piece.color == 'white':
                if isinstance(piece, Pawn):
                    piece_image = self.images['pawn_w']
                elif isinstance(piece, Rook):
                    piece_image = self.images['rook_w']
                elif isinstance(piece, Knight):
                    piece_image = self.images['knight_w']
                elif isinstance(piece, Bishop):
                    piece_image = self.images['bishop_w']
                elif isinstance(piece, Queen):
                    piece_image = self.images['queen_w']
                elif isinstance(piece, King):
                    piece_image = self.images['king_w']
            else:
                if isinstance(piece, Pawn):
                    piece_image = self.images['pawn_b']
                elif isinstance(piece, Rook):
                    piece_image = self.images['rook_b']
                elif isinstance(piece, Knight):
                    piece_image = self.images['knight_b']
                elif isinstance(piece, Bishop):
                    piece_image = self.images['bishop_b']
                elif isinstance(piece, Queen):
                    piece_image = self.images['queen_b']
                elif isinstance(piece, King):
                    piece_image = self.images['king_b']

            if self.game.selected_piece == piece:
                center_x = y * TAILLE_CASE + TAILLE_CASE // 2
                center_y = x * TAILLE_CASE + TAILLE_CASE // 2
                pygame.draw.circle(self.fenetre, GRAY, (center_x, center_y), TAILLE_CASE // 2)
            self.fenetre.blit(piece_image, (y * TAILLE_CASE, x * TAILLE_CASE))

    def update(self):
        self.fenetre.fill(GRAY)
        self.draw_board()
        self.show_pieces()
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
