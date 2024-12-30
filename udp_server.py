#!/bin/env python3

import socket
import xml.etree.ElementTree as ET
import re
import pandas as pd
import geojson
import json

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('10.99.41.255', 4242)  # Replace with your desired address and port
sock.bind(server_address)

print("Waiting for XML data...")


while True:
    data, address = sock.recvfrom(4096)  # Adjust buffer size as needed

    try:
        root = ET.fromstring(data.decode())  # Parse the XML data
        xml_type = None
        file_append = ""
        data = []
        uid = time = lat = long = detail = ""
        # Process the XML elements
        for element in root.iter():
            #row_data = {}
            xml_type = element.tag
            match xml_type:
                case "event":
                    uid = element.attrib['uid']
                    time = element.attrib['time']
                case "point":
                    lat = element.attrib['lat']
                    long = element.attrib['lon']
                case "detail":
                    detail = element.text
                case _:
                    print("wtf!")

        data.append(
            { 
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [ lat, long ]
                    },
                "properties": {
                    "name": uid,
                    "time": time,
                    "details": detail
                    }
             })
                    
        file_append = uid + ", " + time + ", " + lat + ", " + long + ", " + detail + "\n"
        print(file_append)
        #print(data)
        with open("/run/user/1000/gvfs/smb-share:server=10.99.40.84,share=hackathon%20data/data/normies.txt", "a") as file:
            file.write(file_append)

        with open("/run/user/1000/gvfs/smb-share:server=10.99.40.84,share=hackathon%20data/data/normies.json", "a") as file:
            json.dump(data, file)

    except ET.ParseError as e:
        print("Error parsing XML:", e)

"""
def main():
    # Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = ('0.0.0.0', 10000)
    sock.bind(server_address)

    print("UDP server listening on {}:{}".format(*server_address))

    while True:
        # Receive data from a client
        data, client_address = sock.recvfrom(4242)

        print("Received {} bytes from {}".format(len(data), client_address))
        print("Data:", data.decode())

        # Send a response to the client
        message = "Hello from the server!"
        sock.sendto(message.encode(), client_address)

if __name__ == "__main__":
    main()
"""
