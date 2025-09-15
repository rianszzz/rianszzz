import random
import os

# Buat papan default
default_board = [
    list("#######"),
    list("#.....#"),
    list("#.###.#"),
    list("#.#P#.#"),
    list("#.###.#"),
    list("#.....#"),
    list("#######")
]

def load_board():
    if not os.path.exists("board.txt"):
        save_board(default_board)
        return default_board
    with open("board.txt", "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def save_board(board):
    with open("board.txt", "w") as f:
        for row in board:
            f.write("".join(row) + "\n")

def move_pacman(board):
    # Cari posisi Pac-Man
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "P":
                x, y = i, j
                break

    # Pilih arah acak
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    dx, dy = random.choice(moves)
    nx, ny = x + dx, y + dy

    # Kalau bukan dinding, pindah
    if board[nx][ny] != "#":
        if board[nx][ny] == ".":
            board[nx][ny] = "P"
        else:
            board[nx][ny] = "P"
        board[x][y] = " "

    return board

def render_readme(board):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Pac-Man Otomatis\n\n")
        f.write("Setiap 30 menit Pac-Man bergerak 1 langkah.\n\n")
        for row in board:
            f.write("".join(row) + "\n")

if __name__ == "__main__":
    board = load_board()
    board = move_pacman(board)
    save_board(board)
    render_readme(board)
