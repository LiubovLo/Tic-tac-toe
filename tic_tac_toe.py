board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Функция для вывода игрового поля
def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Функция для проверки конца игры
def is_game_over():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

# Главный цикл игры
while True:
    print_board()

    row = int(input("Введите номер строки (0, 1, 2): "))
    col = int(input("Введите номер столбца (0, 1, 2): "))


    if board[row][col] == ' ':
        board[row][col] = current_player
    else:
        print("Клетка занята, попробуйте еще раз")
        continue

    if is_game_over():
        print_board()
        print(f"Игра окончена, победил игрок {current_player}")
        break
    if all(all(cell != " " for cell in row) for row in board):
        print_board()
        print("Ничья")
        break


    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'