import cv2
import mediapipe as mp
from pose_estimation_class import PoseDetector


class Test():
    # super.__init__()
    def __init__(self, mode=False, upBody=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)

    def video(self, ):

        def findPose(self, img, draw=True):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.results = self.pose.process(imgRGB)
            if self.results.pose_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

            return img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS

        def getPosition(self, img, draw=True):
            lmList = []
            if self.results.pose_landmarks:
                for id, lm in enumerate(self.results.pose_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
            return lmList

        cam = cv2.VideoCapture(1)
        while True:
            ret_val, img = cam.read()
            img, p_landmarks, p_connections = findPose(img, False)
            mp.solutions.drawing_utils.draw_landmarks(img, p_landmarks, p_connections)

            lmList = getPosition(img)
            cv2.imshow('test', img)


if __name__ == '__main__':
    test = Test()
    test.video()