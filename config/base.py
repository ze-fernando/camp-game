import pygame

class Base:
    display = None
    x = 700
    y = 700

    @classmethod
    def render_text(cls, text, x_percent, y_percent, color = (255,255,255)):

        if cls.display is None:
            raise Exception("Display ainda não foi iniciado")

        pygame.font.init()
        fonte = pygame.font.SysFont(None, 40)

        txt = fonte.render(text, True, color)

        rect = txt.get_rect()

        rect.center = (int(cls.x * x_percent), int(cls.y * y_percent))

        cls.display.blit(txt, rect)
