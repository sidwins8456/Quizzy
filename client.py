import socket

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('127.0.0.1', 12345))

# Receive the quiz question from the server
question = client.recv(1024).decode()
print("Quiz Question:", question)

# Get the user's answer
answer = input("Your answer: ")

# Send the answer to the server
client.send(answer.encode())

# Receive and print the server's response
response = client.recv(1024).decode()
print("Server says:", response)

# Close the client socket
client.close()
