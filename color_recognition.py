import cv2

def get_color_name(b, g, r):
    if r < 50 and g < 50 and b < 50:
        return "Black"
    elif r > 200 and g > 200 and b > 200:
        return "White"
    elif r > 200 and g > 200 and b < 150:
        return "Yellow"
    
    if g > r and g > b:
        return "Green"
    elif r > g and r > b:
        return "Red"
    elif b > r and b > g:
        return "Blue"
    else:
        return "Other"

cap = cv2.VideoCapture("colors.mp4")  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    height, width, _ = frame.shape
    center_x = width // 2
    center_y = height // 2

    b, g, r = frame[center_y, center_x]
    color_name = get_color_name(b, g, r)

    cv2.circle(frame, (center_x, center_y), 5, (255, 255, 255), -1)
    color = (int(b), int(g), int(r))
    cv2.putText(frame, color_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Color Detection", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()