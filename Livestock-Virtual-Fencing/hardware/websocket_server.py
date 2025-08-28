import asyncio
import websockets
import json

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            pass  # Handle incoming messages if required
    finally:
        connected_clients.remove(websocket)

async def send_data():
    while True:
        data = {"x": 0.12, "y": -0.34, "z": 0.56, "lat": 51.5074, "lng": -0.1278}
        if connected_clients:
            message = json.dumps(data)
            await asyncio.wait([client.send(message) for client in connected_clients])
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await send_data()

asyncio.run(main())
