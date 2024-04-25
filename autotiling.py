import asyncio
import websockets
import json
import platform
import subprocess


# async def free_port():
#     port = 6123
#     system = platform.system()
    
#     if system == "Windows":
#         # On Windows, use netstat to find the process ID (PID) using the port
#         cmd = f"netstat -aon | findstr :{port}"
#         output = subprocess.check_output(cmd, shell=True, encoding="utf-8")
#         if output.strip():
#         # Port is in use, free it
#             try:
#                 output = subprocess.check_output(cmd, shell=True, encoding="utf-8")
#                 lines = output.strip().split("\n")
#                 for line in lines:
#                     parts = line.split()
#                     if parts[-1] != "LISTENING":
#                         continue
#                     pid = int(parts[-2])
#                     # Terminate the process using the PID
#                     subprocess.run(["taskkill", "/F", "/PID", str(pid)], check=True)
#             except subprocess.CalledProcessError:
#                 print(f"Failed to free port {port}")
#         else:
#             print(f"Port {port} is not in use.")


# async def start_websocket_server():
#     async def echo(websocket, path):
#         async for message in websocket:
#             await websocket.send(message)

#     server = await websockets.serve(echo, "localhost", 6123)
#     print(f"WebSocket server started and listening on ws://{server.sockets[0].getsockname()[0]}:{server.sockets[0].getsockname()[1]}")
#     await server.wait_closed()  # Wait for the server to be closed

async def main():
    # # Start the WebSocket server if it's not already running
    # try:
    #     await asyncio.wait_for(start_websocket_server(), timeout=5)
    # except asyncio.TimeoutError:
    #     print("Timeout occurred while starting WebSocket server.")

    uri = "ws://localhost:6123"
    try:
        websocket = await websockets.connect(uri)
    except ConnectionRefusedError:
        print("Connection refused. Make sure the WebSocket server is running and accepting connections.")
        return
    
    try:
        # Send the "hello" message
        await websocket.send("subscribe -e window_managed")

        while True:
            response = await websocket.recv()
            if response:  # Check if response is not empty
                json_response = json.loads(response)
                try:
                    sizePercentage = json_response["data"]["managedWindow"]["sizePercentage"]
                    if sizePercentage <= 0.5:
                        await websocket.send('command "tiling direction toggle"')
                except KeyError:
                    pass
    finally:
        await websocket.close()  # Close the WebSocket connection

if __name__ == "__main__":
    asyncio.run(main())
