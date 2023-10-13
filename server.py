import socket

# Define quiz question and answer
quiz_question = "What is the capital of France?"
correct_answer = "Paris"

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to a specific address and port
server.bind(('0.0.0.0', 12345))

# Listen for incoming connections
server.listen(5)
print("Server is listening on port 12345")

while True:
    # Accept a connection from a client
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address}")

    # Send the quiz question to the client
    client_socket.send(quiz_question.encode())

    # Receive the client's answer
    client_answer = client_socket.recv(1024).decode()

    # Check if the answer is correct
    if client_answer.lower() == correct_answer.lower():
        response = "Correct!"
    else:
        response = "Incorrect."

    # Send the response to the client
    client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()
