import ursina

class Environment:
    def __init__(self):
        self.scale_factor = ursina.window.size[0] / ursina.window.size[1]

    def create(self, app, shader):
    # Load the texture
        texture = ursina.Texture('Resources/images/backgrounds/landscape.jpg')

    # Calculate the scale factor based on the aspect ratio of the image and the window
        #aspect_ratio = texture.width / texture.height
        scale_x = 25
        scale_y = 25

    # Create the background entity
        self.background = ursina.Entity(
        model='quad',
        texture=texture,
        scale=(scale_x, scale_y),
        z=10,
        shader=shader
    )