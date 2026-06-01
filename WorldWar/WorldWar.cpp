#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <limits>

#define RED     "\033[31m"
#define GREEN   "\033[32m"
#define YELLOW  "\033[33m"
#define BLUE    "\033[34m"
#define MAGENTA "\033[35m"
#define CYAN    "\033[36m"
#define RESET   "\033[0m"
#define BOLD    "\033[1m"

using namespace std;

struct Country {
    string name;
    int health;
    int troops;
    int budget;
    bool isAlive;
};

// Global variables for game state
vector<Country> countries;
int playerIndex = -1;

void showEasterEgg() {
    cout << "\n" << MAGENTA << "[!] EASTER EGG ACTIVATED: THE ZEN MODE" << RESET << endl;
    cout << "Inspired by the Word 1.1a secret found 29 years later." << endl;
    cout << "EiJackGH Lab - Saying YES in 2026." << endl;
    cout << "========================================" << endl;
}

void initializeGame() {
    countries.push_back({"USA", 100, 50, 1000, true});
    countries.push_back({"China", 100, 60, 800, true});
    countries.push_back({"Russia", 100, 70, 600, true});
    countries.push_back({"Germany", 100, 40, 900, true});
    countries.push_back({"Japan", 100, 30, 1100, true});
}

void showStats() {
    cout << "\n" << BOLD << "--- Current Standings ---" << RESET << endl;
    for (size_t i = 0; i < countries.size(); ++i) {
        if (countries[i].isAlive) {
            cout << i + 1 << ". " << CYAN << countries[i].name << RESET
                 << " | Health: " << GREEN << countries[i].health << RESET
                 << " | Troops: " << YELLOW << countries[i].troops << RESET
                 << " | Budget: $" << countries[i].budget << endl;
        } else {
            cout << i + 1 << ". " << countries[i].name << " | " << RED << "ELIMINATED" << RESET << endl;
        }
    }
}

void performAttack(int attackerIdx, int defenderIdx) {
    if (attackerIdx == defenderIdx || !countries[attackerIdx].isAlive || !countries[defenderIdx].isAlive) return;

    Country& attacker = countries[attackerIdx];
    Country& defender = countries[defenderIdx];

    cout << "\n" << RED << "[!] " << attacker.name << " is attacking " << defender.name << "!" << RESET << endl;

    int damage = (attacker.troops / 5) + (rand() % 10);
    int troopLossAttacker = (defender.troops / 10) + (rand() % 5);
    int troopLossDefender = (attacker.troops / 10) + (rand() % 5);

    defender.health -= damage;
    attacker.troops -= troopLossAttacker;
    defender.troops -= troopLossDefender;

    if (attacker.troops < 0) attacker.troops = 0;
    if (defender.troops < 0) defender.troops = 0;

    cout << ">>> Results: " << defender.name << " health -" << damage
         << " | " << attacker.name << " lost " << troopLossAttacker << " troops"
         << " | " << defender.name << " lost " << troopLossDefender << " troops" << endl;

    if (defender.health <= 0) {
        defender.health = 0;
        defender.isAlive = false;
        cout << BOLD << RED << "[!!!] " << defender.name << " HAS BEEN DEFEATED!" << RESET << endl;
        attacker.budget += 500; // Loot
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0)));
    initializeGame();

    cout << BOLD << BLUE << "--- EI-JACK LAB: WORLD WAR SIMULATOR V1.0 ---" << RESET << endl;
    cout << "(Hint: Type 'zen' to see the credits)" << endl << endl;

    cout << "Select your country:" << endl;
    for (size_t i = 0; i < countries.size(); ++i) {
        cout << i + 1 << ". " << countries[i].name << endl;
    }

    while (playerIndex < 0 || playerIndex >= (int)countries.size()) {
        cout << "Enter choice (1-" << countries.size() << "): ";
        string input;
        cin >> input;
        try {
            playerIndex = stoi(input) - 1;
        } catch (...) {
            cout << "Invalid input." << endl;
        }
    }

    cout << "\nYou have chosen " << countries[playerIndex].name << "!" << endl;

    bool gameOver = false;
    int turn = 1;

    while (!gameOver) {
        cout << "\n========== TURN " << turn << " ==========" << endl;
        showStats();

        if (!countries[playerIndex].isAlive) {
            cout << "\n[!] YOUR COUNTRY HAS BEEN CONQUERED. GAME OVER." << endl;
            gameOver = true;
            break;
        }

        // Player turn logic
        bool turnEnded = false;
        while (!turnEnded) {
            cout << "\nActions: 1. Attack  2. Recruit (Cost $100)  3. Pass  4. Special" << endl;
            cout << "Choice: ";
            string choice;
            cin >> choice;

            if (choice == "1") {
                cout << "Select target index: ";
                int target;
                if (!(cin >> target)) {
                    cout << "Invalid input. Please enter a number." << endl;
                    cin.clear();
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    continue;
                }
                target--;
                if (target >= 0 && target < (int)countries.size() && countries[target].isAlive && target != playerIndex) {
                    performAttack(playerIndex, target);
                    turnEnded = true;
                } else {
                    cout << "Invalid target!" << endl;
                }
            } else if (choice == "2") {
                if (countries[playerIndex].budget >= 100) {
                    countries[playerIndex].budget -= 100;
                    countries[playerIndex].troops += 20;
                    cout << "[+] Recruited 20 more troops!" << endl;
                    turnEnded = true;
                } else {
                    cout << "[!] Not enough budget!" << endl;
                }
            } else if (choice == "3") {
                cout << "[*] You passed your turn." << endl;
                turnEnded = true;
            } else if (choice == "4" || choice == "zen" || choice == "ZEN") {
                if (choice == "zen" || choice == "ZEN") {
                    showEasterEgg();
                } else {
                    cout << "[*] Special action: Economic Boost! (Cost $200)" << endl;
                    if (countries[playerIndex].budget >= 200) {
                        countries[playerIndex].budget -= 200;
                        countries[playerIndex].health += 10;
                        if (countries[playerIndex].health > 100) countries[playerIndex].health = 100;
                        cout << "[+] Health restored!" << endl;
                        turnEnded = true;
                    } else {
                        cout << "[!] Not enough budget!" << endl;
                    }
                }
            } else {
                cout << "Invalid choice." << endl;
            }
        }

        // Give budget to player too
        countries[playerIndex].budget += 50;

        // Random Event
        if (rand() % 5 == 0) {
            int event = rand() % 3;
            int affected = rand() % countries.size();
            if (countries[affected].isAlive) {
                if (event == 0) {
                    cout << "\n" << GREEN << "[EVENT] Economic Boom in " << countries[affected].name << "! (+$100)" << RESET << endl;
                    countries[affected].budget += 100;
                } else if (event == 1) {
                    cout << "\n" << RED << "[EVENT] Plague in " << countries[affected].name << "! (-10 Health)" << RESET << endl;
                    countries[affected].health -= 10;
                    if (countries[affected].health <= 0) {
                        countries[affected].health = 0;
                        countries[affected].isAlive = false;
                        cout << BOLD << RED << "[!!!] " << countries[affected].name << " HAS DIED FROM THE PLAGUE!" << RESET << endl;
                    }
                } else {
                    cout << "\n" << YELLOW << "[EVENT] Desertion in " << countries[affected].name << "! (-10 Troops)" << RESET << endl;
                    countries[affected].troops -= 10;
                    if (countries[affected].troops < 0) countries[affected].troops = 0;
                }
            }
        }

        // AI turn logic
        for (size_t i = 0; i < countries.size(); ++i) {
            if (i == (size_t)playerIndex || !countries[i].isAlive) continue;

            // Simple AI: randomly decide to attack or recruit
            int action = rand() % 3;
            if (action == 0) { // Attack
                int target;
                do {
                    target = rand() % countries.size();
                } while (target == (int)i || !countries[target].isAlive);
                performAttack(i, target);
            } else if (action == 1) { // Recruit
                int cost = 100;
                if (countries[i].budget >= cost) {
                    countries[i].budget -= cost;
                    countries[i].troops += 15;
                }
            }
            // Give some budget each turn
            countries[i].budget += 50;
        }

        // Check win/loss conditions
        int aliveCount = 0;
        for (const auto& c : countries) {
            if (c.isAlive) aliveCount++;
        }

        if (aliveCount == 1 && countries[playerIndex].isAlive) {
            cout << "\n[!!!] CONGRATULATIONS! " << countries[playerIndex].name << " HAS CONQUERED THE WORLD!" << endl;
            gameOver = true;
        } else if (aliveCount == 0) {
            cout << "\n[!] EVERYONE IS DEAD. NO WINNERS." << endl;
            gameOver = true;
        }

        turn++;
        if (turn > 100) {
            cout << "\n[!] THE WAR HAS DRAGGED ON FOR TOO LONG. STALEMATE." << endl;
            gameOver = true;
        }
    }

    cout << "----------------------------------------" << endl;
    return 0;
}
