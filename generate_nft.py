#!/usr/bin/env python3
import random
from PIL import Image, ImageDraw

base_folder = "/Users/herobinge/Desktop/generatenft"
backgrounds = ["background1.png", "background2.png", "background3.png", "background4.png", "background5.png", "background6.png", "background7.png"]
background_weights = [1, 1, 1, 1, 1, 1, 3]  # 背景图像的权重
eyes = ["eyes1.png", "eyes2.png", "eyes3.png"]
eyes_weights = [1, 1, 1]  # 眼睛图像的权重
mouths = ["mouth1.png", "mouth2.png", "mouth3.png"]
mouths_weights = [1, 1, 1]  # 嘴巴图像的权重
hats = ["hat1.png", "hat2.png"]
hats_weights = [1, 1]  # 帽子图像的权重
bodies = ["body1.png", "body2.png", "body3.png", "body4.png", "body5.png", "body6.png", "body7.png", "body8.png", "body9.png", "body10.png"]
bodies_weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 身体图像的权重

image_width = 400
image_height = 400

def generate_nft_image():
    background = random.choices(backgrounds, weights=background_weights)[0]
    eye = random.choices(eyes, weights=eyes_weights)[0]
    mouth = random.choices(mouths, weights=mouths_weights)[0]
    hat = random.choices(hats, weights=hats_weights)[0] if random.random() < 0.5 else None
    body = random.choices(bodies, weights=bodies_weights)[0]

    background_image = Image.open(f"{base_folder}/backgrounds/{background}").convert("RGBA")
    eye_image = Image.open(f"{base_folder}/eyes/{eye}").convert("RGBA")
    mouth_image = Image.open(f"{base_folder}/mouths/{mouth}").convert("RGBA")
    hat_image = Image.open(f"{base_folder}/hats/{hat}").convert("RGBA") if hat else None
    body_image = Image.open(f"{base_folder}/bodies/{body}").convert("RGBA") if body else None

    image = Image.new("RGBA", (image_width, image_height))
    image.alpha_composite(background_image)
    if body_image:
        image.alpha_composite(body_image)
    image.alpha_composite(eye_image)
    image.alpha_composite(mouth_image)
    if hat_image:
        image.alpha_composite(hat_image)

    nft_number = random.randint(1, 100000)
    nft_name = f"shitnftBRC20 #{nft_number}"

    image.save(f"imagenft/{nft_name}.png")

# 生成1000个NFT图像
for _ in range(1000):
    generate_nft_image()
