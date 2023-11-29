from PIL import Image, ImageDraw, ImageFont

def openFile(file_path):
    try:
        image = Image.open(file_path)
        return image
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

def resize(image, width, height):
    if image:
        try:
            resized_image = image.resize((width, height))
            return resized_image.copy()
        except Exception as e:
            print(f"Error resizing image: {e}")
    return None

def rotate(image, angle):
    if image:
        try:
            rotated_image = image.rotate(angle)
            return rotated_image.copy()
        except Exception as e:
            print(f"Error rotating image: {e}")
    return None

def flip(image, method):
    if image:
        try:
            flipped_image = image.transpose(method)
            return flipped_image.copy()
        except Exception as e:
            print(f"Error flipping image: {e}")
    return None


def close(images):
    for img in images:
        try:
            img.close()
        except:
            pass

def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

def save(image, path):
    try:
        conImage = image.convert("RGB")
        conImage.save(path, "JPEG")
    except Exception as e:
        print(f"Error saving image: {e}")

def write(image, text, position, fontType, size, colour):
    if image:
        try:
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(fontType, size) 
            draw.text(position, text, colour, font=font)
            return image
        except Exception as e:
            print(f"Error writing text on image: {e}")
    return None


try:
    gt3 = openFile("gt3.jpg")
    resizeGt3 = resize(gt3, 850, 450)
    sideGt3 = rotate(gt3, 90)
    flippedGt3 = flip(gt3, Image.FLIP_TOP_BOTTOM)
    gt3rs = openFile("gt3rs.jpg")
    resizeGt3rs = resize(gt3rs, 850, 450)
    mergedCars = merge(resizeGt3, resizeGt3rs)

    images = [gt3, resizeGt3, sideGt3, flippedGt3, mergedCars]

    for index, image in enumerate(images):
        path = f"image{index + 1}.jpg"
        save(image, path)

    #Merging it all together and writing a final proof.
    finalIm = write(mergedCars, "Porsche GT3", (0, 0), "DroidSans.ttf", 50, (0, 0, 0))
    finalIm = write(mergedCars, "Porsche GT3RS", (850, 0), "DroidSans.ttf", 50, (255, 255, 255))
    finalIm = write(mergedCars, "Which would you rather have?", (500, 400), "DroidSans.ttf", 50, (0, 150, 250))
    finalIm.show()
    save(finalIm, "completeIm.jpg")

except Exception as e:
    print(f"Error: {e}")

finally:
    close(images)
