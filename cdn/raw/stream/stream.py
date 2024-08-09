import requests
import base64
import time

def updateFile(y1, y2, y3, y4, y5):
    with open("stream/index.html", "wb") as x:
        q = "<html><head><title>GRU Streaming Element</title></head><body><div><p>" + y1 + " has joined as a GRU member.</p></div><div><p>" + y2 + " has joined as a GRU member.</p></div><div><p>" + y3 + " has joined as a GRU member.</p></div><div><p>" + y4 + " has joined as a GRU member.</p></div><div><p>" + y5 + " has joined as a GRU member.</p></div></body></html>"
        q = q.encode("utf-8")
        x.write(bytes(q))
        
while True:
    r1 = str(base64.b64decode(bytes("KHVzZXJuYW1lKQ==".encode("utf-8"))))
    r2 = str(base64.b64decode(bytes("KHVzZXJuYW1lKQ==".encode("utf-8"))))
    r3 = str(base64.b64decode(bytes("KHVzZXJuYW1lKQ==".encode("utf-8"))))
    r4 = str(base64.b64decode(bytes("KHVzZXJuYW1lKQ==".encode("utf-8"))))
    r5 = str(base64.b64decode(bytes("czNtaWNvbG9u".encode("utf-8"))))
    updateFile(r1, r2, r3, r4, r5)
    time.sleep(60)