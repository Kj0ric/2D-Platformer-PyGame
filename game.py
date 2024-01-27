import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        # Name the screen
        pygame.display.set_caption('Ninja Game')
        # Initialize the screen
        self.screen = pygame.display.set_mode((640, 480))

        # Initialize clock object to track time
        self.clock = pygame.time.Clock()
        
        # To avoid perform issues, load all necessary resources before the game loop starts, and then just draw them during the loop
        # Create img attribute holding a pygame Surface object for the Game object self 
        # Prefer PNG, since its lossless
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img_pos = [160, 260]
        self.img.set_colorkey((0,0,0))
        
        self.movement = [False, False]
        
        # A random rectangle area on the screen
        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        # All in one loop
        while True:
            # To get rid of trails, fill the screen first
            self.screen.fill((14, 219, 248)) 
            
            # Rect object to represent the img hitbox
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())                      
            
            # Detect if the img_r is colliding with the collision area
            if img_r.colliderect(self.collision_area):
                # Draw collision_area Rect object onto the screen with a blue color
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)
            
            # Move the image up or down               
            self.img_pos[1] += (self.movement[1] - self.movement[0])*5                   
            # Render the image ON the screen after collision detection
            self.screen.blit(self.img, self.img_pos) 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # When a key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True 
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                # When a key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                
            pygame.display.update()
            self.clock.tick(60) # Fix to 60fps
    
Game().run()