import pygame
import random
import time

pygame.init()

WIDTH = 420
HEIGHT = 420

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MITA AI")

clock = pygame.time.Clock()

state = "idle"


def set_state(new_state):
    global state
    state = new_state


def load_image(path):

    try:
        img = pygame.image.load(path)
        img = pygame.transform.scale(img,(380,380))
        return img

    except:
        surface = pygame.Surface((380,380))
        surface.fill((100,150,200))
        return surface


idle_img = load_image("assets/idle.png")
blink_img = load_image("assets/blink.png")
talk1_img = load_image("assets/talk1.png")
talk2_img = load_image("assets/talk2.png")
think_img = load_image("assets/think.png")

last_blink = time.time()
is_blinking = False

talk_frame = 0
talk_timer = 0


def draw_avatar():

    global last_blink
    global is_blinking
    global talk_frame
    global talk_timer

    now = time.time()

    if now - last_blink > random.uniform(3,6):

        is_blinking = True
        last_blink = now

    if is_blinking and now - last_blink > 0.15:
        is_blinking = False


    if state == "talking":

        talk_timer += 1

        if talk_timer > 8:
            talk_timer = 0
            talk_frame = 1 - talk_frame

        if talk_frame == 0:
            img = talk1_img
        else:
            img = talk2_img

    elif state == "thinking":

        img = think_img

    else:

        if is_blinking:
            img = blink_img
        else:
            img = idle_img


    rect = img.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(img, rect)


def ui_loop():

    running = True

    while running:

        screen.fill((30,30,40))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        draw_avatar()

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
