import serial
import time

# Configure the serial port
port = '/dev/ttyS0'  # Change this to your UART port
baud_rate = 115200   # Set the baud rate to 115200

try:
    # Create a serial connection
    ser = serial.Serial(port, baud_rate, timeout=1)

    print(f"Listening on {port} at {baud_rate} baud...")

    while True:
        if ser.in_waiting > 0:  # Check if there is data waiting
            data = ser.readline().decode('utf-8').rstrip()  # Read a line and decode
            
            try:
                value = float(data)  # Convert the received data to float
                
                # Check if the value is within the specified range
                if 100 <= value <= 200:
                    print(f"Received: {value} meters")
                    
            except ValueError:
                # Ignore invalid data without printing anything
                pass

except serial.SerialException as e:
    print(f"Error: {e}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close()  # Make sure to close the serial connection
