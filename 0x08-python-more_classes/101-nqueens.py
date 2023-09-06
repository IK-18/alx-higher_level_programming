#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Usage:
$ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format:
[[row, column], [row, column], [row, column], [row, column]]
each pair representing where a queen must be placed on the chessboard.
"""
import sys


def solve_n_queens(n):
    solutions = []
    chessboard = [["."] * n for _ in range(n)]

    def is_safe(row, col):
        for i in range(n):
            if chessboard[row][i] == "Q" or chessboard[i][col] == "Q":
                return False
        for i in range(n):
            for j in range(n):
                if abs(i - row) == abs(j - col) and chessboard[i][j] == "Q":
                    return False
        return True

    def place_queen(row):
        solution = []
        if row == n:
            for r in range(n):
                for c in range(n):
                    if chessboard[r][c] == "Q":
                        solution.append([r, c])
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(row, col):
                chessboard[row][col] = "Q"
                place_queen(row + 1)
                chessboard[row][col] = "."

    place_queen(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(int(sys.argv[1]))
    for solution in solutions:
        print(solution)
