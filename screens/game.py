from config.base import Base
import pygame
import random

class Game(Base):
    score = 0
    lifes = ["x", "x", "x"]
    balls = []

    CAMP = {
        "C": ["C", "Dm", "Em", "F", "G", "Am", "Bm7"],
        "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#m7"],
        "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#m7"],
        "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Em7"],
        "G": ["G", "Am", "Bm", "C", "D", "Em", "F#m7"],
        "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#m7"],
        "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#m7"],
    }

    GREEN = (0,255,0)
    RED = (255,0,0)
    BALL_RADIUS = 10

    SPAWN_INTERVAL = 3000  
    last_spawn = 0

    @classmethod
    def draw_header(cls):
        Base.display.fill((0,0,0))

        cls.render_text(text=f"Score: {cls.score}", y_percent=0.05, x_percent=0.1)
        x_start = 0.45 
        gap = 0.05

        for i, life in enumerate(cls.lifes):
            cls.render_text(text=life, y_percent=0.05, x_percent=x_start + i * gap)

    @classmethod
    def game_over(cls):
        Base.display.fill((0,0,0))

        cls.render_text(text=f"Game Over", y_percent=0.5, x_percent=0.5)
        pygame.display.update()
        pygame.time.delay(2000)


    @classmethod
    def start(cls, camp):
        cls.score = 0
        cls.lifes = ["x", "x", "x"]
        running = True

        while running:
            for event in pygame.event.get():
                if len(cls.lifes) == 0:
                    cls.game_over()
                    running = False

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        cls.score +=1
                    elif event.key == pygame.K_1:
                        cls.lifes.pop()

            cls.draw_header()
            pygame.display.update()


