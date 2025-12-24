import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
from config import WINDOW_WIDTH, WINDOW_HEIGHT
from Game import Game
FPS = 60

game = Game()
background_image = pygame_menu.BaseImage(
    image_path='menu_background.jpg'
)

def start_game():
    game = Game()
    game.run()

def main_background() -> None:
    background_image.draw(surface)

def main(test: bool = False) -> None:
    global main_menu
    global surface

    surface = create_example_window('Pirate Game', (WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    main_menu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    main_menu_theme.set_background_color_opacity(0.4)  # 50% opacity
    main_menu = pygame_menu.Menu(
        height=WINDOW_HEIGHT* 0.7,
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=main_menu_theme,
        title='Pirate Game',
        width=WINDOW_WIDTH * 0.8
    )

    theme_bg_image = main_menu_theme.copy()
    theme_bg_image.background_color = pygame_menu.BaseImage(
        image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER
    )
    theme_bg_image.title_font_size = 25

    main_menu.add.button('Play', start_game)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    # Main loop
    while True:
        clock.tick(FPS)
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        if test:
            break


if __name__ == '__main__':
    main()