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

    @classmethod
    def render_ball(cls, position = (0.1, 0.2), color = (255,0,0)):

        if cls.display is None:
            raise Exception("Display ainda não foi iniciado")

        x = int(cls.x * position[0])
        y = int(cls.y * position[1])

        pygame.draw.circle(
            cls.display,
            color,
            (x,y),
            10
        )


    @classmethod
    def render_player(cls, player_x):

        if cls.display is None:
            raise Exception("Display ainda não foi iniciado")

        player_width = 20
        player_height = 20

        x = int(cls.x * player_x) - player_width // 2
        y = int(cls.y * 0.9)

        pygame.draw.rect(
            cls.display,
            (0, 0, 255),
            (x, y, player_width, player_height)
        )

