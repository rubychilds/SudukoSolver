from OneStrokeGesture import OneStrokeGesture
import sys, pygame

pygame.init()

screen = pygame.display.set_mode((320, 240))
g = OneStrokeGesture()
paths = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            g.PenDown(event.pos)
            paths.append(g.path.points)
        if event.type == pygame.MOUSEMOTION:
            if g.down:
                g.PenTo(event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            print g.PenUp(event.pos)

    screen.fill([255, 255, 255])
    [pygame.draw.aalines(screen, [0, 0, 0], False, p, 1) for p in paths if len(p) > 1]
    pygame.display.flip()