#include <iostream>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()
#include <string>
#include <iomanip>

using namespace std;

// ANSI Color Codes
const string RESET = "\033[0m";
const string GREEN = "\033[32m";
const string RED = "\033[31m";
const string YELLOW = "\033[33m";
const string CYAN = "\033[36m";
const string MAGENTA = "\033[35m";

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

    cout << CYAN << "╔══════════════════════════════════════╗" << RESET << endl;
    cout << CYAN << "║ " << MAGENTA << setw(36) << left << "EI-JACK LAB: NUMBER GUESSER V1.0" << CYAN << " ║" << RESET << endl;
    cout << CYAN << "╚══════════════════════════════════════╝" << RESET << endl;
    cout << "🤔 I'm thinking of a number between 1 and 100." << endl;
    cout << YELLOW << "(Hint: Type 'zen' to see the credits)" << RESET << endl << endl;

    while (guess != secretNumber) {
        cout << "Enter your guess 🎯: ";
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
            cout << RED << "❌ Invalid input. Please enter a number." << RESET << endl;
            continue;
        }

        attempts++;

        if (guess > secretNumber) {
            cout << RED << "📈 Too high! Try again." << RESET << endl;
        } else if (guess < secretNumber) {
            cout << YELLOW << "📉 Too low! Try again." << RESET << endl;
        } else {
            cout << "\n" << GREEN << "🎉 CONGRATULATIONS! 🎉" << RESET << endl;
            cout << GREEN << "You found it in " << attempts << " attempts." << RESET << endl;
        }
    }

    cout << CYAN << "----------------------------------------" << RESET << endl;
    cout << "Press Enter to exit..." << endl;
    cin.ignore(10000, '\n');
    cin.get();
    return 0;
}
