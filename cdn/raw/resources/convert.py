from PIL import Image
import struct
import sys
import os
import base64

start_path = ''
end_path = ''
def convert_png_to_gru(png_path, gru_path):
    os.system("mkdir " + "images/" + gru_path)

    image = Image.open(png_path)
    width, height = image.size
    pixels = list(image.getdata())

    print("Enter a secure password:")
    password = input("> ")
    encrypted_password = base64.b64encode(bytes(password.encode('utf-8')))
    with open("images/" + gru_path + "/" + gru_path + "_info.txt", "wb") as file:
        file.write(encrypted_password)

    with open("images/" + gru_path + "/" + gru_path + ".gru", 'wb') as file:

        file.write(f"{width} {height}\n".encode('utf-8'))


        pixel_data = []
        for pixel in pixels:
            r, g, b = pixel[:3]
            pixel_data.append((r, g, b))

        for r, g, b in pixel_data:
            file.write(struct.pack('3B', r, g, b))

    try:
        with open("resources/cache.txt", "rb") as cache:
            reward_count = str(cache.read())
            reward_count = reward_count.split("b'")[1]
            reward_count = reward_count.split("'")[0]
            reward_count = int(reward_count)
            new_reward_count = reward_count + 1
            new_reward_count = str(new_reward_count)
            print("Rewards: " + str(new_reward_count))
        with open("resources/cache.txt", "wb") as cache:
            cache.write(bytes(new_reward_count.encode('utf-8')))
    except:
        print("Join GRU Members to view your rewards!")



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("error: bad arguments")
        sys.exit(1)
    else:
        start_path = sys.argv[1]
        gru_path = sys.argv[2]
convert_png_to_gru(start_path, gru_path)
print("Successfully converted image.")
os.system("python3 main.py")
