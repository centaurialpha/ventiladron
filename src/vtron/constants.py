import enum
from pathlib import Path

EC_FILE_PATH = Path("/sys/kernel/debug/ec/ec0/io")

# Cooler boost
COOLER_BOOST_ADDR = 0x98
COOLER_BOOST_ON = 0x80
COOLER_BOOST_OFF = 0x00

FAN_MODE_ADDR = 0xF4

CPU_REALTIME_TEMP = 0x68
CPU_REALTIME_FAN_SPEED_RPM = 0xCC

GPU_REALTIME_TEMP = 0x80

FAN_RPM = 478000


class CPUGen(enum.IntEnum):
    DEFAULT = 0
    GEN11 = 1


class FanMode(enum.Enum):
    AUTO = "auto"
    BASIC = "basic"
    ADVANCED = "advanced"


FAN_MODES = {
    0x0D: FanMode.AUTO,
    0x4D: FanMode.BASIC,
    0x8D: FanMode.ADVANCED,
}
