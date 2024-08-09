import requests

def updateFile(y):
    with open("stream/index.html", "wb") as x:
        q = "<html><head><title>GRU Streaming Element</title></head><body><p>" + y + " has joined as a GRU member.</p></body></html>"
        q = q.encode("utf-8")
        x.write(bytes(q))

r = requests.get('https://api.ipdata.co?api-key=b6c69cd24db05d3d56e2cb4e47a51bae7775bf82f63e70ec76ff23f6').json()
ip_address = r["ip"]
        
while True:
    updateFile(ip_address)