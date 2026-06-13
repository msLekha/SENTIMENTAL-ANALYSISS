import cv2

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

# Open camera
cap = cv2.VideoCapture(0)

print("Camera started... Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    # Flip camera
    frame = cv2.flip(frame, 1)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(80, 80)
    )

    sentiment = "No Face Detected"

    for (x, y, w, h) in faces:

        # Draw face rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        # Demo sentiment logic
        face_size = w * h

        if face_size > 30000:
            sentiment = "Positive 😊"
        elif face_size > 18000:
            sentiment = "Neutral 😐"
        else:
            sentiment = "Negative 😔"

        break

    # Show sentiment
    cv2.putText(
        frame,
        sentiment,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Live Sentiment Analysis",
        frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()