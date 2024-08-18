import os
path = "C:\\Users\\pilow\Desktop\\image.py"

# if os.path.exists(path):
#     print('that locations exists!')
#
# else:
#     print("That location doesn't exist!")


if os.path.isfile(path):
    with open(path, "r") as file:
        content = file.read()
        print(content)

else:
    print(f"The file {path} does not exist.")