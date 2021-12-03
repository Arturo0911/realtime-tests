

from typing import Any, Tuple, Dict
from serial import Serial
import time
import re



class Arduino:
    """Arduino connection"""

    def __init__(self):
        # self.port = "COM4"
        self.port = "/dev/ttyACM0"
        self.baud_rate = 9600
        self.timeout = 2

    def _connection(self) -> Any:
        serial_conn = Serial(port=self.port,
                             baudrate=self.baud_rate,
                             timeout=self.timeout)
        return serial_conn

    def read_lines(self, readers=20) -> Tuple[Dict[int, Any], list]:
        conn = self._connection()
        stack_data = list()
        object_data = dict()
        counter = 1
        while readers > 1:
            data = conn.readline()
            convertion = str(data.decode("ascii", errors="replace"))
            stack_data.append(convertion)
            object_data[counter] = data
            counter += 1
            readers -= 1
            time.sleep(0.05)
            # print("Stack data => {} ".format(stack_data))
            # print("Dictionary data => {}".format(object_data))
        
        """position = 0
        while position  < len(stack_data):
            if stack_data[position] == "":
                stack_data.pop(position)
            else:
                position +=1
        """

        register = [re.search(r'\d{1,5}', x).group() for x in stack_data]
        return object_data, register


def main():
    
    arduino = Arduino()
    _,stack = arduino.read_lines()
    print(stack)


if __name__ == "__main__":
    main()
