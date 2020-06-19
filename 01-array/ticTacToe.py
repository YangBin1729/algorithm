"""二维数组及位置型游戏"""


class TicTacToe:
    def __init__(self):
        self._board = [[' '] * 3 for _ in range(3)]
        self._player = 'X'
    
    def mark(self, i, j):
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position accupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'
    
    def _is_win(self, mark):
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or mark ==
                board[1][0] == board[1][1] == board[1][2] or mark == board[2][
                    0] == board[2][1] == board[2][2] or mark == board[0][0] ==
                board[1][0] == board[2][0] or mark == board[0][1] == board[1][
                    1] == board[2][1] or mark == board[0][2] == board[1][2] ==
                board[2][2] or mark == board[0][0] == board[1][1] == board[2][
                    2] or mark == board[0][2] == board[1][1] == board[2][0])
    
    def winner(self):
        for mark in "XO":
            if self._is_win(mark):
                return mark
        return None
    
    def __str__(self):
        rows = ['   |   '.join(self._board[r]) for r in range(3)]
        return '\n------------------\n'.join(rows)


def test_3TGame():
    game = TicTacToe()
    game.mark(1, 1)
    game.mark(0, 2)
    game.mark(2, 2)
    game.mark(0, 0)
    game.mark(0, 1)
    game.mark(2, 1)
    game.mark(1, 2)
    game.mark(1, 0)
    game.mark(2, 0)
    
    print(game)
    winner = game.winner()
    if winner is None:
        print('Tie')
    else:
        print(winner, 'wins')


if __name__ == '__main__':
    test_3TGame()