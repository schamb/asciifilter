from PIL import Image

#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    imgObject = Image.open(filename)
    return imgObject

#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(imgObject):
    imgObject.show()


#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgObject, newImageName): #newImageName = name given to image
    imgObject.save(newImageName, "jpeg")
    show_img(imgObject)


#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(imgObject):
    imgHeight = imgObject.size
    numPixels = imgObject.getdata()
    newPixelList = []
    x = 0
    for i in numPixels:
        pixel = numPixels[x]
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            newPixelList.append((0, 51, 76))
        elif intensity >= 182 and intensity <= 364:
            newPixelList.append((217, 26, 33))
        elif intensity > 364 and intensity <= 546:
            newPixelList.append((112, 150, 158))
        elif intensity > 546:
            newPixelList.append((252, 227, 166))
        x += 1
    newImage = Image.new("RGB", imgHeight)
    newImage.putdata(newPixelList)
    return newImage

def orange(imgObject):
    imgHeight = imgObject.size
    numPixels = imgObject.getdata()
    newPixelList = []
    x = 0
    for i in numPixels:
        pixel = numPixels[x]
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            newPixelList.append((206, 138, 20))
        elif intensity >= 182 and intensity <= 364:
            newPixelList.append((247, 156, 0))
        elif intensity > 364 and intensity <= 546:
            newPixelList.append((239, 173, 59))
        elif intensity > 546:
            newPixelList.append((237, 205, 151))
        x += 1
    newImage = Image.new("RGB", imgHeight)
    newImage.putdata(newPixelList)
    return newImage
