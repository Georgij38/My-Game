import pygame
import sys
import random

clock = pygame.time.Clock()
FPS = 40  # Задайте бажану кількість кадрів на секунду

# Ініціалізація Pygame
pygame.init()
pygame.font.init()

next_letter_time = 0  # Час для виведення наступної літери
letter_interval = 3500  # Інтервал часу між літерами (у мілісекундах)

font = pygame.font.Font(None, 36)  # рахунок
count = 0


def display_score(count):
    score_text = font.render("Рахунок : {}".format(count), True, (255, 255, 255))
    score_rect = score_text.get_rect(topleft=(730, 10))
    window.blit(score_text, score_rect)


game_started = False



# Задаємо розміри вікна гри
window_width = 900
window_height = 360
# Створюємо вікно гри
window = pygame.display.set_mode((window_width, window_height))

# створеня кнопки
white = (255, 255, 255)
button_color = (102, 80, 230)
hovered_color = (60, 42, 159)
font = pygame.font.Font(None, 36)
start_text = font.render("Start Game", True, white)
start_text_rect = start_text.get_rect(center=(window_width // 2, 130))
start_button = pygame.Rect(start_text_rect.x - 10, start_text_rect.y - 10, start_text_rect.width + 20, start_text_rect.height + 20)

pygame.display.set_caption("My AlphabetPygame")
bg = pygame.image.load('background/fon.jpg').convert_alpha()

key_alphabet = {'а': 'alphabet/A.png', 'б': 'alphabet/B.png', 'ч': 'alphabet/Ch.png',
                'д': 'alphabet/D.png', 'е': 'alphabet/E.png', 'ф': 'alphabet/F.png',
                'г': 'alphabet/H.png', 'ґ': 'alphabet/G.png', 'и': 'alphabet/I.png', 'і': 'alphabet/Ii.png',
                'ж': 'alphabet/J.png', 'є': 'alphabet/Je.png', 'к': 'alphabet/K.png', 'х': 'alphabet/Kh.png',
                'л': 'alphabet/L.png', 'м': 'alphabet/M.png', 'н': 'alphabet/N.png',
                'о': 'alphabet/O.png', 'п': 'alphabet/P.png', 'р': 'alphabet/R.png', 'с': 'alphabet/S.png',
                'ш': 'alphabet/Sh.png', 'щ':  'alphabet/Shch.png', 'ь': 'alphabet/SoftSign.png',
                'т': 'alphabet/T.png', 'ц': 'alphabet/Ts.png', 'у': 'alphabet/U.png', 'в': 'alphabet/V.png',
                'й': 'alphabet/Y.png', 'я': 'alphabet/Ya.png', 'ї': 'alphabet/Yi.png',
                'ю': 'alphabet/Yu.png', 'з': 'alphabet/Z.png'}

letters_dict = {}
letters_rect = {}  # Список для збереження зображень та їх позицій


def creating_alphabet():  # створеня алфавіту
    random_letter = random.choice(list(key_alphabet.keys()))
    letter_image_path = key_alphabet[random_letter]
    new_letter_image = pygame.image.load(letter_image_path)
    if random_letter not in letters_dict:
        letters_dict[random_letter] = new_letter_image
        letters_rect[random_letter] = (new_letter_image.get_rect(topleft=(900, 195)))


def output_alphabet():  # вивід алфавіту
    iterator = zip(letters_dict, letters_rect)
    while game_started:
        try:
            let, el_re = next(iterator)
            window.blit(letters_dict[let], letters_rect[el_re])
            if letters_rect[el_re].left <= 0:
                letters_rect[el_re].x = 0
            else:
                letters_rect[el_re].x -= 1
        except StopIteration:
            break


def deleting_object(pressed_key):  # видалиня обекта
    del letters_dict[pressed_key]
    del letters_rect[pressed_key]

pressed_letter = None
def deleting_object_output(letter):
    global pressed_letter
    letters_rect[letter].y += 10

    if letters_rect[letter].y >= 360:
        deleting_object(letter)
        pressed_letter = None



# Головний цикл гри
while True:
    clock.tick(FPS)

    current_time = pygame.time.get_ticks()

    if current_time > next_letter_time and game_started:
        creating_alphabet()
        next_letter_time = current_time + letter_interval

    window.blit(bg, (0, 0))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:  # керуваня кнопкою
            if event.button == 1:  # ЛКМ
                if start_button.collidepoint(event.pos):
                    if not game_started:
                        game_started = True


        elif event.type == pygame.MOUSEMOTION:
            if start_button.collidepoint(event.pos):
                button_color = hovered_color
            else:
                button_color = (102, 80, 230)

        elif event.type == pygame.KEYDOWN:
            pressed_key = event.unicode.lower()  # Отримати натискану клавішу (в нижньому регістрі)

            if pressed_key in letters_dict and pressed_letter == None:  # видаленя з єкрану
                pressed_letter = pressed_key
                count += 1

    if not game_started:  # Тільки відображаємо кнопку, якщо її не було натиснуто
        pygame.draw.rect(window, button_color, start_button)
        window.blit(start_text, start_text_rect)

    if pressed_letter is not None:
        deleting_object_output(pressed_letter)

    output_alphabet()
    display_score(count)
    pygame.display.update()
