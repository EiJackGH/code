#include <iostream>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()
#include <string>
#include <iomanip>

using namespace std;

// ANSI Color Constants
const string GREEN = "\033[32m";
const string RED = "\033[31m";
const string CYAN = "\033[36m";
const string YELLOW = "\033[33m";
const string BOLD = "\033[1m";
const string RESET = "\033[0m";

void showEasterEgg() {
    cout << "\n" << CYAN << BOLD;
    cout << "╔════════════════════════════════════════╗\n";
    cout << "║ 🌟 EASTER EGG ACTIVATED: THE ZEN MODE ║\n";
    cout << "╠════════════════════════════════════════╣\n";
    cout << "║ Inspired by the Word 1.1a secret found ║\n";
    cout << "║ 29 years later.                        ║\n";
    cout << "║ EiJackGH Lab - Saying YES in 2026.     ║\n";
    cout << "╚════════════════════════════════════════╝\n" << RESET;
}

int main() {
    // Seed the randomizer
    srand(static_cast<unsigned int>(time(0)));
    
    int secretNumber = rand() % 100 + 1;
    string input;
    int guess = 0;
    int attempts = 0;

    cout << CYAN << BOLD << "--- 🎮 EI-JACK LAB: NUMBER GUESSER V1.0 ---" << RESET << endl;
    cout << "I'm thinking of a number between 1 and 100." << endl;
    cout << YELLOW << "(Hint: Type 'zen' to see the credits)" << RESET << endl << endl;

    while (guess != secretNumber) {
        cout << BOLD << "Enter your guess: " << RESET;
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
            cout << RED << "⚠️ Invalid input. Please enter a number." << RESET << endl;
            continue;
        }

        attempts++;

        if (guess > secretNumber) {
            cout << RED << "📉 Too high! Try again." << RESET << endl;
        } else if (guess < secretNumber) {
            cout << RED << "📈 Too low! Try again." << RESET << endl;
        } else {
            cout << "\n" << GREEN << BOLD << "🎉 CONGRATULATIONS!" << RESET << endl;
            cout << "You found it in " << YELLOW << attempts << RESET << " attempts." << endl;
        }
    }

    cout << "----------------------------------------" << endl;
    cout << "\nPress Enter to exit..." << endl;
    cin.ignore(10000, '\n');
    cin.get();
    return 0;
}
