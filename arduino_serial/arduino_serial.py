import serial
import io
import logging


# notes: 
# listing ports: python -m serial.tools.list_ports will print a list of available ports. It is also possible to add a regexp as first argument and the list will only include entries that matched.

# see documentation https://pythonhosted.org/pyserial/pyserial_api.html#classes
# screw with ports, id, parity, stopbits, rtscts
# device.in_waiting and .out_waiting gives num bytes in input and output buffers

class Arduino:
    def __init__(self, port='COM1'):
        self.device = serial.Serial(port, baudrate=115200, timeout=5, write_timeout=3)
        self.logger = logging.Logger()
        #self.io = io.TextIOWrapper(io.BufferedRWPair(ser, ser), encoding=None, 
        #errors=None, newline='\n', line_buffering=False, write_through=False)

    def connect(self):
        try:
            self.device.open()
        except serial.SerialException:
            self.logger.log("Error: Failed to open serial port.", print_line=True)
            return False
        return True

    def disconnect(self):
        if self.device.is_open:
            self.device.close()

    def read_without_wrapper_temp(self):
        # for testing. intending to use read()
        value = ser.readline()
        return value.decode().strip('\r\n')

    def read(self):
        value = io.readline()
        return value

    def decode(self, string):
        # for decoding data from string
        pass

    def write_command(self, args):
        sep = ' '
        while (True):
            if self.device.in_waiting:
                buffered_input = True
            else:
                buffered_input = False
                self.serial_out(sep.join(args))

                if buffered_input:
                    self.logger.log(
                        "The following buffered input was detected while entering command mode:\n",
                        print_line=True)

                response = self.device.readline().decode().rstrip()
                input_type = determine_message_type(response[0])

                if input_type == ResponseType.LOG:
                    self.logger.log(response, print_line=buffered_input)

                elif input_type == ResponseType.ERROR:
                    self.logger.log(response, print_line=True)
                    if not buffered_input:
                        return False

                elif input_type == ResponseType.RESPONSE or input_type == ResponseType.PART_RESPONSE:
                    self.logger.log(response, print_line=len(response) > 1 and self.logger.debug_mode)
                    if not input_type == ResponseType.PART_RESPONSE:
                        if buffered_input:
                            break
                        else:
                            if args[0] in ["example_command", "other_example_command"]:
                                return float(response[1:])
                            return True

                if buffered_input and not self.device.in_waiting:
                    self.logger.log("\nFinished clearing input buffer.\n", print_line=True)
                    break

    def read_loop(self):
        while(self.device.in_waiting):
            line = self.device.readline().decode().rstrip()
            self.logger.log(line)
            print(line)

    
    def serial_out(self, string):
        string += "\n"
        logger.log("Serial Out: " + string, print_line=logger.debug_mode)
        self.device.write(string_.encode())

class ResponseType(Enum):
    PART_RESPONSE = "+"
    RESPONSE = ">"
    LOG = "#"
    ERROR = "!"

def determine_message_type(char):
    for in_state in ResponseType:
        if char in in_state.value:
            return in_state
    return None

if __name__ == "__main__":
    arduino = Arduino()
    ar
