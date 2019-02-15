# Converts the board into 2 binary numbers, each representing a board of a player.
# If theres a 1 in a cell, places a 1 in the first number and shifts both numbers left.
# If theres a 2 in a cell, places a 1 in the second number and shifts both numbers left.
def convert_board(game):
    boards = [0b000000000,0b000000000]
    for row in game:
        for cell in row:
            boards[0] = boards[0] << 1
            boards[1] = boards[1] << 1
            if cell == 1:
                boards[0] = boards[0] | 1 # turn on right bit
            elif cell == 2:
                boards[1] = boards[1] | 1 # turn on right bit        
    return boards

# Gets 2 binary numbers and compares them to the winning masks.
# To avoid storing 8 masks (3 rows, 3 cols, and 2 diagonals), we shift the cols
# mask one bit at a time and rows mask 3 bits 3 times, isolating the relevant cells
# using the & operator, and comparing the result to the mask itself.
def whowon(boards):
    win_row = 0b111000000 
    win_col = 0b100100100
    win_diagonal = [0b100010001, 0b001010100]
    for i in range(2):
        tmp_row_mask = win_row
        tmp_col_mask = win_col
        for shift in range(3):
            res_col = boards[i] & tmp_col_mask
            res_row = boards[i] & tmp_row_mask
            if res_col == tmp_col_mask or res_row == tmp_row_mask:
                return i+1
            tmp_col_mask = tmp_col_mask >> 1
            tmp_row_mask = tmp_row_mask >> 3
        
        for mask in win_diagonal:
            res = boards[i] & mask
            if res == mask:
                return i+1
    return 0


def main():
    game = [[1, 2, 1],
            [1, 1, 2],
            [2, 1, 2]]
    winner = whowon(convert_board(game))
    if winner == 0:
        print("No winners.")
    else:
        print("Player "+ str()+" wins.")

main()
