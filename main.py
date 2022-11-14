import cv2 
import numpy as np
import time
from twilio.rest import Client
import authKeys

start = time.time()
client = Client(authKeys.account_sid,authKeys.auth_token)

Cascade = cv2.CascadeClassifier("haarCascade_FrontalFace_default.xml")
cap = cv2.VideoCapture(2)
c=0
z=0
t=0



while True:
    ret, frames= cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = Cascade.detectMultiScale(gray,1.4,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,255,0),5)
        t=t+1
        
       
    


    cv2.imshow("Frame",frames)
    
        
    
    if(time.time()-start>z*60):
        
        
        z=z+1
        if(t>c):
            message = client.messages.create(
            body="Attention, there's someone detected in the vicinity of your security cameras. Updated Every minute",
            from_= authKeys.twilio_num,
            to= authKeys.target_num
        )
            print(message.sid)
            c=t
            
    
        
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()