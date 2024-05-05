import ursina

class InputHandler(ursina.Entity):
    def __init__(self, player, speed=1, jump_speed = 5, jump_height = 2):
        super().__init__()
        self.player = player
        self.speed = speed
        self.jump_speed = jump_speed
        self.jump_height = jump_height
        self.jumping = False
        self.falling = False
        self.start_y = None


    def update(self):
        if ursina.held_keys['a']:
            self.player.x -= self.speed * ursina.time.dt
        if ursina.held_keys['d']:
            self.player.x += self.speed * ursina.time.dt
        if ursina.held_keys['w']:
            self.player.z += self.speed * ursina.time.dt
        if ursina.held_keys['s']:
            self.player.z -= self.speed * ursina.time.dt

        if ursina.held_keys['q']:
            self.player.rotation_y += ursina.time.dt * 100
        if ursina.held_keys['e']:
            self.player.rotation_y -= ursina.time.dt * 100

        if ursina.held_keys['space'] and not self.jumping:
            self.jumping = True
            self.start_y = self.player.y

        if self.jumping and not self.falling:
            if self.player. y < self.start_y + self.jump_height:
                self.player.y += self.jump_speed * ursina.time.dt
            else:
                self.falling = True

        if self.falling:
            if self.player.y > self.start_y:
                self.player.y -= self.jump_speed * ursina.time.dt
            else:                       
                self.jumping = False
                self.falling = False
                self.start_y = None
                