import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
width = 820
height = 500
window = pygame.display.set_mode((width, height))
timer = pygame.time.Clock()
player = 20, 20


def loop():
    pressed = False
    jmp_cnt = 0
    x = width // 2 - player[0] // 2
    y = height - player[0]
    up = True
    left = False
    right = False
    while True:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                return False
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_w and not pressed:
                    pressed = True
                if event.key is pygame.K_a:
                    if x > 0:
                        x -= 4
                        left = True
                if event.key is pygame.K_d:
                    if x < width - player[0]:
                        x += 4
                        right = True
        keys = pygame.key.get_pressed()
        if left:
            left = False
        else:
            if keys[pygame.K_a]:
                if x > 0:
                    x -= 4
        if right:
            right = False
        else:
            if keys[pygame.K_d]:
                if x < width - player[0]:
                    x += 4

        if pressed:
            if jmp_cnt < 50 and up:
                jmp_cnt += 4
            elif jmp_cnt >= 50 and up:
                up = False
                jmp_cnt -= 4
            elif 0 < jmp_cnt < 50 and not up:
                jmp_cnt -= 4
            else:
                pressed = False
                up = True

        window.fill(WHITE)
        pygame.draw.rect(window, BLACK, (x, y - jmp_cnt, 20, 20))
        pygame.display.update()
        timer.tick(30)


loop()
pygame.quit()
