import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна (необязательно, но полезно для визуализации)
screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption("Blaster Sound Demo")

# Загрузка звука выстрела
sound_shoot = pygame.mixer.Sound('sounds/'+"shoot.wav")

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Обработка нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Клавиша 1
                sound_shoot.play()  # Воспроизведение звука
    


# Завершение работы
pygame.quit()
sys.exit()