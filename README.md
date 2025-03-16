File Transfer using TCP and UDP in Python

Overview

This project implements a simple file transfer system using both TCP and UDP protocols in Python. The TCP method ensures reliable file transfer, while the UDP method provides faster but less reliable transfer.

Features

TCP File Transfer (Reliable, ordered delivery)

UDP File Transfer (Faster but may have packet loss)

Supports any file type (Text, images, etc.)

Simple and easy-to-use command-line interface

Error handling for missing files

Technologies Used

Python

Sockets (TCP & UDP)

Networking Basics

Prerequisites

Ensure you have Python installed on your system.

python3 --version

If Python is not installed, download it from python.org or install it using Homebrew on macOS:

brew install python3

Setup

Clone this repository:

git clone https://github.com/yourusername/file-transfer-python.git
cd file-transfer-python

Create a test file in the server directory:

echo "Hello, this is a test file!" > test.txt

How to Run

TCP File Transfer

Start the TCP Server

python3 tcp_server.py

Start the TCP Client

python3 tcp_client.py

Enter the filename when prompted (e.g., test.txt).

The client will receive the file and save it as received_test.txt.

UDP File Transfer

Start the UDP Server

python3 udp_server.py

Start the UDP Client

python3 udp_client.py

Enter the filename when prompted (e.g., test.txt).

The client will receive the file and save it as received_test.txt.

Example Output

Server (TCP)

[TCP] Server listening on 127.0.0.1:5001
[TCP] Connection from ('127.0.0.1', 54678)
[TCP] File test.txt sent successfully.

Client (TCP)

[TCP] File test.txt received successfully.

Troubleshooting

File Not Found Error? Ensure test.txt exists in the server's directory.

Address Already in Use? Change the port number in the script (e.g., port=5003).

UDP File Corruption? UDP doesn’t guarantee order or reliability—use TCP for accuracy.

License

This project is open-source and available under the MIT License.

Author

Your Name

Contributing

Feel free to submit issues or pull requests to enhance this project!

