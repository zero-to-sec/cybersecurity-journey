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
