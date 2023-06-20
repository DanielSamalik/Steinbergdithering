from PIL import Image

def floyd_steinberg(image):
    width, height = image.size
    image = image.convert('1')
    pixels = image.load()
    for y in range(height):
        for x in range(width):
            stary_pixel = pixels[x, y]
            novy_pixel = 0 if stary_pixel < 128 else 255
            pixels[x, y] = novy_pixel
            error = stary_pixel - novy_pixel
            if x + 1 < width:
                pixels[x + 1, y] = pixels[x + 1, y] + (error * 7) // 16
            if x > 0 and y + 1 < height:
                pixels[x - 1, y + 1] = pixels[x - 1, y + 1] + (error * 3) // 16
            if y + 1 < height:
                pixels[x, y + 1] = pixels[x, y + 1] + (error * 5) // 16
            if x + 1 < width and y + 1 < height:
                pixels[x + 1, y + 1] = pixels[x + 1, y + 1] + (error * 1) // 16
    return image