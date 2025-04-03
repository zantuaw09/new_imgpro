from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import Image
from .image_filters import apply_filter

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save(commit=False)
            filter_choice = form.cleaned_data['filter']
            image_obj.filter_applied = filter_choice
            image_obj.save()
            apply_filter(image_obj, filter_choice)
            return redirect('result', image_id=image_obj.id)
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def result(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'result.html', {'image': image})
