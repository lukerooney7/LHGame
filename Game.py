import pygame

from config import WINDOW_WIDTH, WINDOW_HEIGHT
from objects.ships.Ships import SmallShip, MediumShip, LargeShip
from objects.ui.UI import MAX_POWER, UI
from objects.user.user import User, MAX_HEALTH
from objects.weapons.PlayerBall import PlayerBall


class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
        pygame.display.set_caption("Pirate Game")

        self.clock = pygame.time.Clock()
        self.running = True
        self.user = User()
        # Game state
        self.power = 0
        self.charging = False
        self.state = 0
        self.last_wave_time = 0

        self.WAVE_INTERVAL = 500

        # Assets
        self.background = pygame.image.load("images/background.png")

        self.waves = [
            pygame.image.load("images/wave1.png"),
            pygame.image.load("images/wave2.png"),
            pygame.image.load("images/wave3.png"),
            pygame.image.load("images/wave4.png"),
            pygame.image.load("images/wave5.png"),
        ]

        # Objects
        self.ships = [
            SmallShip(self.surface, 4),
            MediumShip(self.surface, 3),
            LargeShip(self.surface, 2),
            LargeShip(self.surface, 1),
        ]

        self.cannonballs = []
        self.enemy_cannonballs = []

        self.ui = UI(self.surface, self.user)

    # ------------------ UI ------------------

    def scope(self):
        x, _ = pygame.mouse.get_pos()

        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 255))

        pygame.draw.circle(
            overlay,
            (0, 0, 0, 0),
            (x, 300),
            300
        )

        self.surface.blit(overlay, (0, 0))
        pygame.draw.line(self.surface, (255, 255, 255), (x - 75, 300), (x + 75, 300), 2)
        pygame.draw.line(self.surface, (255, 255, 255), (x, 225), (x, 375), 2)

    # ------------------ GAME LOGIC ------------------

    def shoot(self):
        if self.user.cannonballs > 0:
            if self.power < 10:
                power_level = 0
            elif self.power < 30:
                power_level = 1
            elif self.power < 50:
                power_level = 2
            elif self.power < 70:
                power_level = 3
            elif self.power < 90:
                power_level = 4
            else:
                power_level = 5
            x, _ = pygame.mouse.get_pos()
            self.cannonballs.append(PlayerBall(self.surface, x, power_level))
            self.user.cannonballs -= 1


    def interact(self):
        for ship in self.ships:
            shot = ship.shoot()
            if shot:
                self.enemy_cannonballs.append(shot)

            for ball in self.cannonballs:
                if (
                    ball.x - ball.size > ship.rect.bottomleft[0]
                    and ball.x + ball.size < ship.rect.bottomright[0]
                    and ball.level == ship.level
                    and ball.y < ship.y
                    and not ball.landed
                ):
                    self.user.cannonballs += ship.cannonballs
                    self.user.coins += ship.coins
                    ship.hit()
                    ball.hit()

        for enemy_ball in self.enemy_cannonballs:
            if enemy_ball.y > 600:
                self.user.health -= 1
                enemy_ball.hit()

        self.enemy_cannonballs = [
            b for b in self.enemy_cannonballs if not b.landed
        ]
        self.cannonballs = [
            b for b in self.cannonballs if not b.finished
        ]

    # ------------------ DRAW ------------------

    def draw(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_wave_time >= self.WAVE_INTERVAL:
            self.state = (self.state + 1) % len(self.waves)
            self.last_wave_time = current_time

        self.surface.fill((80, 120, 160))
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.waves[self.state], (0, 0))

        for ship in self.ships:
            ship.move()
            ship.draw()

        for ball in self.cannonballs:
            ball.move()
            ball.draw()

        for ball in self.enemy_cannonballs:
            ball.move()
            ball.draw()

        self.scope()
        self.ui.draw(self.power)

        pygame.display.update()

    # ------------------ MAIN LOOP ------------------

    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.charging = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.charging = False
                    self.shoot()
                    self.power = 0

            if self.charging and self.power < MAX_POWER:
                self.power += 1

            self.interact()
            self.draw()

        pygame.quit()

