import cv2
# image = cv2.imread("img.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("Nepal", image)
# cv2.waitKey(0)

src = cv2.imread("img.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("Nepal", src)
scale_percent = 50
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[1] * scale_percent / 100)
output = cv2.resize(src,(width,height))
cv2.imwrite("NewImageNepal.jpg",output)
cv2.waitKey(0)