import boto3

myec2 = boto3.resource('ec2')

def launchOS():
    response = myec2.create_instances(
        ImageId = 'ami-0b9ecf71fe947bbdd',
        InstanceType='t2.micro',
        MaxCount = 1,
        MinCount = 1
)
    
import cv2
cp = cv2.VideoCapture(0)

from cvzone.HandTrackingModule import HandDetector
detector = HandDetector()

while True:
    status , photo = cp.read()
    cv2.imshow("my photo", photo)
    if cv2.waitKey(50) == 13:
        break

    handphoto = detector.findHands(photo , draw=False)

    if handphoto:
        lmlist = handphoto[0]
        fingerstatus = detector.fingersUp(lmlist)

        if fingerstatus == [1,1,1,1,1]:
            print("all ups")
            launchOS()
            launchOS()
            launchOS()
            launchOS()
            launchOS()

        elif fingerstatus == [0,1,0,0,0]:
            print("index finger")
            launchOS()

        elif fingerstatus == [0,1,1,0,0]:
            print("index and middle finger")
            launchOS()
            launchOS()

        elif fingerstatus == [0,1,1,1,0]:
            print("index, middle and ring finger")
            launchOS()
            launchOS()
            launchOS()

        elif fingerstatus == [0,1,1,1,1]:
            print("index, middle, ring finger and little finger")
            launchOS()
            launchOS()
            launchOS()
            launchOS()

        else :
            print("No fingers found!!")

cv2.destroyAllWindows()
cp.release()