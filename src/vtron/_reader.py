import struct
from pathlib import Path

from vtron import constants


class Reader:
    def __init__(self, ec_file_path: Path) -> None:
        self._ec_fd = ec_file_path.open("rb")

    def get_realtime_cpu_temp(self) -> int:
        self._ec_fd.seek(constants.CPU_REALTIME_TEMP)
        return int(self._ec_fd.read(1).hex(), 16)

    def get_realtime_cpu_fan_rpm(self) -> int:
        self._ec_fd.seek(constants.CPU_REALTIME_FAN_SPEED_RPM)
        value = self._ec_fd.read(2)
        rpm = (0 | value[0] << 8) | value[1]
        if rpm != 0:
            value = constants.FAN_RPM // rpm
        else:
            value = 0
        return value

    def get_realtime_gpu_temp(self) -> int:
        self._ec_fd.seek(constants.GPU_REALTIME_TEMP)
        return int(self._ec_fd.read(1).hex(), 16)

    # def get_fan_mode_type(self):
    #     mask = 0x03
    #     value = int(self._read_fan_mode())
    #     print(value & mask)

    def _read_fan_mode(self) -> bytes:
        self._ec_fd.seek(constants.FAN_MODE_ADDR)
        value = self._ec_fd.read(1)
        return struct.unpack("B", value)[0]

    def get_fan_mode(self) -> constants.FanMode:
        byte_value = int(self._read_fan_mode())
        return constants.FAN_MODES[byte_value]
