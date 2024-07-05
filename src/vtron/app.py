from vtron._reader import Reader
from vtron.constants import EC_FILE_PATH


def main() -> None:
    reader = Reader(EC_FILE_PATH)
    text = f"""
    Fan Mode: {reader.get_fan_mode()}
    CPU TEMP: {reader.get_realtime_cpu_temp()}
    FAN RPM: {reader.get_realtime_cpu_fan_rpm()}
    GPU TEMP: {reader.get_realtime_gpu_temp()}
    """
    print(text)
