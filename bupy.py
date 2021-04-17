import pygame

## заставляем работать
pygame.init()

w, h = 500, 500
x, y = w//2, h//2

## создание окна. обязательно двойные скобки. сет мод для установления разрешения
# окно в качестве переменной
screen = pygame.display.set_mode((w,h))

# от нуля до 255 цвет окна
# все 255 - белый
# все 0 - черный
color = (0, 0, 0)
newcolor = (255, 255, 255)
running = True

fps = pygame.time.Clock()

# все действие должно быть в главном цикле while
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(color)

    # нарисовать фигуру(окно, цвет, координаты, радиус, толщина (необязательно последнее))
    # pygame.draw.circle(screen, newcolor, (250, 250), 200, 5)

    # # rect - прямоугольник
    # pygame.draw.rect(screen, newcolor, (250, 250, 210, 210), 5)

    # # линия - lines (если больше 2 точек), если 2 точки, то line (окно, цвет, True, (точка 1, точка 2, точка 3 и далее сколько угодно) если больше двух точек, то в доп скобках)
    # pygame.draw.lines(screen, newcolor, True, ((100, 120), (120, 200), (50, 90)), 10)

    # # если нужна гладкая линия, то draw.aaline(s)
    
    # # polygon - заполненный контур, нужно выбрать линии
    # pygame.draw.polygon(screen, (30, 46, 250), [(100, 200), (120, 400), (50, 50), (100,100), (240, 300)], 5)
    

    # ellipse - овал
    
    # for i in range(10):
    #     pygame.draw.ellipse(screen, (255, 255, 255), (i * 500//10, 0, 500 - i * 30, 500), 1)
        
    #     pygame.draw.ellipse(screen, (255, 255, 255), (i * 500//10, 0, 500, 500 - i * 30), 1)
    
    ## перемещение с клавиатуры:
    keys = pygame.key.get_pressed()
    
    # движение вниз
    if keys[pygame.K_DOWN]:
        y += 1
        if y > h:
            y = 0
    # движение вверх
    if keys[pygame.K_UP]:
        y -= 1
        if y < 0:
            y = h
    # движение влево
    if keys[pygame.K_LEFT]:
        x -= 1
        if x < 0:
            x = w
    # движение вправо
    if keys[pygame.K_RIGHT]:
        x += 1
        if x > w:
            x = 0

    if x < 150 or x > 350:
        newcolor = (250, 44, 100)
        fps.tick(1000)
    elif y > 350 or y < 150:
        newcolor = (250, 44, 100)
        fps.tick(1000)
    else:
        newcolor = (255, 255, 255)
        fps.tick(500)

    if not keys[pygame.K_DOWN] and not keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        while x != 250:
            
            if x > 250:
                x -= 1
            if x < 250:
                x += 1
        while y != 250:
            
            if y > 250:
                y -= 1
            if y < 250:
                y += 1


    # беспрерывное движение
    # x += 10
    # if x > w:
    #     x = 0

    pygame.draw.rect(screen, newcolor, (150, 150, 200, 200), 5)
    pygame.draw.circle(screen, newcolor, (x, y), 25)
   
    # контроль скорости, переменная фпс в начале. чем > тем быстрее
    fps.tick(500)

    # нужно постоянно обновлять окно!!! ОБЯЗАТЕЛЬНО!!!!
    pygame.display.update()

    # назвать окно:
    pygame.display.set_caption('проект')