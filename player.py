import ursina

class Player:
    def __init__(self):
        self.player = None

    def create_player(self, app, lit_shader):
        """
        Create a player entity with a locust model and texture.
        """
        self.player = ursina.Entity(model='Resources/images/models/locust/locust.obj',
                            shader=lit_shader,
                            texture='Resources/images/models/locust/Image_0.jpg',
                            collider='box',
                            speed=5)

        try:
            with open('Resources/images/models/locust/locust.mtl') as f:
                for line in f:
                    if line.startswith('map_Kd'):
                        texture_path = line.split(' ')[-1].strip()
                        self.player.texture = ursina.load_texture(f'Resources/images/models/locust/{texture_path}')
        except Exception as e:
            print(f"Error reading locust.mtl: {e}")


    def get_player(self):
        """
        Return the player entity.
        """
        return self.player