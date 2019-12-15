import pgzrun
from random import randint
apple = Actor('apple')


def draw():
    screen.clear()
    apple.draw()
    
    

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    
    else:
        print("You missed!")
        print('Click the apple to play again.')
        on_mouse_click_apple_to_start_game_again(pos)

def on_mouse_click_apple_to_start_game_again(pos):
    if apple.collidepoint(pos):
        place_apple()
        place_orange()
        place_pineapple()
        print('Let\'s Play Again!')


pgzrun.go()
