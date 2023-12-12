import pygame
window = pygame.display.set_mode((1000,600))
window.fill((0,100,0))
image = pygame.image.load("./test.png")
window.blit(image, (1,1))
done = False
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
x = 1
y = 1
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            window.fill((0,100,0))
            image = pygame.transform.rotate(image,45)
            if(x == 1):
                x, y = 1-int(249 / 2**0.5),1-int(249 / 2**0.5)
            else:
                x,y =1,1
            window.blit(image, (x,y))
            pygame.display.flip()