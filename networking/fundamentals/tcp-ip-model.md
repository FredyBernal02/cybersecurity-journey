# TCP/IP Model

## Objective

Understand how data moves through the TCP/IP model and how network layers interact with each other.

---

## Key Concepts

- TCP/IP Model
- Encapsulation
- Decapsulation
- PDU
- Segment
- Packet
- Frame
- Headers
- Trailer

---

## What I Learned
The TCP/IP model is used to describe how devices communicate over a network.

The 5 layers are:

1. Application
2. Transport
3. Internet
4. Data Link
5. Physical

Each layer has a specific role in network communication.

Data moves down through the layers during encapsulation and moves up through the layers during decapsulation.

Each layer adds its own header to the data before transmitting it across the network.

Common PDUs:
- Segment (Layer 4)
- Packet (Layer 3)
- Frame (Layer 2)

At the physical layer, data is transmitted as bits (0s and 1s).

---

## My Understanding
The TCP/IP model helps organize network communication into layers.

Each layer adds information that allows data to travel correctly across networks.

Encapsulation means adding headers as data moves down the layers, while decapsulation removes those headers at the destination device.

---

## Notes
- Layer 4 PDU = Segment
- Layer 3 PDU = Packet
- Layer 2 PDU = Frame
- Layer 1 transmits bits
- Encapsulation = adding headers
- Decapsulation = removing headers
- Ethernet frames include a trailer for error detection

### Common Protocols by Layer

#### Application Layer
- HTTP (HyperText Transfer Protocol)
- HTTPS (HyperText Transfer Protocol Secure)
- DNS (Domain Name System)
- DHCP (Dynamic Host Configuration Protocol)
- FTP (File Transfer Protocol)
- SSH (Secure Shell)

#### Transport Layer
- TCP (Transmission Control Protocol)
- UDP (User Datagram Protocol)

#### Internet Layer
- IP (Internet Protocol)
- ICMP (Internet Control Message Protocol)

#### Data Link Layer
- Ethernet

#### Physical Layer
- Copper Cable
- Fiber Optic
- Wireless Signals