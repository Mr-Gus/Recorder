
import cv2
import os 

#future use for object tracking
'''
trackers = ['cv2.TrackerBoosting_create()', 'cv2.TrackerMIL_Create()', 'cv2.TrackerKCF_Create()','cv2.TrackerTLD_Create()', 'cv2.TrackerMedianFlow_Create()']
def_tracker = trackers[0]
'''

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame',  cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 1800, 1000)

#captures width/height of image
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#path to save videos
path = 'Videos/Live/'
myList = os.listdir(path)
fps = 20 #frames/sec 

#example xvid/linux -- codec | where to save
writer = cv2.VideoWriter(path + f'vid{len(myList)+1}.mp4', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))


def draw_rectangle(event, x, y, flags, param):

    global pt1, pt2, top_left_clicked, bot_right_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:

        #Reset the rectangle (checks if rect below)
        if top_left_clicked & bot_right_clicked:
            pt1 = (0,0)
            pt2 = (0,0)
            top_left_clicked = False
            bot_right_clicked = False 
        
        if top_left_clicked == False:
            pt1 = (x,y)
            top_left_clicked = True

        elif bot_right_clicked == False:
            pt2 = (x,y)
            bot_right_clicked = True

##Global variables 
pt1 = (0,0)
pt2 = (0,0)

top_left_clicked = False
bot_right_clicked = False

##connect to callback
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', draw_rectangle)


def record():
    try: 

        loop= True

        while loop| cap.isOpened():

            if cap.isOpened() == False:
                print('\n\nFailed! No camera detected!..\n')
                loop= False

            ret, frame = cap.read() #read in frame


            if top_left_clicked:
                cv2.circle(frame, center=pt1, radius=5, color=(255, 255, 0), thickness=-1)

            if top_left_clicked & bot_right_clicked:
                
                cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 3)


            
            writer.write(frame)

            color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #swap color 4 matplotlib            
            cv2.imshow('frame', color)

            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break

        cap.release()
        writer.release()
        cv2.destroyAllWindows()
    
    except Exception:
       pass

record()
