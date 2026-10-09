#OSI MODEL

.Layer 1: Physical - Its function is to control signals, i.e., Ethernet cable, Fibre cable, etc.

.Layer 2: Data Link - Its function is to create a frame, i.e., to classify the MAC sender and receiver for the packet.

.Layer 3: Network - Its function is to add the IP sender and receiver to the data segment and create the packet.

.Layer 4: Transport - Its function is to divide data into data segments to facilitate its rapid transfer without any data loss. It also determines the port for the device that will receive the data and chooses whether to use the UDP protocol (speed without guarantee) or TCP (guaranteed delivery without speed).

.Layer 5: Session - Its function is to create, maintain, and terminate sessions and perform synchronization between the two parties.

.Layer 6: Presentation - Its function is to translate, compress, and encrypt data.

.Layer 7: Application - This is the final interface that you see, and its function is to define the service protocol.

#TCP/IP

.Apllication = (application + presentation + session)

.Transport = (transport)

.Internet = (network)

.Link = (data link + physical)

OSI is a theoretical model that helps you analyze and explain. However, TCP/IP is the practical model that the Internet and networks operate with and are built upon.

TCP handshake: is 3 steps to establish a reliable connection between client and server
1. SYN : The client sends a data packet containing the SYN tag (synchronization) and sequence number (x) to the server to inform it of its desire to initiate a connecton
2. SYN-ACK : The server receives and responds with SYN and ACK (confirmation) where it sends its sequence number, for example (y), and confirms receipt of the client number by adding 1 it (x+1)
3. ACK : The client responds by sending an ACK packet to the server, confirming receipt its response (y+1). the connection is then successfully established, and the data transfer process begins.

DNS Lookup : it start with operation system to ask DNS resolver when it searches in the DNS cashe and doesn't find the website's IP. It then asks the root name server. followed by the TLD server which stores website names (.com .net ). Finally it goes to authoritative name server, which provides the website's IP. This is then stored in the cashe to avoid repeating the process each time.
