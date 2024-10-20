def pos_to_move(pos1, pos2):
    result = tuple(a - b for a, b in zip(pos1, pos2))
    return result
