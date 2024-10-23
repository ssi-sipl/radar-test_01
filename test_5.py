import serial
import logging

# Configure the serial port
port = '/dev/ttyS0'  # Change this to your UART port
baud_rate = 115200   # Set the baud rate to 115200

# Set up logging
logging.basicConfig(filename='uart_values.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

try:
    # Create a serial connection
    ser = serial.Serial(port, baud_rate, timeout=1)

    print(f"Listening on {port} at {baud_rate} baud...")

    while True:
        if ser.in_waiting > 0:  # Check if there is data waiting
            data = ser.readline().decode('utf-8').rstrip()  # Read a line and decode
            
            try:
               # value = float(data)  # Convert the received data to float
                
                # Check if the value is within the specified range
                if 100 <= data <= 200:
                    print(f"Received: {value} meters")
                    logging.info(f"Received: {value} meters")  # Log the in-range value
                else:
                    logging.info(f"Out of range: {value} meters")  # Log the out-of-range value
                    
            except ValueError:
                logging.warning(f"Invalid data received: {data}")  # Log invalid data

except serial.SerialException as e:
    logging.error(f"Serial error: {e}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close()  # Make sure to close the serial connection
