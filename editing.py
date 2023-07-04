import cv2

import cv2
import os

image_folder = 'path_to_images_folder'  # Folder containing the images
video_name = 'output_video.mp4'  # Name of the output video file
video_fps = 24  # Frames per second of the output video

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort()

image_path = os.path.join(image_folder, images[0])
img = cv2.imread(image_path)
height, width, _ = img.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*"mp4v"), video_fps, (width, height))

for image in images:
    image_path = os.path.join(image_folder, image)
    img = cv2.imread(image_path)
    video.write(img)

video.release()
cv2.destroyAllWindows()
