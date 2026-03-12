#include <iostream>
#include <cstdlib> // For rand() and srand()
#include <ctime>   // For time()
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

// ANSI Color Codes
const string RESET = "\033[0m";
const string RED = "\033[31m";
const string GREEN = "\033[32m";
const string YELLOW = "\033[33m";
const string BLUE = "\033[34m";
const string MAGENTA = "\033[35m";
const string CYAN = "\033[36m";
const string BOLD = "\033[1m";

const string HIGHSCORE_FILE = "NumberGuess/highscore.txt";

int loadHighScore() {
    ifstream file(HIGHSCORE_FILE);
    int highScore = 999;
    if (file.is_open()) {
        file >> highScore;
        file.close();
    }
    return highScore;
}

void saveHighScore(int score) {
    ofstream file(HIGHSCORE_FILE);
    if (file.is_open()) {
        file << score;
        file.close();
    }
}

void showEasterEgg() {
    cout << MAGENTA << "\n[!] EASTER EGG ACTIVATED: THE ZEN MODE" << RESET << endl;
    cout << "Inspired by the Word 1.1a secret found 29 years later." << endl;
    cout << "EiJackGH Lab - Saying YES in 2026." << endl;
    cout << MAGENTA << "========================================" << RESET << endl;
}

void printHeader() {
    cout << CYAN << "╔════════════════════════════════════════╗" << RESET << endl;
    cout << CYAN << "║       " << BOLD << "EI-JACK LAB: NUMBER GUESSER" << RESET << CYAN << "      ║" << RESET << endl;
    cout << CYAN << "╚════════════════════════════════════════╝" << RESET << endl;
}

int main() {
    // Seed the randomizer
    srand(static_cast<unsigned int>(time(0)));
    
    string playAgainInput;
    char playAgain;
    int highScore = loadHighScore();

    do {
        int secretNumber = rand() % 100 + 1;
        string input;
        int guess = 0;
        int attempts = 0;

        printHeader();
        cout << YELLOW << "Current High Score: " << BOLD << (highScore == 999 ? "N/A" : to_string(highScore)) << RESET << " attempts" << endl;
        cout << "I'm thinking of a number between " << BOLD << "1 and 100" << RESET << "." << endl;
        cout << "(Hint: Type 'zen' to see the credits)" << endl << endl;

        while (guess != secretNumber) {
            cout << "Enter your guess: ";
            if (!(cin >> input)) break;

            // Check for Easter Egg
            if (input == "zen" || input == "ZEN") {
                showEasterEgg();
                continue;
            }

            // Convert string to integer for the game logic
            try {
                guess = stoi(input);
            } catch (...) {
                cout << RED << "Invalid input. Please enter a number." << RESET << endl;
                continue;
            }

            attempts++;

            if (guess > secretNumber) {
                cout << RED << ">>> Too high! 📈 Try again." << RESET << endl;
            } else if (guess < secretNumber) {
                cout << BLUE << ">>> Too low!  📉 Try again." << RESET << endl;
            } else {
                cout << "\n" << GREEN << BOLD << "🎉 CONGRATULATIONS! 🎉" << RESET << endl;

                cout << "╔════════════════════════════════════════╗" << endl;
                cout << "║            " << BOLD << "GAME SUMMARY" << RESET << "                ║" << endl;
                cout << "╠════════════════════════════════════════╣" << endl;
                cout << "║ Attempts: " << setw(28) << left << attempts << " ║" << endl;

                if (attempts < highScore) {
                    highScore = attempts;
                    saveHighScore(highScore);
                    // Adjusted padding for emoji width (Emoji 🏆 is 2-char wide in many terminals)
                    cout << "║ " << GREEN << BOLD << "NEW HIGH SCORE! 🏆" << RESET << setw(20) << "" << " ║" << endl;
                }

                cout << "╚════════════════════════════════════════╝" << endl;
            }
        }

        cout << "\nDo you want to play again? (y/n): ";
        if (!(cin >> playAgainInput)) break;
        playAgain = playAgainInput[0];
        cout << endl;

    } while (playAgain == 'y' || playAgain == 'Y');

    cout << CYAN << "Thanks for playing! See you next time at EiJack Lab! 👋" << RESET << endl;

    return 0;
}
