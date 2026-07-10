from enum import Enum
class Position(Enum):
    WHITE = 0
    BLACK = 1
    
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5
    
    PIECE_SYMBOLS = {
        (WHITE, PAWN): "WP",
        (WHITE, KNIGHT): "WK",
        (WHITE, BISHOP): "WB",
        (WHITE, ROOK): "WR",
        (WHITE, QUEEN): "WQ",
        (WHITE, KING): "WK",
        (BLACK, PAWN): "BP",
        (BLACK, KNIGHT): "BK",
        (BLACK, BISHOP): "BB",
        (BLACK, ROOK): "BR",
        (BLACK, QUEEN): "BQ",
        (BLACK, KING): "BK"
    }
    
    WHITE_PAWNS = (
        1 << 8,
        1 << 9,
        1 << 10,
        1 << 11,
        1 << 12,
        1 << 13,
        1 << 14,
        1 << 15
    )
    WHITE_ROOKS = (
        1 << 0,
        1 << 7
    )
    WHITE_KNIGHTS = (
        1 << 1,
        1 << 6
    )
    WHITE_BISHOPS = (
        1 << 2,
        1 << 5
    )
    WHITE_KING = 1 << 4
    WHITE_QUEEN = 1 << 3
    
    BLACK_PAWNS = (
        1 << 48,
        1 << 49,
        1 << 50,
        1 << 51,
        1 << 52,
        1 << 53,
        1 << 54,
        1 << 55
    )
    BLACK_ROOKS = (
        1 << 56,
        1 << 63
    )
    BLACK_KNIGHTS = (
        1 << 57,
        1 << 62
    )
    BLACK_BISHOPS = (
        1 << 58,
        1 << 61
    )
    BLACK_KING = 1 << 60
    BLACK_QUEEN = 1 << 59
    
    STARTING_POSITION = {
        (WHITE, PAWN): WHITE_PAWNS,
        (WHITE, KNIGHT): WHITE_KNIGHTS,
        (WHITE, BISHOP): WHITE_BISHOPS,
        (WHITE, ROOK): WHITE_ROOKS,
        (WHITE, QUEEN): WHITE_QUEEN,
        (WHITE, KING): WHITE_KING,
        (BLACK, PAWN): BLACK_PAWNS,
        (BLACK, KNIGHT): BLACK_KNIGHTS,
        (BLACK, BISHOP): BLACK_BISHOPS,
        (BLACK, ROOK): BLACK_ROOKS,
        (BLACK, QUEEN): BLACK_QUEEN,
        (BLACK, KING): BLACK_KING
    }
    