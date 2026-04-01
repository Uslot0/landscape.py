import math
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480

SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

sun = 0
wave_speed = 0
wave_color = (100, 180, 230)
wave = [
    (185, 213),
    (314, 211),
    (309, 137),
    (341, 104),
    (375, 127),
    (383, 97),
    (346, 63),
    (261, 71),
    (209, 108),
    (189, 169)
]

leaves = [
    (101, 250),
    (57, 253),
    (29, 291),
    (5, 259),
    (34, 216),
    (97, 206),
    (138, 249),
    (170, 263),
    (185, 297),
    (210, 271),
    (181, 224),
    (135, 203)
]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((173, 216, 230))
    pygame.draw.rect(screen, (79, 66, 181), (0, HEIGHT * 0.35, WIDTH, HEIGHT * 0.65))
    pygame.draw.rect(screen, (246, 215, 176), (0, HEIGHT * 0.65, WIDTH, HEIGHT * 0.35))

    pygame.draw.circle(screen, "white", (180, 35), 30)
    pygame.draw.circle(screen, "white", (200, 45), 30)
    pygame.draw.circle(screen, "white", (140, 45), 30)
    pygame.draw.circle(screen, "white", (450, 35), 30)
    pygame.draw.circle(screen, "white", (470, 45), 30)
    pygame.draw.circle(screen, "white", (420, 45), 30)
    
    pygame.draw.rect(screen, (173, 216, 230), (400, 350, 120, 60))

    sun += 0.05
    sun_speed = 30 + int(10* math.sin(sun)) #30 is the radius
    pygame.draw.circle(screen, "yellow", (605, 35), sun_speed)

    wave_speed += 3
    if wave_speed > WIDTH:
        wave_speed = -400

    moved_wave = [(x + wave_speed, y) for x, y in wave]
    pygame.draw.polygon(screen, wave_color, moved_wave)

    pygame.draw.rect(screen, (180, 140, 100), (100, 250, 40, 150))
    pygame.draw.polygon(screen, "green", leaves)
    pygame.draw.circle(screen, (139, 69, 19), (100, 250), 20)
    pygame.draw.circle(screen, (139, 69, 19), (140, 250), 20)
    pygame.draw.circle(screen, (139, 69, 19), (120, 230), 20)
    pygame.draw.rect(screen, (230, 200, 160), (250, 370, 50, 50))
    pygame.draw.rect(screen, (230, 200, 160), (210, 380, 40, 40))
    pygame.draw.rect(screen, (230, 200, 160), (300, 380, 40, 40))
    
    square_x=250
    squarecount=0
    while square_x <= 390:
        squarecount +=1
        square_x += 20
        if squarecount <3:
            pygame.draw.rect(screen, (230, 200, 160), (square_x-60, 375, 9, 9))
        elif 2 < squarecount < 6:
            pygame.draw.rect(screen, (230, 200, 160), (square_x-60, 365, 10, 10))
        else: 
            pygame.draw.rect(screen, (230, 200, 160), (square_x-80, 375, 9, 9))




    pygame.display.flip()
    clock.tick(60)



pygame.quit()