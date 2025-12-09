import pygame

class SelectCamp:
    @classmethod
    def start(cls, display):
        display.fill((0, 0, 80))

        fonte = pygame.font.SysFont(None, 50)
        texto = fonte.render("Tela SelectCamp", True, (255, 255, 255))
        rect = texto.get_rect(center=(350, 350))

        display.blit(texto, rect)
        pygame.display.update()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
