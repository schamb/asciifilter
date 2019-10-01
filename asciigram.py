import filters

def main():
    filename = input("Enter the image name you want to edit: ")

    img = filters.load_img(filename)

    newImage = filters.asci(img)
    # filters.show_img(newImage)






# -------------------- #
#    DO NOT TOUCH      #
# -------------------- #
if __name__ == "__main__":
    main()
