from config.base import Base
from .select_camp import SelectCamp
import pygame

class Game(Base):
    @classmethod
    def start(cls):
        Base.display = pygame.display.set_mode((cls.x, cls.y))

        pygame.display.set_caption('Gamezin')

        Base.display.fill((0,0,0))

        pygame.display.flip()

        running = True

        cls.render_text("Pressione Space Para Continuar", 0.5, 0.8)
        pygame.display.update()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        SelectCamp.start()

        pygame.quit()
