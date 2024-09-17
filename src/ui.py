import pygame

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

    def draw_button(self, rect, text):
        # 绘制圆角矩形按钮
        pygame.draw.rect(self.screen, (0, 0, 0), rect, border_radius=10)
        pygame.draw.rect(self.screen, (100, 100, 100), rect.inflate(-4, -4), border_radius=10)

        # 绘制按钮文本
        font = pygame.font.Font(None, 36)
        text_surf = font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)

    def show(self):
        button_width = 150
        button_height = 50
        button_y = self.screen_height // 2 - button_height // 2

        # 定义三个难度按钮的位置和大小
        difficulty_buttons = {
            "easy": pygame.Rect(self.screen_width // 4 - button_width // 2, button_y, button_width, button_height),
            "medium": pygame.Rect(self.screen_width // 2 - button_width // 2, button_y, button_width, button_height),
            "hard": pygame.Rect(3 * self.screen_width // 4 - button_width // 2, button_y, button_width, button_height)
        }

        selected_difficulty = None

        while True:
            self.screen.fill((255, 255, 255))  # 清空屏幕
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测是否点击了某个难度按钮
                    for difficulty, rect in difficulty_buttons.items():
                        if rect.collidepoint(event.pos):
                            selected_difficulty = difficulty
                            return selected_difficulty  # 返回选择的难度

            # 绘制难度按钮
            for difficulty, rect in difficulty_buttons.items():
                self.draw_button(rect, difficulty.capitalize())

            pygame.display.flip()

