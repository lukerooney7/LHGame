import pygame

from objects.ships.Ships import SmallShip, MediumShip, LargeShip
from objects.weapons.PlayerBall import PlayerBall

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)
pygame.display.set_caption('follow mouse')
surface.fill((0,0,0))
blood_splashes = []
power = 0
MAX_POWER = 100
charging = False
state = 0
last_wave_time = 0
WAVE_INTERVAL = 500

background = pygame.image.load("images/background.png")

waves = [pygame.image.load("images/wave1.png"),
         pygame.image.load("images/wave2.png"),
         pygame.image.load("images/wave3.png"),
         pygame.image.load("images/wave4.png"),
         pygame.image.load("images/wave5.png")]

enemy_cannonballs = []

ships = [
    SmallShip(surface, 600, 4),
    MediumShip(surface, 600, 3),
    LargeShip(surface, 600, 2),
    MediumShip(surface, 600, 1),
]
cannonballs = []


def draw_power_bar():
    bar_width = 300
    bar_height = 20
    x = 50
    y = WINDOW_HEIGHT - 50

    pygame.draw.rect(surface, (50, 50, 50), (x, y, bar_width, bar_height))

    fill_width = int((power / MAX_POWER) * bar_width)
    pygame.draw.rect(surface, (255, 0, 0), (x, y, fill_width, bar_height))

    pygame.draw.rect(surface, (255, 255, 255), (x, y, bar_width, bar_height), 2)

def scope():
    x, y = pygame.mouse.get_pos()
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 255))

    pygame.draw.circle(
        overlay,
        (0, 0, 0, 0),
        (x, 300),
        300
    )

    # Black background
    surface.blit(overlay, (1, 0))
    pygame.draw.line(surface, (255, 255, 255), (x - 75, 300), (x + 75, 300), 2)
    pygame.draw.line(surface, (255, 255, 255), (x, 300 - 75), (x, 300 + 75), 2)

def draw(state, last_wave_time):
    current_time = pygame.time.get_ticks()
    if current_time - last_wave_time >= WAVE_INTERVAL:
        state = (state + 1) % len(waves)
        last_wave_time = current_time

    surface.fill((80, 120, 160))
    surface.blit(background, (0, 0))
    surface.blit(waves[state], (0, 0))
    for ship in ships:
        ship.draw()
        ship.move()

    for ball in cannonballs:
        ball.draw()
        ball.move()

    for ball in enemy_cannonballs:
        ball.draw()
        ball.move()

    scope()
    draw_power_bar()
    return state, last_wave_time

def shoot(cannonballs, power):
    if power < 10:
        power_level = 0
    elif power < 30:
        power_level = 1
    elif power < 50:
        power_level = 2
    elif power < 70:
        power_level = 3
    elif power < 90:
        power_level = 4
    else:
        power_level = 5
    x, _ = pygame.mouse.get_pos()
    cannonballs += [PlayerBall(surface, x, power_level)]
    return

def interact(cannonballs):
    for ship in ships:
        shot = ship.shoot()
        if shot:
            enemy_cannonballs.append(shot)
        for ball in cannonballs:
            # Check left and right
            if ball.x - ball.size > ship.rect.bottomleft[0] and ball.x + ball.size < ship.rect.bottomright[0]:
                if ball.level == ship.level and ball.y < ship.y:
                    ship.hit()
                    ball.hit()

    for enemy_ball in enemy_cannonballs:
        if enemy_ball.y > 600:
            enemy_ball.hit()

    return [ball for ball in enemy_cannonballs if not ball.landed], [ball for ball in cannonballs if not ball.landed]

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            charging = True

        if event.type == pygame.MOUSEBUTTONUP:
            charging = False
            shoot(cannonballs, power)
            power = 0

    if charging and power < MAX_POWER:
        power += 1

    enemy_cannonballs, cannonballs = interact(cannonballs)
    state, last_wave_time = draw(state, last_wave_time)

    pygame.display.update()
