from config.base import Base
import pygame
import random

class Game(Base):
    score = 0
    lifes = ["x", "x", "x"]

    ball_pos = [0.5, 0.0] 
    ball_speed = 0.0008
    ball_color = (255, 0, 0) 

    player_x = 0.5

    CAMP = {
        "C": ["C", "Dm", "Em", "F", "G", "Am", "Bm7"],
        "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#m7"],
        "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#m7"],
        "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Em7"],
        "G": ["G", "Am", "Bm", "C", "D", "Em", "F#m7"],
        "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#m7"],
        "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#m7"],
    }
    RED = (255,0,0)
    GREEN = (0,255,0)

    @classmethod
    def spawn_ball(cls):
        cls.ball_pos = [random.random(), 0.0]
        cls.ball_color = random.choice([cls.GREEN, cls.RED])

    @classmethod
    def update_ball(cls):
        cls.ball_pos[1] += cls.ball_speed

        if cls.ball_pos[1] > 1:
            if cls.ball_color == cls.RED:
                cls.score -= 1
            else:
                cls.score += 1

            cls.spawn_ball()

    @classmethod
    def draw_ball(cls):
        cls.render_ball(tuple(cls.ball_pos), cls.ball_color)

    @classmethod
    def draw_player(cls):
        cls.render_player(cls.player_x)

    @classmethod
    def update_player(cls):
        print(cls.player_x)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            cls.player_x -= 0.0005 

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            cls.player_x += 0.0005

        cls.player_x = max(0, min(1, cls.player_x))

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
                    if event.key == pygame.K_RIGHT:
                        cls.player_x += 1
                    elif event.key == pygame.K_LEFT:
                        cls.player_x -= 1

            cls.draw_header()

            cls.update_ball()
            cls.update_player()
            
            cls.draw_player()
            cls.draw_ball()
            pygame.display.update()


