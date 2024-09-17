import pygame
import random
from utils import load_patterns

class Game:
    def __init__(self, screen, difficulty_level):
        self.screen = screen
        self.difficulty_level = difficulty_level
        self.time_left = self.set_time_limit(difficulty_level)
        self.clock = pygame.time.Clock()
        self.board = self.create_board()
        self.first_click = None  # 用于存储第一次点击的图案位置
        self.background = pygame.image.load('../assets/background/back.png')  # 加载背景图片

    def set_time_limit(self, difficulty_level):
        if difficulty_level == 'easy':
            return 120
        elif difficulty_level == 'medium':
            return 90
        else:
            return 60

    def create_board(self):
        patterns = load_patterns()  # 调用加载图案的函数
        patterns = patterns[:8]  # 只使用前8种图案
        patterns *= 2  # 每种图案成对出现
        random.shuffle(patterns)  # 打乱图案顺序
        board = [patterns[i * 4:(i + 1) * 4] for i in range(4)]  # 4x4的游戏板
        return board

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_click(event.pos)
        self.time_left -= self.clock.tick(60) / 1000  # 每秒减少时间
        if self.time_left <= 0:
            self.game_over()

    def handle_click(self, pos):
        # 计算游戏板的总宽度和高度
        tile_size = 100
        spacing = 10
        board_width = len(self.board[0]) * (tile_size + spacing) - spacing
        board_height = len(self.board) * (tile_size + spacing) - spacing

        # 计算游戏板的左上角位置，使其居中
        offset_x = (self.screen.get_width() - board_width) // 2
        offset_y = (self.screen.get_height() - board_height) // 2

        # 调整点击位置的计算，考虑偏移量和间隔
        col = (pos[0] - offset_x) // (tile_size + spacing)
        row = (pos[1] - offset_y) // (tile_size + spacing)

        if row >= len(self.board) or col >= len(self.board[0]) or row < 0 or col < 0:
            return  # 如果点击超出游戏板范围，直接返回

        if self.board[row][col] is None:
            return  # 如果点击的是空白区域，直接返回

        if self.first_click is None:
            self.first_click = (row, col)  # 记录第一次点击的位置
        else:
        # 检查两次点击的图片是否相同且路径可达
            if (row, col) != self.first_click and self.board[row][col] == self.board[self.first_click[0]][self.first_click[1]]:
                if self.is_path_clear(self.first_click, (row, col)):
                    self.board[row][col] = None  # 移除第二次点击的图片
                    self.board[self.first_click[0]][self.first_click[1]] = None  # 移除第一次点击的图片
            self.first_click = None  # 重置第一次点击
    def is_path_clear(self, start, end):
        # 这里可以实现路径检查逻辑
        return True

    def game_over(self):
        print("Game Over")
        pygame.quit()
        exit()

    def draw(self):
        self.screen.blit(self.background, (0, 0))  # 绘制背景图片
        # 计算游戏板的总宽度和高度，考虑间隔
        tile_size = 100
        spacing = 10
        board_width = len(self.board[0]) * (tile_size + spacing) - spacing
        board_height = len(self.board) * (tile_size + spacing) - spacing

        # 计算游戏板的左上角位置，使其居中
        offset_x = (self.screen.get_width() - board_width) // 2
        offset_y = (self.screen.get_height() - board_height) // 2

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                tile = self.board[row][col]
                if tile is not None:
                    # 使用计算出的左上角位置进行偏移，并添加间隔
                    x = col * (tile_size + spacing) + offset_x
                    y = row * (tile_size + spacing) + offset_y
                    self.screen.blit(tile, (x, y))

        # 创建字体对象
        font = pygame.font.Font(None, 36)
        # 渲染剩余时间为文本图像，只显示整数秒数
        time_text = font.render(f"Time Left: {int(self.time_left)}", True, (0, 0, 0))
        # 将文本图像绘制到屏幕上
        self.screen.blit(time_text, (10, 10))