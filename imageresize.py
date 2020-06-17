from PIL import Image


image = Image.open(r"D:/resize_source/portrait.tif")
new_image = image.resize((455, 562), Image.ANTIALIAS)
new_image.save("portrait_resized_final.tif")





