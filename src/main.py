import pygame
from game import Game
from ui import MainMenu
def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("羊了个羊小游戏")

    # 创建主菜单实例
    main_menu = MainMenu(screen)

    # 显示主菜单并获取用户选择的难度
    selected_difficulty = main_menu.show()
    if selected_difficulty is None:
        return  # 如果用户退出主菜单，直接退出程序

    # 创建游戏实例，并将难度系数传入
    game = Game(screen, difficulty_level=selected_difficulty)

    game.show()


if __name__ == "__main__":
    main()