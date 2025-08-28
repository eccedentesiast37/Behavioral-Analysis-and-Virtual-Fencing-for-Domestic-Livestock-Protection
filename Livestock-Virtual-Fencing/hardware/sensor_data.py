import smbus2
import time
import serial
import json
import asyncio
import websockets

# MPU6050 constants
MPU6050_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

bus = smbus2.SMBus(1)
bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

def read_raw_data(addr):
    high = bus.read_byte_data(MPU6050_ADDR, addr)
    low = bus.read_byte_data(MPU6050_ADDR, addr+1)
    value = ((high << 8) | low)
    if value > 32768:
        value = value - 65536
    return value

def get_accel_data():
    ax = read_raw_data(ACCEL_XOUT_H) / 16384.0
    ay = read_raw_data(ACCEL_XOUT_H + 2) / 16384.0
    az = read_raw_data(ACCEL_XOUT_H + 4) / 16384.0
    return ax, ay, az

# GPS setup
gps_serial = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

def read_gps():
    line = gps_serial.readline().decode('ascii', errors='replace')
    if line.startswith('$GPGGA'):
        parts = line.split(',')
        if parts[2] and parts[4]:
            lat = float(parts[2]); lon = float(parts[4])
            lat_deg = int(lat / 100); lat_min = lat - (lat_deg * 100)
            latitude = lat_deg + lat_min / 60
            lon_deg = int(lon / 100); lon_min = lon - (lon_deg * 100)
            longitude = lon_deg + lon_min / 60
            return latitude, longitude
    return None, None

async def send_sensor_data():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            ax, ay, az = get_accel_data()
            lat, lng = read_gps()
            data = {"x": ax, "y": ay, "z": az, "lat": lat, "lng": lng}
            await websocket.send(json.dumps(data))
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(send_sensor_data())
