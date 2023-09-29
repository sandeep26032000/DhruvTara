# pip install opencv-contrib-python
# pip install cx_freeze

import cv2
import speech2_DT

#new_text2 = speech2_DT.text2

if (speech2_DT.text2) == "yes" :
    # Opencv DNN - config and wait
    net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(320,320), scale=1/255)


    #Load class lists
    classes = []
    with open("dnn_model/classes.txt","r") as file_object:
        for class_name in file_object.readlines() :
            class_name = class_name.strip()
            classes.append(class_name)

    #print("Object list")
    #print(classes)

    #initialize camera
    cap = cv2.VideoCapture(0) #0 means computer camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    # Full HD 1920 x 1080

    def click_button(event, x,y,flags,params):
        if event == cv2.EVENT_LBUTTONDOWN :
            print(x,y)


    #create window
    cv2.namedWindow("Frame")
    cv2.setMouseCallback("Frame", click_button)

    while True:
        #Get frames
        ret, frame = cap.read()

        #object detection
        (class_ids, scores, bboxes) = model.detect(frame)
        for class_id, score, bbox in zip(class_ids, scores, bboxes):
            (x, y, w, h) = bbox
            class_name=classes[class_id]

        # mention what u want to detect only
            #new_text = speech2_DT.text
            if class_name == speech2_DT.text :
                cv2.putText(frame, class_name, (x, y-5), cv2.FONT_HERSHEY_PLAIN, 2, (200,0,5),2)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (200,0,50), 3)
            

        cv2.imshow("Frame",frame)
        key = cv2.waitKey(1)
        if key==27 :
            break

    cap.release()
    cv2.destroyAllWindows()
            
elif (speech2_DT.text2) == "no" :
    speech2_DT.SpeakText("answer is other than yes")
    
    
    

    
