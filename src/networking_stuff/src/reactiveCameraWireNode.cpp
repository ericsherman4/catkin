#include <ros/ros.h>
#include "transmitSubscriber.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "reactiveCameraNetworkNode");
    TransmitSubscriber newNode(WIFI_REACTIVE_CAMERA_PORT, CLIENT_IP, IMAGE_BUFFER_SIZE, "reactiveCameraNetworkNode", REACTIVE_CAMERA_DEBUG, "reactiveCameraNetworkNodeSubsriber", REACTIVE_CAMERA_PORT_PRIORITY);
    return 0;
}