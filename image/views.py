from PIL import Image as PIL_Image
from PIL import ImageColor
from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image


def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "index.html", {"obj": obj, "current_img_id": obj.pk})
    elif request.method == "GET":
        current_img_id = request.GET.get('current_img_id')
        wanted_color = request.GET.get('wanted_color')
        if current_img_id is None:
            form = ImageForm()
            img = Image.objects.all()
            return render(request, "index.html", {"img": img, "form": form})
        elif wanted_color and current_img_id:
            current_img = Image.objects.get(pk=current_img_id)
            black_white = pixels(current_img)
            res_color = count_color(current_img, wanted_color)
            return render(request, "index.html", {"obj": current_img, "bw": black_white, "my_color_pixels": res_color, "current_img_id": current_img_id})
        else:
            current_img = Image.objects.get(pk=current_img_id)
            black_white = pixels(current_img)
            return render(request, "index.html", {"obj": current_img, "bw": black_white, "current_img_id": current_img_id})
    else:
        form = ImageForm()
        img = Image.objects.all()
        return render(request, "index.html", {"img": img, "form": form})


def pixels(img):
    image = PIL_Image.open(img.image)
    black = 0
    white = 0
    for pixel in image.getdata():
        if pixel == (0, 0, 0):
            black += 1
        elif pixel == (255, 255, 255):
            white += 1
    if black > white:
        result = "more black"
    elif black < white:
        result = "more white"
    else:
        result = "equal black and white"
    return result


def count_color(img, color_hex):
    image = PIL_Image.open(img.image)
    color_pix = 0
    my_color = ImageColor.getcolor('#' + str(color_hex), "RGB")
    for pixel in image.getdata():
        if pixel == my_color:
            color_pix += 1
    return color_pix