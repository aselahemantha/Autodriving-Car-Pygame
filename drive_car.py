import pygame


def track_int(track):
    pygame.init()
    track = pygame.image.load(track)
    window = pygame.display.set_mode((1200, 400))
    car = pygame.image.load("images\\tesla.png")
    car = pygame.transform.scale(car, (30, 60))
    car_x = 150
    car_y = 300
    cam_dis = 25
    cam_returnx = 0
    cam_returny = 0
    direction = "up"
    drive = True
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load("images\\satisfya.mp3")
    pygame.mixer.music.play(0, 38.8)

    while drive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                drive = False

        clock.tick(60)
        cam_x = car_x + 15 + cam_returnx
        cam_y = car_y + 15 + cam_returny
        px_up = window.get_at((cam_x, cam_y - cam_dis))[0]
        px_right = window.get_at((cam_x + cam_dis, cam_y))[0]
        px_left = window.get_at((cam_x - cam_dis, cam_y))[0]
        px_down = window.get_at((cam_x, cam_y + cam_dis))[0]
        print(px_up, px_left, px_right, px_down)

        # change direction

        if px_up != 255 and px_right == 255 and direction == "up":
            direction = "right"
            cam_returnx = 30
            car = pygame.transform.rotate(car, -90)
        elif px_up != 255 and px_left == 255 and direction == "up":
            direction = "left"
            car = pygame.transform.rotate(car, 90)
        elif direction == "right" and px_down == 255 and px_right != 255:
            direction = "down"
            car = pygame.transform.rotate(car, -90)
            car_x = car_x + 30
            cam_returnx = 0
            cam_returny = 30
        elif direction == "down" and px_down != 255 and px_right == 255:
            direction = "right"
            car = pygame.transform.rotate(car, 90)
            car_y = car_y + 30
            cam_returny = 0
            cam_returnx = 30
        elif direction == "right" and px_right != 255 and px_up == 255:
            direction = "up"
            car = pygame.transform.rotate(car, 90)
            car_x = car_x + 30
            cam_returnx = 0

        # drive
        if px_up == 255 and direction == "up":
            car_y = car_y - 2
        elif direction == "right" and px_right == 255:
            car_x = car_x + 2
        elif direction == "down" and px_down == 255:
            car_y = car_y + 2

        window.blit(track, (0, 0))
        window.blit(car, (car_x, car_y))
        pygame.draw.circle(window, 'blue', (cam_x, cam_y), 5, 5)
        pygame.display.update()

