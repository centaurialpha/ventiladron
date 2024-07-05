from io import BufferedWriter
from pathlib import Path

from vtron import constants
from vtron._reader import Reader


class Manager:
    def __init__(self, reader: Reader) -> None:
        self._reader = reader
        self._current_cooler_boost_mode = None

    def _open_file_rw(self, filepath: Path) -> BufferedWriter:
        return filepath.open("wb")

    def set_cooler_boost(self, mode: int) -> None:
        if self._current_cooler_boost_mode == mode:
            return
        fd = self._open_file_rw(constants.EC_FILE_PATH)
        data = 0
        if mode == constants.CoolerBoostModes.ON:
            data |= constants.COOLER_BOOST_ON
        elif mode == constants.CoolerBoostModes.OFF:
            data &= constants.COOLER_BOOST_OFF
        else:
            return
        fd.seek(constants.COOLER_BOOST_ADDR)
        fd.write(bytes((data,)))
        fd.close()
