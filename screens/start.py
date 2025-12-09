from .select_camp import SelectCamp
import pygame

class Game:
    display = None
    x, y = 700, 700 

    @classmethod
    def start(cls):
        cls.display = pygame.display.set_mode((cls.x, cls.y))

        pygame.display.set_caption('Gamezin')

        cls.display.fill((0,0,0))

        pygame.display.flip()

        running = True

        cls.render_text("Pressione Space Para Continuar")

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        SelectCamp.start(cls.display)

        pygame.quit()

    @classmethod
    def render_text(cls, text):
        if cls.display is None:
            raise Exception("Display ainda não foi iniciado")

        pygame.font.init()
        fonte = pygame.font.SysFont(None, 40)

        txt = fonte.render(text, True, (255,255,255))

        rect = txt.get_rect()

        rect.center = (int(cls.x * 0.5), int(cls.y * 0.8))

        cls.display.blit(txt, rect)
        pygame.display.update()
