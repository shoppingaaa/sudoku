import random
import sys


def find_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return -1, -1


def solve_puzzle(puzzle, solutions):
    # 查找空白位置
    row, col = find_empty(puzzle)

    # 如果没有空白位置，表示谜题已解答
    if row == -1 and col == -1:
        solutions.append([row[:] for row in puzzle])
        return

    # 尝试填入数字
    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num
            solve_puzzle(puzzle, solutions)
            puzzle[row][col] = 0


def generate_puzzle():
    puzzle = [[0] * 9 for _ in range(9)]
    fill_remaining(puzzle, 0, 0)
    return puzzle


def print_puzzle(puzzle):
    for row in range(9):
        for col in range(9):
            print(puzzle[row][col], end=' ')
        print()
    sys.stdout.flush()


def dig_holes(puzzle, num_holes):

    holes = random.sample(range(81), num_holes)

    # 确保挖空后的谜题仍然有唯一解
    while not has_unique_solution(puzzle, holes):
        holes = random.sample(range(81), num_holes)

    for hole in holes:
        row = hole // 9
        col = hole % 9
        puzzle[row][col] = 0


def is_valid(puzzle, row, col, num):
    # 检查当前数字在行中是否重复
    if num in puzzle[row]:
        return False

    # 检查当前数字在列中是否重复
    for i in range(9):
        if puzzle[i][col] == num:
            return False

    # 检查当前数字在九宫格中是否重复
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[i + start_row][j + start_col] == num:
                return False

    return True


def fill_remaining(puzzle, i, j):
    # 如果已经填充完最后一行，则生成完整数独谜题
    if i == 9 and j == 0:
        return True

    # 如果已经填充完一列，则填充下一行的第一个位置
    if j == 9:
        return fill_remaining(puzzle, i + 1, 0)

    # 如果当前位置已经填充数字，则填充下一个位置
    if puzzle[i][j] != 0:
        return fill_remaining(puzzle, i, j + 1)

    # 生成可选的数字列表
    available_nums = []
    for num in range(1, 10):
        if is_valid(puzzle, i, j, num):
            available_nums.append(num)

    # 随机选择一个数字填入当前位置
    random.shuffle(available_nums)
    for num in available_nums:
        puzzle[i][j] = num
        if fill_remaining(puzzle, i, j + 1):
            return True
        puzzle[i][j] = 0

    return False


def has_unique_solution(puzzle, holes):
    # 复制数独谜题，以免修改原谜题
    puzzle_copy = [row[:] for row in puzzle]

    # 挖掉指定位置的数字
    for hole in holes:
        row = hole // 9
        col = hole % 9
        puzzle_copy[row][col] = 0

    # 使用回溯法求解谜题
    solutions = []
    solve_puzzle(puzzle_copy, solutions)

    return len(solutions) == 1



