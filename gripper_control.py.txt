import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GripperController(Node):
    def __init__(self):
        super().__init__('gripper_controller')

        self.subscription = self.create_subscription(
            String,
            '/gripper_command',
            self.command_callback,
            10
        )

        self.get_logger().info("Gripper controller started")

    def command_callback(self, msg):
        command = msg.data

        if command == "open":
            self.open_gripper()
        elif command == "close":
            self.close_gripper()

    def open_gripper(self):
        self.get_logger().info("Opening gripper...")

    def close_gripper(self):
        self.get_logger().info("Closing gripper...")

def main():
    rclpy.init()
    node = GripperController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
