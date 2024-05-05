import ursina
from ursina.shaders import lit_with_shadows_shader as lit_shader
from window import Window
from environment import Environment
from player import Player
from input_handler import InputHandler

class Game:
    def __init__(self, window, environment, player):
        self.app = ursina.Ursina()
        self.window = window
        self.environment = environment
        self.player = player
        self.input_handler = None

    def setup(self):
        self.window.create()
        self.environment.create(self.app, lit_shader)
        self.player.create_player(self.app, lit_shader)
        self.input_handler = InputHandler(self.player.get_player())


    def run(self):
        self.app.run()

def create_game():
    window = Window()
    environment = Environment() 
    player = Player()
    return Game(window, environment, player)

if __name__ == '__main__':
    game = create_game()
    game.setup()
    game.run()