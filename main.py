def display_board(board: list):

    print()
    print()
    for row in board:
        print("\t\t\t", end="")
        for item in row:
            if item % 3 != 0:
                print(f"{item}|", end="")
            else:
                print(item)
        print("\t\t\t-----")
    print()
    print()

def main():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    display_board(board)

main()
