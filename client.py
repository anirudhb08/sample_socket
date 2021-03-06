import socketio

host = '0.0.0.0'
port = 5000
sio_client = socketio.Client()

sio_client.connect("http://" + str(host) + ":" + str(port), namespaces = ['/con', '/'])

@sio_client.event
def message(data):
    print(data)

@sio_client.event
def connect():
    print("connected to server")