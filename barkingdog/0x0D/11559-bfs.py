from collections import deque


def pop(i, j):
    visited = [[False] * 6 for _ in range(12)]
    visited[i][j] = True
    queue = deque([(i, j)])
    target = [(i, j)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if visited[nx][ny] or board[nx][ny] != board[x][y]:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny))
            target.append((nx, ny))

    if len(target) >= 4:
        for i, j in target:
            pop_list.add((i, j))


board = [list(input()) for _ in range(12)]

answer = 0
while True:
    pop_list = set()
    for i in range(12):
        for j in range(6):
            if board[i][j] != ".":
                pop(i, j)

    if not pop_list:
        break

    answer += 1
    for i, j in pop_list:
        board[i][j] = "."

    for j in range(6):
        for i in range(11, -1, -1):
            if board[i][j] != ".":
                continue

            for k in range(i - 1, -1, -1):
                if board[k][j] != ".":
                    board[i][j], board[k][j] = board[k][j], "."
                    break

print(answer)