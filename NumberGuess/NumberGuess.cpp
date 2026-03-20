#include <iostream>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()
#include <string>
#include <iomanip>

using namespace std;

// ANSI Color Constants for UX
const string RESET = "\033[0m";
const string BOLD = "\033[1m";
const string GREEN = "\033[32m";
const string YELLOW = "\033[33m";
const string BLUE = "\033[34m";
const string CYAN = "\033[36m";
const string RED = "\033[31m";


void showEasterEgg() {
    cout << "\n" << BOLD << CYAN << "[✨] EASTER EGG ACTIVATED: THE ZEN MODE" << RESET << endl;

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

    cout << BOLD << BLUE << "--- EI-JACK LAB: NUMBER GUESSER V1.0 ---" << RESET << endl;
    cout << "I'm thinking of a number between 1 and 100." << endl;
    cout << YELLOW << "(Hint: Type 'zen' to see the credits)" << RESET << endl << endl;

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
            cout << RED << "⚠️ Invalid input. Please enter a number." << RESET << endl;
            continue;
        }

        attempts++;

        if (guess > secretNumber) {
            cout << RED << "📈 Too high! Try again." << RESET << endl;
        } else if (guess < secretNumber) {
            cout << BLUE << "📉 Too low! Try again." << RESET << endl;
        } else {

            cout << "\n" << BOLD << GREEN << "╔════════════════════════════════════════╗" << endl;
            cout << "║ " << RESET << "🎉 CONGRATULATIONS! 🎉               " << BOLD << GREEN << "║" << endl;
            cout << "╠════════════════════════════════════════╣" << endl;
            cout << "║ " << RESET << "You found the secret number in: " << setw(4) << attempts << BOLD << GREEN << " ║" << endl;
            cout << "╚════════════════════════════════════════╝" << RESET << endl;

        }
    }

    cout << "----------------------------------------" << endl;
    cout << "\nPress Enter to exit..." << endl;
    cin.ignore(10000, '\n'); // Ignore any remaining characters in the buffer
    cin.get(); // Wait for the user to press Enter
    return 0;
}
