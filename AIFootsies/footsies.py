import cv2  
import numpy as np
import torch
import inference
import supervision as sv


model = inference.get_model("footsiestest/9", api_key="1PQTZXC6moROBOJGVsFK")


# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture("video_Trim.mp4")

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()
    image=cv2.resize(image, (854,480))
    results = model.infer(image)[0]
    detections = sv.Detections.from_inference(results)
    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()

        # annotate the image with our inference results
    annotated_image = bounding_box_annotator.annotate(
    scene=image, detections=detections)
    annotated_image = label_annotator.annotate(
            scene=annotated_image, detections=detections)




    # Show the image in a window
    cv2.imshow("Webcam Image",annotated_image)

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()