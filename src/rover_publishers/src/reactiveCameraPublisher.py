#!/usr/bin/env python
import rospy, cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import UInt8MultiArray


bridge = CvBridge()
newPub = rospy.Publisher("reactiveCameraNetworkNodeSubsriber", UInt8MultiArray, queue_size=5)

def image_callback(msg):

    sendData = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
    sendData = cv2.cvtColor(sendData, cv2.COLOR_BGR2GRAY)
    sendData = cv2.pyrDown(sendData)

    __, sendData = cv2.imencode('.jpg', sendData, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    messagePayload = UInt8MultiArray()
    messagePayload.data = sendData.tobytes()
    newPub.publish(messagePayload)


rospy.init_node("image_subscriber")
rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
rospy.spin()
