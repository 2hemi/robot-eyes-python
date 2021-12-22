import pygame
from itertools import cycle

TILE_SIZE = 32
SCREEN_SIZE = pygame.Rect((0, 0, 21*TILE_SIZE, 17*TILE_SIZE))


class Expression(pygame.sprite.Sprite):
    def __init__(self, data):
        super().__init__()
        self.image = pygame.Surface((len(data[0]), len(data)))
        x = y = 0
        for row in data:
            for col in row:
                if col == "O" or col ==".":
                    self.image.set_at((x, y), pygame.Color('dodgerblue'))
                x += 1
            y += 1
            x = 0
        self.image = pygame.transform.scale(self.image, (TILE_SIZE*len(data[0]), TILE_SIZE*len(data)))
        self.rect = self.image.get_rect()

REGULAR = Expression([
"                     ",
"                     ",
"                     ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OO  OO   OO  OO   ",
"   OO  OO   OO  OO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"                     ",
"                     ",
"                     ",
])

LEFT = Expression([
"                     ",
"                     ",
"                     ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   O  OOO   O  OOO   ",
"   O  OOO   O  OOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"                     ",
"                     ",
"                     ",
])

RIGHT = Expression([
"                     ",
"                     ",
"                     ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOO  O   OOO  O   ",
"   OOO  O   OOO  O   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"                     ",
"                     ",
"                     ",
])

QUESTION = Expression([
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"   O             O   ",
"   OO           OO   ",
"   OOO         OOO   ",
"   OOOO       OOOO   ",
"   OOOOO     OOOOO   ",
"   OOOOOO   OOOOOO   ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
])

BLINK = Expression([
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"   OOOOOO   OOOOOO   ",
"   OOOOOO   OOOOOO   ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
])

HAPPY = Expression([
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"                     ",
"   OOOOOO   OOOOOO   ",
"   O    O   O    O   ",
"   O    O   O    O   ",
"   O    O   O    O   ",
"   O    O   O    O   ",
"   O    O   O    O   ",
"                     ",
"                     ",
"                     ",
])
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    timer = pygame.time.Clock()
    expressions = cycle([REGULAR,LEFT,LEFT,RIGHT,RIGHT,BLINK,REGULAR,REGULAR,BLINK,REGULAR])
    current = next(expressions)
    pygame.time.set_timer(pygame.USEREVENT, 200)

    while True:

        for e in pygame.event.get():
            if e.type == pygame.QUIT: 
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return
            if e.type == pygame.USEREVENT:
                current = next(expressions)

        screen.fill((0, 0, 0))
        screen.blit(current.image, current.rect)
        timer.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    main()
