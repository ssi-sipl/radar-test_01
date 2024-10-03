import serial
import threading
import sys
import time

def read_from_port(ser):
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(f"Received: {data}")
        except serial.SerialException:
            print("Serial port closed")
            break
        except Exception as e:
            print(f"Error reading from port: {e}")
            break

def main():
    port = /dev/ttyS0
    baud_rate = 115200

    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to {port} at {baud_rate} baud")

        read_thread = threading.Thread(target=read_from_port, args=(ser,))  
        read_thread.start()
        read_thread.join()

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        if 'ser' in locals():
            ser.close()
            print("Serial port closed")

if __name__ == "__main__":
    main()
