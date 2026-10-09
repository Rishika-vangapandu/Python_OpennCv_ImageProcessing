import cv2
import os
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found! Check the file name.")
    exit()
height, width, channels = img.shape

print("Width:", width)
print("Height:", height)
print("Channels:", channels)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


resized = cv2.resize(img, (300, 300))


os.makedirs("output", exist_ok=True)

cv2.imwrite("output/grayscale.jpg", gray)
cv2.imwrite("output/resized.jpg", resized)

cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Resized Image", resized)

print("Image processing completed!")

cv2.waitKey(0)
cv2.destroyAllWindows()