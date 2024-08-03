#!/usr/bin/python3
"""
N-queen problem: This script solves the N-queen problem for any N >= 4.
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n):
    """
    Solve the N-queens problem using backtracking
    """
    if row >= n:
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n)
            board[row][col] = 0


def print_solution(board, n):
    """
    Print a solution
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)
