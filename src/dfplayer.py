
import serial
import time

# Initialize UART connection to DFPlayer
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

def send_cmd(cmd):
    ser.write(bytearray(cmd))
    time.sleep(0.1)

def play_track(track_num):
    high_byte = (track_num >> 8) & 0xFF
    low_byte = track_num & 0xFF
    checksum = 0xFFFF - (0xFF + 0x06 + 0x03 + 0x00 + high_byte + low_byte) + 1
    checksum_high = (checksum >> 8) & 0xFF
    checksum_low = checksum & 0xFF
    cmd = [0x7E, 0xFF, 0x06, 0x03, 0x00, high_byte, low_byte, checksum_high, checksum_low, 0xEF]
    send_cmd(cmd)

if __name__ == "__main__":
    track = int(input("Which track? "))
    play_track(track)
