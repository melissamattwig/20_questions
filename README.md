# 20 Questions game for SI 507 at the University of Michigan
A python program that plays a game akin to 20 questions with the user

## Table of contents
* [General info](#general-info)
* [Skills gained](#skills-gained)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project implements a 20 questions game based on user input. The user will think of a secret object and the program will try to guess the object. If the program guesses incorrectly, it will ask for user input to learn about the secret object. Thus the program will improve as it is played.

The user will have an option to load a tree file from a previously played game. If a file is not loaded, the game will start with a basic tree of questions. Each time the game is played, the user will have the option to save the tree file from that game in order to play again. 

## Skills gained
* Use of trees with tuples of tuples
* Loading in files and saving new files
* Implementation of user input

## Technologies
Project is created with:
* Visual Studio Code version 1.76.2
* Python 3.10
	
## Setup
To run this project:

```
$ cd ../20_questions
$ python3 20_questions.py
```
