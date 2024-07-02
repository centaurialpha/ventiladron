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
        rpm = ((0 | value[0] << 8 ) | value[1])
        if rpm != 0:
            value = constants.FAN_RPM / rpm
        else:
            value = 0
        return value
