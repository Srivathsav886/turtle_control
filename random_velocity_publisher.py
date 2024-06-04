# random_velocity_publisher.py

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class RandomVelocityPublisher(Node):
    def __init__(self):
        super().__init__('random_velocity_publisher')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.publish_velocity)
        self.get_logger().info("Random Velocity Publisher Node has been started")

    def publish_velocity(self):
        twist = Twist()
        twist.linear.x = random.uniform(0.5, 2.0)
        twist.angular.z = random.uniform(-1.0, 1.0)
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = RandomVelocityPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
