import asyncio  # Provides support for asynchronous programming
import tkinter as tk  # Provides the GUI framework for the application
import websockets  # Provides WebSocket protocol support for asynchronous communication

# Create the main Tkinter window
root = tk.Tk()  # Initializes the root window for the GUI

# Create a label to display messages received from the WebSocket
label = tk.Label(root, text="Waiting for message...")  # A Label widget for displaying text
label.pack()  # Adds the Label widget to the window

# Function to update the label with new text
def update_label(message):
    # Updates the Label text (Tkinter must update widgets in the main thread)
    root.after(0, label.config, {"text": message})

# Define the function to handle WebSocket communication
async def run_websocket():
    # WebSocket URI for connection
    uri = "wss://demo.piesocket.com/v3/channel_123?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self"
    try:
        # Connect to the WebSocket server
        async with websockets.connect(uri) as websocket:
            while True:
                # Wait for a message from the server
                message = await websocket.recv()
                print(f"Received: {message}")  # Print the received message to the console
                update_label(message)  # Update the GUI label with the message
    except Exception as e:
        # Print any error that occurs during WebSocket communication
        print(f"WebSocket error: {e}")

# Define a function to start the WebSocket communication
def start_websocket():
    # Use asyncio to run the WebSocket communication as a background task
    asyncio.create_task(run_websocket())

# Create a button to start the WebSocket communication
start_button = tk.Button(root, text="Start WebSocket", command=start_websocket)
start_button.pack()  # Adds the Button widget to the window

# Define a combined Tkinter and asyncio event loop
async def tkinter_async_loop():
    while True:
        root.update()  # Process Tkinter events
        await asyncio.sleep(0.01)  # Allow asyncio tasks to run

# Entry point of the program
if __name__ == "__main__":
    # Run the combined event loop using asyncio
    asyncio.run(tkinter_async_loop())
