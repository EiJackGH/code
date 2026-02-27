# Use a lightweight C++ compiler image
FROM gcc:latest

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy your C++ file into the container
COPY NumberGuess.cpp .

# Compile the code
RUN g++ -o NumberGuess NumberGuess.cpp

# Command to run the game
CMD ["./NumberGuess"]
