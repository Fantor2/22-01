class Bat:
    def __init__(self):
        bat_x = BAT_OFFSET
        bat_y = (SCREEN_HEIGHT - BAT_HEIGHT)
        self.bat.speedy=0
    def update(self):
        self.bat_y +=self.stick_speed_y
        if self.bat_y <=0:
            self.bat_y =0
        elif self.bat_y >= SCREEN_HEIGHT - BAT_HEIGHT:
            self.bat_y = SCREEN_HEIGHT - BAT_HEIGHT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.bat_x -=15
        elif keys[pygame.K_RIGHT]:
            self.stick_x +=15
            
