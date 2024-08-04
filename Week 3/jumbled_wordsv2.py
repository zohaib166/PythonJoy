# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:14:09 2024

This is a game where two players have to guess the correct word from a jumbled word
version 2

@author: Zohaib
"""

import random

def choose():
    word_bank = []
    with open("word_bank.csv", "r") as f:
        word_bank = f.read().split(",")
    return random.choice(word_bank)

def jumbled(word):
    q_word = "".join(random.sample(word, len(word)))
    return q_word


def play():
    p1_name = input("Enter Player 1 Name: ")
    p2_name = input("Enter Player 2 Name: ")
    
    turn = 0
    p1_score = p2_score = 0
    
    while 1:
        # Generate and display a jumbled word
        correct_word = choose()
        question_word = jumbled(correct_word)
        print(question_word)
        if turn%2 == 0:
            print(p1_name, "your turn")
            p1_guess = input("Guess the correct word: ")
            if(p1_guess == correct_word):
                p1_score += 1
                print("Your score is ", p1_score)
            else:
                print("Wrong!!! The correct word is", correct_word)
        else:
            print(p2_name, "your turn")
            p2_guess = input("Guess the correct word: ")
            if(p2_guess == correct_word):
                p2_score += 1
                print("Your score is ", p2_score)
            else:
                print("Wrong!!! The correct word is", correct_word)
        turn += 1
        
        c = input("Do you want to continue, y for yes and n for no: ")
        if c=='n':
            print("Thanks for playing")
            print(p1_name,"Score:", p1_score)
            print(p2_name,"Score:", p2_score)
            break
            

play()