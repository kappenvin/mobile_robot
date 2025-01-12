import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('simple_rpi_publisher')
        self.publisher_ = self.create_publisher(String, '/pub_topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.iterator = 0

    def timer_callback(self):
        msg = String()
        msg.data = "Hello World %d" % self.iterator
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing:  "%s"' % msg.data)
        self.iterator += 10


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()