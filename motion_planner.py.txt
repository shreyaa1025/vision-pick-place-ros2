import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class MotionPlanner(Node):
    def __init__(self):
        super().__init__('motion_planner')
        self.subscription = self.create_subscription(
            PoseStamped,
            '/object_pose',
            self.callback,
            10)

    def callback(self, msg):
        self.get_logger().info("Planning pick and place motion")

def main():
    rclpy.init()
    node = MotionPlanner()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
