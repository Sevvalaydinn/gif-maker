import imageio
from PIL import Image, ImageEnhance
import os

image_path = "cat.jpg"  #
output_gif = "animated_cat.gif"

image = Image.open(image_path)

frames = []
for i in range(20):
    zoom_factor = 1 + (i % 10) * 0.02
    width, height = image.size
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)

    frame = image.resize((new_width, new_height), Image.LANCZOS)
    left = (new_width - width) // 2
    top = (new_height - height) // 2
    frame = frame.crop((left, top, left + width, top + height))

    enhancer = ImageEnhance.Brightness(frame)
    frame = enhancer.enhance(0.8 + (i % 10) * 0.02)

    frames.append(frame)

frames[0].save(output_gif, save_all=True, append_images=frames[1:], duration=50, loop=0)

print(f"✅ Gif Oluşturuldu: {output_gif}")
