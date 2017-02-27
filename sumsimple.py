#!/usr/bin/python

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADOR, 1)#me libera el puerto
mySocket.bind(("localhost", 1234)) #ponemos gethostname para coger la ip de donde estemos

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5) #maximo 5 conexiones

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

sumando = 0;

try:
	while True:

		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
	 	print 'HTTP request received:'
		peticion = recvSocket.recv(1024)
		print peticion
		try:
			entero = int(peticion.split()[1][1:])

			print entero
			if sumando == 0:
				print "SUMANDO ES 0"
				sumando=entero;
				respuesta = "dame otro numero";
			else:
				resultado = entero + sumando;
				respuesta = "El resultado de la suma es :" + str(entero) + "+" + str(sumando) + "=" + str(resultado);
				sumando=0;

			Numaleatorio = random.randint(0,100000)
			recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
				              "<html><body><h1>HOLA!"
				               + respuesta + "</p>" + "<html><body><html>" +
				              "\r\n")
		except ValueError:
			continue
		recvSocket.close()
except KeyboardInterrupt:
	mysocket.close()
