# # file to set up pillow code

# def copy_image(your_image):
#    my_src = Image.open(your_image)
#    w,h = my_src.width, my_src.height
#    sound_im = Image.new('RGB', (w,h))

#    target_x = 0
#    for source_x in range(w):
#        target_y = 0
#        for source_y in range(h):
#            p = my_src.getpixel((source_x, source_y))
#            sound_im.putpixel((target_x, target_y), p)
#            target_y += 1
#        target_x += 1

#    sound_im.show()

from PIL import Image 

def build_image(sound_list):
    # im = Image.new('RGB', (25, 25)) # create a new image 

    w = 25
    h =  25
    sound_im = Image.new('RGB', (w,h))

    target_x = 0
    for source_x in range(w):
        target_y = 0
        for source_y in range(h):
            #hertz value from list
            sound_im.putpixel((target_x, target_y), (sound_list[source_x], sound_list[source_y], sou))
            target_y += 1
        target_x += 1

    sound_im.show()

sound_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]
build_image(sound_list)
