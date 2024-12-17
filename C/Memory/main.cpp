#include <iostream>
#include <algorithm>
#include <array> 
#include <random>
#include <chrono>
#include <vector>

#include "constants.h"

void randomizeDeckOrder() {
    // Initialise the card list array; one card for each letter
    int k { 0 };
    for (int i { 0 }; i < sizeof(letters); i++) {
        deck[k] = Card { letters[i], false, false };
        deck[k + 1] = Card { letters[i], false, false };
        k += 2;
    }

    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    shuffle(std::begin(deck), std::end(deck), std::default_random_engine(seed));
}

void displayCurrentDeck() {
    int k { 0 };
    for (int i { 0 }; i < sizeof(deck) / sizeof(deck[0]); i++) {

        if (deck[i].isRemoved) {
            std::cout << "\x1B[32m[+]\033[0m ";
        }
        else if (deck[i].isFlipped) {
            std::cout << "\x1B[94m[" << deck[i].value << "]\033[0m ";
        }
        else {
            std::cout << "[?] ";
        }

        k++;
        if (k >= maxTableWidth) {
            k = 0; std::cout << "\n";
        }
    }
}

void selectTile(int row, int column) {
    deck[maxTableWidth * (row - 1) + (column - 1)].isFlipped = true;
    flippedPositions.push_back(maxTableWidth * (row - 1) + (column - 1));
}

int main() {
    randomizeDeckOrder();
    displayCurrentDeck();
    while (true) {
        system("cls");
        displayCurrentDeck();
        if (flippedPositions.size() >= 2) {
            if (deck[flippedPositions[0]].value == deck[flippedPositions[1]].value) {
                deck[flippedPositions[0]].isRemoved = true; deck[flippedPositions[1]].isRemoved = true;
                flippedPositions = {};
                std::cout << "It is a match!\n";
            }
            else {
                deck[flippedPositions[0]].isFlipped = false; deck[flippedPositions[1]].isFlipped = false;
            }

            flippedPositions = {};
            system("pause");
            continue;
        }

        std::cout << "Input two numbers in the format '<row> <col>' to flip a card...\n";
        // Exploiting behaviour of cin to get two values
        int row {}; int column {};
        std::cin >> row >> column;

        selectTile(row, column);
    }

    system("pause");
}
