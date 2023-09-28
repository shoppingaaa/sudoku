> 这是我们的结队编程作业# sudoku
# 使用指南
### 下载main分支里的“数独主要代码”，在vscode或者pycharm打开文件夹，运行server.py,点击运行结果里的网址即可
具体步骤如下（以pycharm为例）

1. 在pycharm打开文件
   
<img width="960" alt="image" src="https://github.com/shoppingaaa/sudoku/assets/143972767/193ca3f0-2d07-42c1-83af-0d5b903e7734">

> 确保在你的开发环境中安装了 flask。可以在终端使用以下命令使用 pip 安装 flask：`pip install flask`

2. 运行server.py，访问运行结果里的网址
   <img width="960" alt="image" src="https://github.com/shoppingaaa/sudoku/assets/143972767/d33ad97e-cf06-47ff-979d-c1ad4566d73e">

3.成功打开页面，现在可以开始求解数独了！
  <img width="960" alt="image" src="https://github.com/shoppingaaa/sudoku/assets/143972767/2826c09f-1587-4b23-963c-85b795d4256e">

- 难度选择
  如果想要挑战不同难度的数独，可以修改server.py中的以下代码：
  
  `dig_holes(dighole, 45)`
  
  把‘45’改成你想要的每个九宫格空白格数，为你的数独生成不同的难度，建议在40~55之间，修改后重新运行打开即可。
  
  > 可以把挖空数改成1用来检查数独的功能
  

   
