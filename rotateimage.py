class Solution(object):
    def rotate(self, matrix):
        self.rotate_subset(matrix, 0, len(matrix) - 1)

    def rotate_subset(self, matrix, start, end):
        i = 0

        while i < end - start:
            self.shift(matrix, start, end)
            i += 1

        start += 1
        end -= 1

        # inner matrix exists
        if end - start >= 1:
            self.rotate_subset(matrix, start, end)

    def shift(self, matrix, start, end):
        row = start
        column = start
        pivot = matrix[row][column]
        previous_row = row
        previous_column = column

        moves = 0

        # go down array by default
        traverse_column = True
        step = 1

        # movements around a n*n dimensional array excluding pivot -> 4n - 6
        max_moves = ((end - start + 1) * 4) - 6
        while moves <= max_moves:

            # at bottom-left edge, traverse right
            if row == end and column == start:
                traverse_column = False
                step = 1

            # at bottom-right edge, traverse upwards
            if column == end and row == end:
                traverse_column = True
                step = -1

            # at top-right edge, traverse left
            if column == end and row == start:
                traverse_column = False
                step = -1

            if traverse_column:
                row += step
            else:
                column += step

            matrix[previous_row][previous_column] = matrix[row][column]
            previous_column = column
            previous_row = row

            moves += 1

        matrix[previous_row][previous_column] = pivot

    @staticmethod
    def print_matrix(matrix):
        i = 0
        while i < len(matrix):
            print matrix[i]
            i += 1
        print ""


test_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

solution = Solution()
solution.print_matrix(test_matrix)
solution.rotate(test_matrix)
solution.print_matrix(test_matrix)
