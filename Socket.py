#!/user/bin/env python

# Importing the socket module
import socket

# We use the socket() method of the module socket and store it in the variable s.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Here we use the connect method of the socket we created. The two arguments are pretty self-explanatory
# The first is the adress the second is the port.
s.connect(("address",port_number )) #link and port number

# Here we save what the socket reviewed in the variable answer.
answer = s.recv(1024)
print answer

# Send stuff. REMEMBER THE \r\n
payload = #insert payload here 	#Example of payload 'A'*62 + '\x82\x91\x04\x08'  		
s.send(payload +'\n')
print s.recv(1024)

# Here we close the socket.
s.close
