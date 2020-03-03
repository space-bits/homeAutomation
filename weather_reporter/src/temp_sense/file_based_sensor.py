class FileBasedSensor():
    """Class to read and record the value of a digital sensor such as the DS18B20.

    Reads from a filepath to return the contents of a file on disk that
    contains the data from the sensor.
    """

    def __init__(self, name, s_type, f_path):
        self.name = name
        self.s_type = s_type
        self.f_path = f_path

    def set_path(self, f_path):
        """Sets the path of the sensor on disk.

        Args:
            path (String): File location of the sensor, eg /sensors/28-XXXXXX/w1_slave
        """

        self.f_path = f_path

    def read_temp(self):
        """Reads the temperature of the sensor and returns it as a float.
        """

        raw = self.read_raw_values()
        val = self.get_value(raw)
        return val

    def read_raw_values(self):
        """Reads the raw value of the sensor and returns the lines from the file

        Returns:
            The lines from the sensor's file.
        """

        with open(self.f_path, 'r') as sensor:
            return sensor.readlines()

    def get_value(self, s_lines):
        """Gets the value of the sensor from the lines read from read_raw_values

        Args:
            s_lines (String): Array of lines that were read from read_raw_values

        Returns:
            ret_val of the sensor as the temperature as a string.
        """

        # The last 5 values in the second line is the temp
        ret_val = s_lines[1].strip()[-5:]
        # Convert from milli-celsius to celsius
        ret_val = float(ret_val) / 1000
        return ret_val
