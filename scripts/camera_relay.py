#!/usr/bin/env python
# -*- coding: utf-8 -*-


import rospy
from sensor_msgs.msg import Image, CameraInfo


rospy.init_node("camera_relay")
ns = rospy.get_param("~out_ns")
image_pub = rospy.Publisher(ns+"/image_raw", Image, queue_size=10)
info_pub = rospy.Publisher(ns+"/camera_info", CameraInfo, queue_size=10)

def image_cb(msg):
    msg.header.frame_id = ns
    image_pub.publish(msg)
    
def info_cb(msg):
    msg.header.frame_id = ns
    info_pub.publish(msg)
    
sub = [
    rospy.Subscriber(rospy.get_param("~img_in"), Image, image_cb),
    rospy.Subscriber(rospy.get_param("~info_in"), CameraInfo, info_cb)
]

rospy.spin()
