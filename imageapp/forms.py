from django import forms
from .models import Image

FILTER_CHOICES = [
    ('gray', 'Grayscale'),
    ('sepia', 'Sepia'),
    ('blur', 'Blur'),
]

class ImageUploadForm(forms.ModelForm):
    filter = forms.ChoiceField(choices=FILTER_CHOICES)

    class Meta:
        model = Image
        fields = ['original_image', 'filter']
