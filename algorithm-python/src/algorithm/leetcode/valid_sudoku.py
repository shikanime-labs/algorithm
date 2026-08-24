from collections import Counter
from functools import partial
from operator import itemgetter, ne


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (
            self.isValidSodukuByCounter(self.countByRows(board))
            and self.isValidSodukuByCounter(self.countByColumns(board))
            and self.isValidSodukuByCounter(self.countByBlocks(board))
        )

    def isValidSodukuByCounter(self, board):
        return not any(
            map(lambda counter: any(map(partial(ne, 1), counter.values())), board)
        )

    def countByRows(self, board):
        return map(
            lambda offset: Counter(
                filter(self.hasValue, map(partial(itemgetter(offset)), board))
            ),
            range(9),
        )

    def countByColumns(self, board):
        return map(lambda cells: Counter(filter(self.hasValue, cells)), board)

    def countByBlocks(self, board):
        for row_offset in range(0, 9, 3):
            for col_offset in range(0, 9, 3):
                yield Counter(
                    filter(
                        self.hasValue,
                        [
                            board[row_offset + j][col_offset + i]
                            for j in range(3)
                            for i in range(3)
                        ],
                    )
                )

    def hasValue(self, cell):
        return cell != "."
