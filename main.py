from PIL import Image

img = Image.open("Face.jpeg")
width, height = img.size
img = img.resize((int(width * 0.5), int(height * 0.5)))
resized_img = img.resize((500, 500), Image.LANCZOS)
cropped_img = img.crop((0, 0, 200, 200))
# cropped_img.show()
rotated_img = img.rotate(40)
# rotated_img.show()
rotated_img.save("rotated_img.png", "png")

r,g,b = img.split()
print(r, g, b)
histogram = img.histogram()
print(histogram)


# img = Image.merge("RGB", (r, b, g))
# img.show()
info = img.getexif()
# img.show()
print(info)

def rotate_img(imgs, iterations):
    result = []
    for i in range(iterations):
        for j in imgs:
            result.append(j.rotate(10 * i, expand=True))
    return result

result = rotate_img([img, cropped_img], 4)
# for i in range(len(result)):
#     result[i].save(f"rotated_img_{i}.png", "png")
for i in result:
    r,g,b = i.split()
    print(r, g, b)

cmyk_img = img.convert("L")
cmyk_img.show()