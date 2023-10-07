import copy
import threading

from flask import Flask, render_template
from generate import generate_puzzle, dig_holes

app = Flask(__name__)

@app.route('/')
def index():

    # 创建一个空列表用于保存生成的九个数独谜题
    sudokus = []

    # 定义生成数独的函数
    def generate_sudoku():
        sudoku = generate_puzzle()
        dighole = copy.deepcopy(sudoku)
        dig_holes(dighole, 45)
        return (sudoku, dighole)

    # 创建九个线程，每个线程生成一个数独谜题并将其保存到列表中
    threads = []
    for _ in range(9):
        thread = threading.Thread(target=lambda: sudokus.append(generate_sudoku()))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成生成任务
    for thread in threads:
        thread.join()

    # 将九个数独谜题传递给模板进行渲染
    return render_template('sudogame_update.html', sudokus=sudokus)


if __name__ == '__main__':

    app.run()
