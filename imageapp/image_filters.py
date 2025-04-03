from PIL import Image as PilImage, ImageFilter
from django.conf import settings
import os

def apply_filter(image_obj, filter_choice):
    input_path = os.path.join(settings.MEDIA_ROOT, image_obj.original_image.name)
    output_path = os.path.join(settings.MEDIA_ROOT, 'processed', f'processed_{image_obj.id}.png')

    img = PilImage.open(input_path)

    if filter_choice == 'gray':
        img = img.convert('L')
    elif filter_choice == 'sepia':
        sepia = []
        r, g, b = (239, 224, 185)
        for i in range(255):
            sepia.append(i*r//255)
            sepia.append(i*g//255)
            sepia.append(i*b//255)
        img = img.convert("L")
        img.putpalette(sepia, "RGB")
        img = img.convert("RGB")
    elif filter_choice == 'blur':
        img = img.filter(ImageFilter.BLUR)

    img.save(output_path)
    image_obj.processed_image.name = f'processed/processed_{image_obj.id}.png'
    image_obj.save()