from Position import Position
class Board:
    def __init__(self):
        self.side_to_move = Position.WHITE.value
        self.pieces = {
            Position.WHITE.value: [0] * 6,
            Position.BLACK.value: [0] * 6
        }
        for (color, piece), pos in Position.STARTING_POSITION.value.items():
            self.pieces[color][piece] = pos
    def get_legal_moves(self, piece):
        