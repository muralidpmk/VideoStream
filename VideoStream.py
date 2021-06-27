import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Streaming")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Streaming", frame)

    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k == ord("s"):
        # SPACE pressed
        img_name = "frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
 

 

