import pygame

from config.base import Base
from screens.game import Game

class SelectCamp(Base):
    options = ['C','D','E','F','G','A','B']
    selected = 0

    @classmethod
    def draw_menu(cls):
        Base.display.fill((0,0,0))

        cls.render_text(text="Escolha o Campo Hármonico", y_percent=0.2, x_percent=0.5)

        for i, op in enumerate(cls.options):
            x = 0.2 + (i * 0.1)
            color = (0,0,255) if i == cls.selected else (255,255,255)
            cls.render_text(text=op, y_percent=0.8, x_percent=x, color=color)


    @classmethod
    def start(cls):
        running = True

        while running:
            cls.draw_menu()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        cls.selected = (cls.selected - 1) % len(cls.options)
                    elif event.key == pygame.K_RIGHT:
                        cls.selected = (cls.selected + 1) % len(cls.options)
                    elif event.key == pygame.K_RETURN:
                        Game.start(cls.options[cls.selected])
