#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include "utils.cpp"

static enum Opcode {
    DAT, MOV, ADD, SUB, MUL, DIV, MOD, JMP, JMZ, JMN, DJN, SPL, CMP, SEQ, SNE, SLT, LDP, STP, NOP
};

static enum Modifier {
    Immediate, Direct, AIndirect, BIndirect, AIndirectPreDec, BIndirectPreDec, AIndirectPostInc, BIndirectPostInc
};

struct {
    int CORESIZE {};
} constants;

std::string labels[100] {};

class Instruction {
    std::string label {};
    Opcode opcode {};
    Modifier aMod {};
    Modifier bMod {};
    int aField {};
    int bField {};
};

int main() {
    constants.CORESIZE = 8000;
    Instruction instruction {};
    std::string input {};
    std::stringstream inputStream {};
    std::string params[10] {};

    std::cout << "== TAILWIND REDCODE COMPILER ==\n\nInput: ";
    std::getline(std::cin, input);

    inputStream << input;

    std::string segment;
    int i {};
    while(std::getline(inputStream, segment, ' ')) {
        if (segment != " " && segment != "\t")
            params[i] = segment;
        i++;

        if (i > 9) {
            throwError("Too many attributes!");
            return 1;
        }
    }

    // Check if first attribute exists in opcode array; if not assume it is a label
    if (std::find(std::begin(opcodes), std::end(opcodes), params[0]) != std::end(opcodes))
        std::cout << params[0];
}