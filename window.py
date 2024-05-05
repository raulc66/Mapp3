from ursina import window
import ursina

class Window:
    def __init__(self):
        self.app = ursina.Ursina()
        self.create()

    def create(self):
        window.size = (1024, 1024)
        window.color = ursina.color.green
        window.clear_color = ursina.color.black