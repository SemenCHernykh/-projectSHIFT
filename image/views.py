import PIL
from django.shortcuts import render,redirect
from .form import ImageForm
from .models import Image

def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "index.html", {"obj": obj})
    else:
        form = ImageForm()
        img = Image.objects.all()
    return render(request,"index.html", {"img": img, "form": form})

def pixels(request):
    if request.GET.get('action'):
        image = Image.open('img-thumbnail')  # Открываем изображение
        width = image.size[0]  # Определяем ширину
        height = image.size[1]  # Определяем высоту
        pix = image.load()  # Выгружаем значения пикселей
        black = 0
        white = 0
        p = 0
        for x in range(width):
            for y in range(height):
                p = p + 1
                if y == (0, 0, 0):
                    black += 1
                elif y == (255, 255, 255):
                    white += 1
        result=0
        if black>white:
            result="more black"
        else:
            result="more white"

    return render(request,"index.html", {'bw':result})
def pixels(request):
    image = Image.open('img-thumbnail')  # Открываем изображение
    width = image.size[0]  # Определяем ширину
    height = image.size[1]  # Определяем высоту
    pix = image.load()  # Выгружаем значения пикселей
    black = 0
    white = 0
    p = 0
    for x in range(width):
        for y in range(height):
            p = p + 1
            if y == (0, 0, 0):
                black += 1
            elif y == (255, 255, 255):
                white += 1
    result=0
    if black>white:
        result="more black"
    else:
        result="more white"

    return render(request,"index.html", {'bw':"result"})