import telebot


bot = telebot.Telebot('5907869617:AAFxh5mSIaoqmRVzmzDpj3Ah97E565WgkGk')

# Определяем символы игроков и пустую ячейку
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Определяем функцию для создания игрового поля
def create_board():
    board = {}
    for i in range(1, 10):
        board[str(i)] = EMPTY
    return board

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_game(message):
    global board
    global chat_id
    board = create_board()
    chat_id = message.chat.id
    # Отрисовываем игровое поле
    draw_board(chat_id, board)
    # Отправляем сообщение с инструкциями
    bot.send_message(chat_id, "Чтобы сделать ход, отправьте номер ячейки от 1 до 9.")

# Инициализируем игровое поле
board = {str(i): EMPTY for i in range(1, 10)}

# Определяем функцию для отрисовки игрового поля
def draw_board(chat_id, board):
    bot.send_message(chat_id, f"{board['1']}|{board['2']}|{board['3']}\n"
                             f"{board['4']}|{board['5']}|{board['6']}\n"
                             f"{board['7']}|{board['8']}|{board['9']}")

# Определяем функцию для проверки, заполнено ли игровое поле
def check_board_full(board):
    for cell in board.values():
        if cell == EMPTY:
            return False
    return True

# Определяем функцию для проверки, есть ли победитель
def check_winner(board):
    # Проверяем горизонтали
    if board['1'] == board['2'] == board['3'] and board['1'] != EMPTY:
        return board['1']
    if board['4'] == board['5'] == board['6'] and board['4'] != EMPTY:
        return board['4']
    if board['7'] == board['8'] == board['9'] and board['7'] != EMPTY:
        return board['7']
    # Проверяем вертикали
    if board['1'] == board['4'] == board['7'] and board['1'] != EMPTY:
        return board['1']
    if board['2'] == board['5'] == board['8'] and board['2'] != EMPTY:
        return board['2']
    if board['3'] == board['6'] == board['9'] and board['3'] != EMPTY:
        return board['3']
    # Проверяем диагонали
    if board['1'] == board['5'] == board['9'] and board['1'] != EMPTY:
        return board['1']
    if board['3'] == board['5'] == board['7'] and board['3'] != EMPTY:
        return board['3']
    return None

# Определяем функцию для хода компьютера
def computer_move():
    global board
    # Ищем пустую ячейку и ставим в неё нолик
    for i in range(1, 10):
        if board[str(i)] == EMPTY:
            board[str(i)] = PLAYER_O
            break
    # Отрисовываем игровое поле
    draw_board(chat_id, board)
    # Проверяем, есть ли победитель
    winner = check_winner(board)
    if winner is not None:
        # Выводим сообщение о победе
        bot.send_message(chat_id, f"Победил {winner}")
    return
# Определяем функцию для хода игрока
@bot.message_handler(func=lambda message: True)
def player_move(message):
    global board
    # Получаем номер ячейки, в которую сходил игрок
    cell_num = message.text
    if cell_num not in board.keys():
        bot.send_message(chat_id, "Неверный номер ячейки. Введите число от 1 до 9.")
        return
    if board[cell_num] != EMPTY:
        bot.send_message(chat_id, "Эта ячейка уже занята. Выберите другую.")
        return
    board[cell_num] = PLAYER_X
    # Отрисовываем игровое поле
    draw_board(chat_id, board)
    # Проверяем, есть ли победитель
    winner = check_winner(board)
    if winner is not None:
        # Выводим сообщение о победе
        bot.send_message(chat_id, f"Победил {winner}")
        return
    # Проверяем, заполнено ли игровое поле
    if check_board_full(board):
        bot.send_message(chat_id, "Ничья!")
        return
    # Ход компьютера
    computer_move()

