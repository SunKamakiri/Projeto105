import os
import cv2

path = "Imgs"

images = []

for files in os.listdir(path):
    name, ext = os.path.splitext(files)

    if ext in ['.jpg']:
        file_name = path+"/"+files

        print(file_name)

        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
height, width,channels = frame.shape

size = (width,height)
print(size)

out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)
print("Concluído!")