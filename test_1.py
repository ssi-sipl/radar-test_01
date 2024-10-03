import serial
import threading
import sys

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

def write_to_port(ser):
    while True:
        try:
            message = input()
            ser.write(message.encode('utf-8') + b'\r\n')
        except serial.SerialException:
            print("Serial port closed")
            break
        except Exception as e:
            print(f"Error writing to port: {e}")
            break

def main():
    port = input("Enter serial port (e.g., /dev/ttyS0): ")
    baud_rate = int(input("Enter baud rate (e.g., 115200): "))

    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to {port} at {baud_rate} baud")

        read_thread = threading.Thread(target=read_from_port, args=(ser,))
        write_thread = threading.Thread(target=write_to_port, args=(ser,))

        read_thread.start()
        write_thread.start()

        print("Type your messages to send. Press Ctrl+C to exit.")

        read_thread.join()
        write_thread.join()

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
