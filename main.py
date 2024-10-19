from board import Board
from visual import Visualizer

if __name__ == "__main__":
    board = Board()  # Instancier le plateau
    visualizer = Visualizer(board)  # Passer le plateau au visualiseur
    visualizer.run()