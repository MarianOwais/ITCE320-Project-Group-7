#Done By Group 7:
#Marian Samir Owais - 20182547
#Mohamed Salah AlBastawi - 20180992

import socket
import json
import sys

PORT=22334
HOST='127.0.0.1'
sock_c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_c.connect((HOST, PORT))
print("\nThe Client has started successfully ✔")

#Ask for Client name
client_n=input("\nEnter your name: ")

#Send Client name to the server
sock_c.send(client_n.encode())

#Ask for Airport code (arr_icao)
apcode=input("\nEnter the Airport Code: ")

#Send Airport code to the server
sock_c.send(apcode.encode())

print("✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈ ✈")

while True: # To keep the client ready until the user quits
    print("\nSelect one of the options below:")
    print("1- Display The Arrived flights\n"
          "2- Display The Delayed flights\n"
          "3- Display Flights from a specific city\n"
          "4- Display Details of a specific flight\n"
          "5- Quit 🗙\n")

    option = input()
    sock_c.send(option.encode())

    # Temporary .json file with the client name, to save data he requests from the server
    temp = r'C:\Users\marya\PycharmProjects\ITCE320 Project\client\temp/{}_data.json'.format(client_n)

    #1) Display The Arrived flights
    if option == '1':
        print("Loading: Details of all Arrived flights ⏳") #Loading message until the data are printed
        with open(temp, 'wb') as t:
            recevied = sock_c.recv(999999)
            t.write(recevied) #Write the received data within temp (json) file

        #Reading the data from the temp json file
        with open(temp) as t:
            flights = json.load(t)
            for output in flights["data"]: #Print the data according to the required parameters
                print("\nFlight Code (IATA):",output['flight']['iata'],"🔶 Departure Airport:",output['departure']['airport'],
                      "\nArrival Time:",output['arrival']['actual'],"🔶 Terminal:",output['arrival']['terminal'],"🔶 Gate:", output['arrival']['gate'],'\n',35 *'✈ ')


    #2) Display The Delayed flights
    if option == '2':
        print("Loading: Details of all Delayed flights ⏳")
        with open(temp, 'wb') as t:
            recevied = sock_c.recv(999999)
            t.write(recevied)

        with open(temp) as t:
            flights = json.load(t)
            for output in flights["data"]:
                print("\nFlight Code (IATA):",output['flight']['iata'],"🔶 Departure Airport:",output['departure']['airport'],
                      "\nDeparture Time:",output['departure']['actual'],"🔶 Estimated Arrival:",output['arrival']['estimated'],"🔶 Terminal:", output['arrival']['terminal'],"🔶 Gate:", output['arrival']['gate'],'\n',35 *'✈ ')


    #3) Display Flights from a specific city
    if option == '3':
        #Ask the client for the city code, and sent it to server
        city = input("Enter the City Code: ")
        sock_c.send(city.encode())

        print("Loading: All flights coming from",city,"⏳")

        with open(temp, 'wb') as t:
            recevied = sock_c.recv(999999)
            t.write(recevied)

        with open(temp) as t:
            flights = json.load(t)
            for output in flights["data"]:
                print("\nFlight Code (IATA):",output['flight']['iata'],"🔶 Departure Airport:",output['departure']['airport'],
                      "\nDeparture Time:",output['departure']['actual'],"🔶 Estimated Arrival:",output['arrival']['estimated'],"🔶 Terminal:", output['arrival']['terminal'],"🔶 Gate:", output['arrival']['gate'],'\n',35 *'✈ ')


  #4) Display Details of a specific flight
    if option == '4':
        #Ask the client for flight number, and send it to server
        fnumber = input("Enter the Flight Number: ")
        sock_c.send(fnumber.encode())

        print("Loading: Details of Flight Number",fnumber,"⏳")

        with open(temp, 'wb') as t:
            recevied = sock_c.recv(999999)
            t.write(recevied)

        with open(temp) as t:
            flights = json.load(t)
            for output in flights["data"]:
                print("\nFlight Code (IATA):",output['flight']['iata'],"🔶 Date:",output['flight_date'],
                      "\nDeparture Airport:",output['departure']['airport'],"🔶 Departure Gate:",output['departure']['gate'],"🔶 Departure Terminal:",output['departure']['terminal'],
                      "\nArrival Airport:",output['arrival']['airport'],"🔶 Arrival Gate:", output['arrival']['gate'],"🔶 Arrival Terminal:", output['arrival']['terminal'],
                      "\nFlight Status:",output['flight_status'],"🔶 Scheduled Departure Time:",output['departure']['scheduled'],"🔶 Scheduled Arrival Time:",output['arrival']['scheduled'],
                      "\nEstimated Arrival Time:",output['arrival']['estimated'],"🔶 Delay:",output['arrival']['delay'],'\n',35 *'✈ ')


    #5) Close the connection and Quit
    if option == '5':
        print("Connection has been closed 🔌")
        print("Good Bye")
        sys.exit()























