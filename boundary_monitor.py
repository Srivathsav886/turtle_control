# boundary_monitor.py

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import math

class BoundaryMonitor(Node):
    def __init__(self):
        super().__init__('boundary_monitor')
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'turtle_boundary_warning', 10)
        self.cmd_vel_publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.near_boundary = False
        self.get_logger().info("Boundary Monitor Node has been started")

    def pose_callback(self, msg):
        boundary_threshold = 1.0
        if (msg.x < boundary_threshold or msg.x > 11.0 - boundary_threshold or
            msg.y < boundary_threshold or msg.y > 11.0 - boundary_threshold):
            if not self.near_boundary:
                warning_msg = String()
                warning_msg.data = "Turtle is near boundary"
                self.publisher_.publish(warning_msg)
                self.near_boundary = True
                self.make_turn(msg.theta)
        else:
            self.near_boundary = False

    def make_turn(self, current_theta):
        turn_angle = math.radians(120)
        twist = Twist()
        twist.linear.x = 2.0
        twist.angular.z = turn_angle
        self.cmd_vel_publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = BoundaryMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
