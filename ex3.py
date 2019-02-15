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
# To avoid storing 8 masks (3 rows, 3 cols, and 2 diagonals), we shift th cols
# and rows masks 3 bits 3 times, isolating the relevant cells
# using the & operator, and comparing the result to the mask itself.
def whowon(boards):
    win_row_col = [0b111000000, 0b100100100]
    win_diagonal = [0b100010001, 0b001010100]
    for i in range(2):
        for mask in win_row_col:
            tmp_mask = mask
            for shift in range(3):
                res = boards[i] & tmp_mask
                if res == tmp_mask:
                    return i+1
                tmp_mask = tmp_mask >> 3
        
        for mask in win_diagonal:
            res = boards[i] & mask
            if res == mask:
                return i+1


def main():
    game = [[1, 2, 2],
            [1, 1, 2],
            [2, 2, 1]]
    print("Player "+ str(whowon(convert_board(game)))+" wins.")

main()
