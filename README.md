##Course: ISYS2101_15s1 - s1-Software Engineering Project Management
## Project name: Parking Slot Management
## Group 2
## Group members:
**Nguyen Vinh Linh - s3410595**  
**Tran Vuong Trung - s3408675**  
**Kang Rok Kim - s3479779**  
**Mai Hoang - s3426105**  
**Tran Ngoc Thuc - s3446356**  
## Description:
The project uses Raspberry PI and Ultra Sonic to determine cars. All state of
each parking slot will be published on the internet via website or mobile
application. The main component takes responsibility to handle updating date is
Web Socket Server.   

Web socket server is an open library which is written in python.
[SimpleWebSocketServer](https://github.com/opiate/SimpleWebSocketServer)  

## How to install:
**a. Requirement**  
The system requires a Apache Web Server, if you are using Raspbian you can use
`sudo apt-get install apache2 -y` to install the Apache Web server. The default directory
of `html source` for apache2 is `/var/www`   

**b. Installing**
- Clone the repository `git clone
  git@github.com:nguyenvinhlinh/ParkingSlot.git`  
- In the file named `ParkingSlot.py`, change the IP of hosted Rapsberry PI
  instead of `localhost`, with favor port. The default value for web socket port
  is `8000`  
- In the directory `www`, find file named `index.html`, At position `column:44,
  row:95`, change the default value of web socket server to the IP of hosted
  Raspberry PI instead of `localhost:8000` with favor port  
- In the root directory of repository, run the script `install.sh`, for example `./install.sh`  

## How to run:
- In the root directory of the repository, run the script `start.sh`, for
  example, `./start.sh`
