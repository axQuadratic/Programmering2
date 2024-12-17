// ConsoleApplication2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <ctime>
#include <thread>
#include <chrono>
#include <bitset>
#include <string>

enum AnswerTypes
{
    YesAnswer,
    NoAnswer,
    UncertainAnswer
};

std::string yesAnswers[] = {
    "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
    "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes"
};
std::string uncertainAnswers[] = {
    "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"
};
std::string noAnswers[] = {
    "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"
};

int main()
{
    std::string input = "";
    std::cout << "Please input a question for the great Magic 8 Ball.\n";
    std::cin >> input;
    std::cout << "The Ball is processing your query... ";
    
    std::string inputBinary = "";
    for (char c : input)
    {
        inputBinary += std::bitset<8>(c).to_string();
    }
    
    int inputNumber = std::stoi(inputBinary, nullptr, 2);

    std::srand(inputNumber);
    AnswerTypes answerType = static_cast<AnswerTypes>(std::rand() % 3);

    std::this_thread::sleep_for(std::chrono::seconds((std::rand() + 1) % 5));

    std::string answer = "";
    switch (answerType)
    {
        case YesAnswer:
            answer = yesAnswers[std::rand() % std::size(yesAnswers)];
            break;
        case UncertainAnswer:
            answer = uncertainAnswers[std::rand() % std::size(uncertainAnswers)];
            break;
        case NoAnswer:
            answer = noAnswers[std::rand() % std::size(noAnswers)];
            break;
    }

    std::cout << answer;
};