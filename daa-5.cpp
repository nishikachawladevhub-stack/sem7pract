
	// 8-Queens Problem using Backtracking
    
#include <iostream>
using namespace std;

#define N 8

int board[N][N] = {0};

// Check whether a Queen can be placed safely
bool isSafe(int row, int col) {

    // Check same column
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 1)
            return false;
    }

    // Check upper-left diagonal
    for (int i = row - 1, j = col - 1;
         i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1)
            return false;
    }

    // Check upper-right diagonal
    for (int i = row - 1, j = col + 1;
         i >= 0 && j < N; i--, j++) {
        if (board[i][j] == 1)
            return false;
    }

    return true;
}

// Solve using backtracking
bool solveNQueens(int row) {

    // All queens have been placed
    if (row == N)
        return true;

    // Try every column in the current row
    for (int col = 0; col < N; col++) {

        if (isSafe(row, col)) {

            // Place the Queen
            board[row][col] = 1;

            // Move to the next row
            if (solveNQueens(row + 1))
                return true;

            // Backtrack if placement fails
            board[row][col] = 0;
        }
    }

    return false;
}

int main() {

    // Place the first Queen at position (0, 0)
    board[0][0] = 1;

    cout << "First Queen placed at (0, 0).\n";

    // Place the remaining seven Queens
    if (solveNQueens(1)) {

        cout << "\nFinal 8-Queens Matrix:\n";

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }

    } else {
        cout << "No solution exists.";
    }

    return 0;
}








//python code 


// # 8 Queens Problem using Backtracking

// N = 8

// # Create an 8x8 chessboard
// board = [[0 for _ in range(N)] for _ in range(N)]

// # Check whether a Queen can be placed safely
// def is_safe(row, col):

//     # Check same column
//     for i in range(row):
//         if board[i][col] == 1:
//             return False

//     # Check upper-left diagonal
//     i, j = row - 1, col - 1

//     while i >= 0 and j >= 0:
//         if board[i][j] == 1:
//             return False
//         i -= 1
//         j -= 1

//     # Check upper-right diagonal
//     i, j = row - 1, col + 1

//     while i >= 0 and j < N:
//         if board[i][j] == 1:
//             return False
//         i -= 1
//         j += 1

//     return True


// # Solve using backtracking
// def solve_n_queens(row):

//     # All queens have been placed
//     if row == N:
//         return True

//     # Try every column in the current row
//     for col in range(N):

//         if is_safe(row, col):

//             # Place the Queen
//             board[row][col] = 1

//             # Move to the next row
//             if solve_n_queens(row + 1):
//                 return True

//             # Backtrack if placement fails
//             board[row][col] = 0

//     return False


// # Place the first Queen at position (0, 0)
// board[0][0] = 1

// print("First Queen placed at (0, 0).")

// # Place the remaining seven Queens
// if solve_n_queens(1):

//     print("\nFinal 8-Queens Matrix:")

//     for row in board:
//         print(*row)

// else:
//     print("No solution exists.")
