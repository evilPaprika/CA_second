import operator

moves = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
letter_to_index = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
index_to_letter = {v: k for k, v in letter_to_index.items()}


def find_knight_moves_to_pawn(knight_position, pawn_position):
    queue, visited = [knight_position], {knight_position: None}
    while queue:
        current_position = queue.pop(0)
        for move in moves:
            next_move = tuple(map(operator.add, current_position, move))
            if 0 < next_move[0] < 9 and 0 < next_move[1] < 9 and next_move not in visited:
                visited[next_move] = current_position
                queue.append(next_move)
            if next_move == pawn_position:
                result = []
                while next_move:
                    result.append(next_move)
                    next_move = visited[next_move]
                return result[::-1]


if __name__ == "__main__":
    path = find_knight_moves_to_pawn(
        *[tuple([letter_to_index[a[0]], int(a[1])])
          for a in open("in.txt").read().splitlines()])
    result = "\n".join([index_to_letter[move[0]] + str(move[1]) for move in path])
    # print(result)
    open("out.txt", "w").write(result)
