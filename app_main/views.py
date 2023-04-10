from django.shortcuts import render
import os
# Create your views here.


def return_gallery_pic_paths():
    dir_path = r'./static/images/velev/gallery'
    return sorted([pic_name for pic_name in os.listdir(dir_path)])


def prepare_content_per_row():
    pics = return_gallery_pic_paths()
    max_pics_per_row = 4
    pic_content = []
    temp = {}

    for idx in range(0, len(pics), 2):
        temp["images/velev/gallery/" + pics[idx]] = "images/velev/gallery/" + pics[idx+1]
        if len(temp.keys()) == max_pics_per_row:
            pic_content.append(temp.copy())
            temp.clear()

    if temp:
        pic_content.append(temp.copy())

    return pic_content


def show_main_page(request):
    return render(request, "base_one_pager.html", {
        "pictures": prepare_content_per_row()
    })

