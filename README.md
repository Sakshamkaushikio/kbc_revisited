# KBC Quiz Game – Python (Revisited)

A simple command-line **Kaun Banega Crorepati (KBC)** quiz game built using Python.

I originally created this project while learning Python fundamentals. I have revisited the project to practise loops, nested loops, conditional statements, list operations, input validation, and loop control.

## About the Project

The game presents 10 general knowledge questions, each with four multiple-choice options.

- Each correct answer earns ₹10,000.
- The game continues if the player answers correctly.
- An incorrect answer ends the game.
- Invalid inputs are rejected, and the player is asked to enter their choice again.
- The correct answers are stored separately within each question and are not displayed to the player.

## Concepts Practised

1. **Nested Lists:** Storing questions, options, and correct answers inside individual lists.
2. **For Loops:** Iterating through the collection of questions.
3. **Nested For Loops:** Displaying questions and their multiple-choice options.
4. **List Slicing:** Using `i[0:5]` to display only the question and four options while keeping the correct answer hidden.
5. **While Loops:** Repeatedly asking for input until a valid option is entered.
6. **Conditional Statements:** Checking whether the selected answer is correct.
7. **Input Handling:** Using `.strip()` and `.casefold()` to handle whitespace and uppercase/lowercase inputs.
8. **Break:** Exiting the inner loop after valid input and ending the quiz after an incorrect answer.
9. **Variables and Accumulation:** Maintaining the player's total winnings.

## Previous Version vs. Revisited Version

This project has two versions:

**Older Version:**
- Used separate lists for questions and answers.
- Used a `while` loop with a counter to iterate through questions.
- Awarded ₹1,000 per correct answer.

**Revisited Version:**
- Uses nested lists to store each question, its options, and its correct answer together.
- Uses a `for` loop to iterate through questions.
- Uses an inner `for` loop to display question options.
- Uses list slicing to hide the correct answer.
- Uses a `while` loop for input validation.
- Awards ₹10,000 per correct answer.

## How to Run

1. Make sure Python is installed.
2. Clone this repository or download the project.
3. Open the project directory in your terminal.
4. Run:

```bash
python kbc_revisited.py
```

## Purpose

The purpose of revisiting this project was to reinforce my understanding of Python fundamentals and explore alternative ways of solving the same problem.

This is part of my ongoing Python learning journey.