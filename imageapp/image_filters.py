from PIL import Image as PilImage, ImageFilter, ImageOps
from django.conf import settings
import os

def apply_filter(image_obj, filter_choice):
    input_path = os.path.join(settings.MEDIA_ROOT, image_obj.original_image.name)
    output_path = os.path.join(settings.MEDIA_ROOT, 'processed', f'processed_{image_obj.id}.png')

    img = PilImage.open(input_path)

    if filter_choice == 'gray':
        img = img.convert('L')

    elif filter_choice == 'sepia':
        img = img.convert("RGB")
        pixels = img.load()  # Get pixel access
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = pixels[x, y]

                # Apply sepia transformation
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                # Ensure values stay within RGB range
                pixels[x, y] = (min(tr, 255), min(tg, 255), min(tb, 255))

    elif filter_choice == 'blur':
        img = img.filter(ImageFilter.BLUR)
    
    elif filter_choice == 'poster':
        img = ImageOps.posterize(img, bits=3)  # Adjust `bits` for stronger/weaker effect

    img.save(output_path)
    image_obj.processed_image.name = f'processed/processed_{image_obj.id}.png'
    image_obj.save()