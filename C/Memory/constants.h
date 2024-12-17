#ifndef CONSTANTS_H
#define CONSTANTS_H

struct Card
{
    char value {};
    bool isFlipped {};
    bool isRemoved {};
};

char letters[] {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'
};

Card deck[sizeof(letters) * 2] {};
std::vector<int> flippedPositions {};

const int maxTableWidth { 4 };

#endif