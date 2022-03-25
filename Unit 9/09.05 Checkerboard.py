n = int(input("Enter size: "))
board = []

for i in range(n):
    board.append([' '] * n)
for i in range(0,n,2):
    for j in range(1,n,2):
        board[i][j] = '*'
for i in range(1,n,2):
    for j in range(0,n,2):
        board[i][j] = '*'

print('+' + '-'*(n) + '+')
for i in range(len(board)):
    print('|', end='')
    for j in range(len(board[i])):
        print(board[i][j], end='')
    print('|')
print('+' + '-'*(n) + '+')