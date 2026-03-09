#include <iostream>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()
#include <string>

using namespace std;

void showEasterEgg() {
    cout << "\n[!] EASTER EGG ACTIVATED: THE ZEN MODE" << endl;
    cout << "Inspired by the Word 1.1a secret found 29 years later." << endl;
    cout << "EiJackGH Lab - Saying YES in 2026." << endl;
    cout << "========================================" << endl;
}

int main() {
    // Seed the randomizer
    srand(static_cast<unsigned int>(time(0)));
    
    int secretNumber = rand() % 100 + 1;
    string input;
    int guess = 0;
    int attempts = 0;

    cout << "--- EI-JACK LAB: NUMBER GUESSER V1.0 ---" << endl;
    cout << "I'm thinking of a number between 1 and 100." << endl;
    cout << "(Hint: Type 'zen' to see the credits)" << endl << endl;

    while (guess != secretNumber) {
        cout << "Enter your guess: ";
        cin >> input;

        // Check for Easter Egg
        if (input == "zen" || input == "ZEN") {
            showEasterEgg();
            continue;
        }

        // Convert string to integer for the game logic
        try {
            guess = stoi(input);
        } catch (...) {
            cout << "Invalid input. Please enter a number." << endl;
            continue;
        }

        attempts++;

        if (guess > secretNumber) {
            cout << ">>> Too high! Try again." << endl;
        } else if (guess < secretNumber) {
            cout << ">>> Too low! Try again." << endl;
        } else {
            cout << "\nCONGRATULATIONS!" << endl;
            cout << "You found it in " << attempts << " attempts." << endl;
        }
    }

    cout << "----------------------------------------" << endl;
    system("pause"); // Essential for Dev-C++ to keep the window open
    return 0;
}
