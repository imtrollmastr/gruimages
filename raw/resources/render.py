import pygame
import sys
from PIL import Image
import struct
import os

class Pixel:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getRGB(self):
        return (self.r, self.g, self.b)

    def __str__(self):
        return f"({self.r}, {self.g}, {self.b})"

def load_gru_image(gru_path):
    pixels = []
    image_code = []

    with open(gru_path, 'rb') as file:

        first_line = file.readline().decode('utf-8').strip()
        print(first_line)
        width, height = map(int, first_line.split())


        pixel_data = file.read()
        pixel_count = width * height

        if len(pixel_data) < pixel_count * 3:
            raise ValueError("Not enough pixel data in the file")


        index = 0
        for i in range(height):
            row = []
            for j in range(width):
                r, g, b = struct.unpack_from('3B', pixel_data, index)
                index += 3
                row.append(Pixel(r, g, b))
            pixels.append(row)

    return pixels, width, height

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test2.py <gru_file>")
        sys.exit(1)

    gru_path = sys.argv[1]

    print(gru_path)

    try:
        pixels, width, height = load_gru_image(gru_path)
    except Exception as e:
        print(f"Error loading gru image: {e}")
        sys.exit(1)


    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Gru Image Viewer')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        window.fill((255, 255, 255))

        for y, row in enumerate(pixels):
            for x, pixel in enumerate(row):
                image = pygame.draw.rect(window, pixel.getRGB(), (x, y, 1, 1))

        pygame.display.flip()

    pygame.quit()
    sys.exit()