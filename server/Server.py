#Done By Group 7:
#Marian Samir Owais - 20182547
#Mohamed Salah AlBastawi - 20180992

import socket
import threading
import json
import requests

print("\nPlease wait ⏳")

PORT=22334
HOST='127.0.0.1'
sock_p = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_p.bind((HOST, PORT))

sock_p.listen(3)

print("\nThe Server has started successfully ✔") #Confirming that the server is ready for the client

#Function responsible for client connection
#Receives the client name and the arr_icao from the client
def cc(s):
    cname = s.recv(1024).decode()
    print("\n➡Client",cname,"has connected")
    apcode = s.recv(1024).decode()


#Main function responsible for retrieving the data depending on the option chosen
    def main(params):
        api_request = requests.get('http://api.aviationstack.com/v1/flights', params)
        api_response = api_request.json()
        dir = r'C:\Users\marya\PycharmProjects\ITCE320 Project\server/group_7.json'
        file = open(dir, 'w')
        file.write(json.dumps(api_response, indent=2))
        file.close()
        return (dir)

    while True:
        o = s.recv(1024).decode() #Receiving the option from the client

        #1) Display The Arrived flights
        if o == '1':
            #The parameters to fufill the requested option
            params = {
                'access_key': '324ebc81fbf19047f7dba843e9342273',
                'arr_icao': apcode,
                'flight_status': 'landed'
            }
            #Retrive the data and send it to the client by excecuting the main function
            with open(main(params), 'rb') as f:
                details = f.read()
                s.sendall(details)

            #Confirming that the client received the data
            print("\n➡Client",cname,"has requested the details below of Arrived flights:\n"
            "Flight code (IATA), Departure Airport, Arrival Time, Terminal, Gate")


        #2) Display The Delayed flights
        if o == '2':
            params = {
                'access_key': '324ebc81fbf19047f7dba843e9342273',
                'arr_icao': apcode,
                'min_delay_arr': '0'
            }
            with open(main(params), 'rb') as f:
                details = f.read()
                s.sendall(details)

            print("\n➡Client",cname,"has requested the details below of Delayed flights:\n"
            "Flight code (IATA), Departure Airport, Departure Time, Estimated Arrival Time, Terminal, Gate")


        #3) Display Flights from a specific city
        if o == '3':
            city = s.recv(1024).decode() #Receving the city code from client
            params = {
                'access_key': '324ebc81fbf19047f7dba843e9342273',
                'dep_iata': city,
                'arr_icao': apcode,
            }

            with open(main(params), 'rb') as f:
                details = f.read()
                s.sendall(details)

            print("\n➡Client", cname, "has requested the details below of flights coming from",city,
              "\nDeparture Airport, Departure Time, Estimated Arrival Time, Terminal, Gate")


        #4) Display Details of a specific flight
        if o == '4':
            flightn = s.recv(1024).decode() #Receivng the flight number from the client
            params = {
                'access_key': '324ebc81fbf19047f7dba843e9342273',
                'flight_number': flightn,
                'arr_icao': apcode,
            }

            with open(main(params), 'rb') as f:
                details = f.read()
                s.sendall(details)

            print("\n➡Client",cname,"has requested the details below of the flight ",flightn,
                  "\nFlight code (IATA), Date, Departure Airport, Departure Gate, Departure Terminal, Arrival Airport, Arrival Gate, Arrival Terminal, Status,Scheduled Departure Time,Scheduled Arrival Time")

        #5)Close the connection and Quit
        if o == '5':
            print("\n➡Client",cname,"has closed the connection.")
            break

threads = []

#Threading
while True:
    sock_a, sockname = sock_p.accept()
    t = threading.Thread(target=cc(sock_a), args=(sock_a, len(threads) +1))
    threads.append(t)
    t.start()
    if len(threads) > 3: #Assiging the number of threads
        break







