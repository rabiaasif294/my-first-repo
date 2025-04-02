import math

# Initialize a 3x3 Tic-Tac-Toe board with empty spaces.
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def is_winner(board, player):
    """Checks if the given player has won."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:  # Check rows
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:  # Check columns
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def is_full(board):
    """Returns True if the board is full, otherwise False."""
    for row in board:
        if ' ' in row:
            return False
    return True


def minimax(board, depth, is_maximizing, alpha, beta):
    """
    Minimax algorithm with Alpha-Beta Pruning to evaluate board positions.
    Alpha tracks the best score for the maximizer (AI).
    Beta tracks the best score for the minimizer (Human).
    """
    # Base cases: Check for a terminal state (win, loss, draw)
    if is_winner(board, 'O'):  # AI wins
        return 10 - depth
    if is_winner(board, 'X'):  # Human wins
        return depth - 10
    if is_full(board):  # Draw
        return 0

    # Maximizing player's turn (AI)
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # AI makes a move
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '  # Undo the move
                    best_score = max(best_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:  # Prune the branch
                        break
        return best_score

    # Minimizing player's turn (Human)
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Human makes a move
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '  # Undo the move
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:  # Prune the branch
                        break
        return best_score


def best_move():
    """Finds and returns the best move for the AI using the minimax function."""
    best_score = -math.inf
    move = (-1, -1)
    alpha, beta = -math.inf, math.inf  # Initialize alpha and beta
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # AI tries this move
                score = minimax(board, 0, False, alpha, beta)
                board[i][j] = ' '  # Undo the move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def main():
    """Main game loop."""
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Human player's move
        x, y = map(int, input("Enter your move (row and column: 0, 1, or 2): ").split())
        if board[x][y] == ' ':
            board[x][y] = 'X'
        else:
            print("Invalid move! Try again.")
            continue

        print_board(board)
        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI is making a move...")
        ai_move = best_move()
        board[ai_move[0]][ai_move[1]] = 'O'
        print_board(board)
        
        if is_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
