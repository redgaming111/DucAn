import numpy as np
import cv2 as cv

# Biến toàn cục
drawing = False
mode = True  # True: chữ nhật, False: vòng tròn
ix, iy = -1, -1
rect_pts = None
img = np.ones((512,512,3), np.uint8) * 255
img_temp = img.copy()

# Vẽ hình
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode, img, img_temp, rect_pts
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        img_temp = img.copy()
    elif event == cv.EVENT_MOUSEMOVE and drawing:
        img = img_temp.copy()
        if mode:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        x1, y1 = ix, iy
        x2, y2 = x, y
        if mode:
            cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            rect_pts = np.array([[x1,y1],[x2,y1],[x2,y2],[x1,y2]], dtype=float)


# Vẽ polygon từ các điểm
def draw_polygon(img, pts, color):
    pts = pts.astype(int)
    for i in range(len(pts)):
        cv.line(img, tuple(pts[i]), tuple(pts[(i+1)%len(pts)]), color, 2)

# Biến đổi
def transform(pts, dx, dy, angle, sx, sy):
    if pts is None:
        return None
    # Dịch
    pts = pts + np.array([dx, dy])
    # Xoay
    theta = np.radians(angle)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    center = pts.mean(axis=0)
    pts = (pts - center) @ R.T + center
    # Scale
    S = np.array([[sx,0],[0,sy]])
    pts = (pts - center) @ S.T + center
    return pts

# Callback trackbar
def update(x):
    global img
    if rect_pts is not None:
        dx = cv.getTrackbarPos('Dx','image') - 256
        dy = cv.getTrackbarPos('Dy','image') - 256
        angle = cv.getTrackbarPos('Angle','image') - 180
        sx = cv.getTrackbarPos('ScaleX','image') / 100
        sy = cv.getTrackbarPos('ScaleY','image') / 100
        img = img_temp.copy()
        new_pts = transform(rect_pts, dx, dy, angle, sx, sy)
        draw_polygon(img, new_pts, (255,0,0))
        draw_polygon(img, new_pts, (0,255,0))


cv.namedWindow('image')
cv.setMouseCallback('image', draw_shape)

# Trackbar
cv.createTrackbar('Dx','image',256,512,update)      # -256 -> 256
cv.createTrackbar('Dy','image',256,512,update)      # -256 -> 256
cv.createTrackbar('Angle','image',0,180,update)   # -180 -> 180
cv.createTrackbar('ScaleX','image',100,300,update)  # 0 -> 3.0
cv.createTrackbar('ScaleY','image',100,300,update)  # 0 -> 3.0

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('c'):
        img = np.ones((512,512,3), np.uint8) * 255
        img_temp = img.copy()
        rect_pts = None
    elif k == 27:
        break

cv.destroyAllWindows()
