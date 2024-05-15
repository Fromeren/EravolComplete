from flask import Flask, request, jsonify, request

import serial
import time

arduino = serial.Serial(port='COM5',  baudrate=115200, timeout=.1)
app = Flask(__name__)


# This route will receive data from the website
@app.route('/temperature', methods=['POST'])
def receive_data():
    data = request.json

    # Extracting the temperature data
    temperature = data.get('temperature')

    print("Data modtaget", temperature)

    # You can now use the temperature data as needed

    # Dummy response just for demonstration
    response = {'message': 'Data received successfully'}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode

def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return  data


while True:
    num = input("Enter a temperature: ")
    value  = write_read(num)
    print(value)
