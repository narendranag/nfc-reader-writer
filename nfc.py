# /dev/tty.usbmodem2F5272D864842

import serial
import time

# Update the port to match the one your Arduino is connected to
arduino_port = '/dev/tty.usbmodem2F5272D864842'  # e.g., '/dev/tty.usbmodem14101' on macOS
baud_rate = 115200  # Should match the baud rate in your Arduino code

def main():
    try:
        ser = serial.Serial(arduino_port, baud_rate, timeout=1)
        time.sleep(2)  # Wait for the connection to initialize
        print("Connected to Arduino. Listening for NFC data...")
        
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()
                print(f"Received from Arduino: {data}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ser.close()

if __name__ == "__main__":
    main()