import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class PerceptionNode(Node):
    def __init__(self):
        super().__init__('perception_node')
        self.publisher = self.create_publisher(PoseStamped, '/object_pose', 10)
        self.timer = self.create_timer(2.0, self.publish_pose)

    def publish_pose(self):
        msg = PoseStamped()
        msg.header.frame_id = "camera_link"
        msg.pose.position.x = 0.3
        msg.pose.position.y = 0.1
        msg.pose.position.z = 0.2
        msg.pose.orientation.w = 1.0
        self.publisher.publish(msg)
        self.get_logger().info("Publishing object pose")

def main():
    rclpy.init()
    node = PerceptionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
