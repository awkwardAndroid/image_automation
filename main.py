import functions
import sys, os


INPUT_FOLDER = "in/"
def main():
    item_list = get_image_list()
    if item_list == None:
        return
    
    for item in item_list:
        print(item)

    print("")
    while True:
        print("Convert all images to jpeg?(y/n)")
        u_input = input(">")
        u_input = u_input.lower()
        if u_input == "y":
            for item in item_list:
                functions.png_to_jpeg(item)
            
            print("Convertions complete. Exiting...")
            return
        else:
            print("Exiting...")
            return
        


def get_image_list():
    item_array = []

    for item in os.listdir(INPUT_FOLDER):
        item_array.append(os.path.join(INPUT_FOLDER, item))

    # If the length of the array is smaller than one, it means its empty
    if len(item_array) < 1:
        print("The input folder is empty...")
        return None
    
    return item_array


if __name__ == "__main__":
    main()