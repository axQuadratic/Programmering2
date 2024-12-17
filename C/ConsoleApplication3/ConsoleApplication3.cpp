#include <iostream>
#include <string>

char consonants[] = {
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z'
};

static std::string translateToRobberLanguage(std::string input)
{
    char originalString[1024];
    char modifiedString[1024] = {};
    strcpy_s(originalString, 1024, input.c_str());

    int modifiedPointer = 0;
    for (int i = 0; i < std::size(originalString); i++)
    {
        for (char consonant : consonants)
        {
            if (originalString[i] == consonant)
            {
                modifiedString[modifiedPointer] = originalString[i];
                modifiedPointer++;
                modifiedString[modifiedPointer] = 'o';
                modifiedPointer++;
                modifiedString[modifiedPointer] = originalString[i];
            }
            else
            {
                modifiedString[modifiedPointer] = originalString[i];
            }
        }

        modifiedPointer++;
    }

    return modifiedString;
}

int main()
{
    std::string input = "";
    std::cout << "Input a sentence to translate to the Robber Language.\n";
    std::cout << "Robber Language (C) 1853-2024 Nils K., all rights reserved.\n";
    std::getline(std::cin, input);

    std::cout << translateToRobberLanguage(input);
}
