from board import Board, Game
from visual import Visualizer

if __name__ == "__main__":
    board = Board()
    game = Game(board)
    visualizer = Visualizer(board, game)
    visualizer.run(game)