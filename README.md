# SER502: Group Project

## Lexar Programming Language

### Group 32

### Team Members:

- Aditya Soude (ASU ID- 1233364979)
- Savankumar Pethani (ASU ID- 1233436310)
- Vidhisha Amle (ASU ID- 1233138272)
- Charu Sneha (ASU ID-1233592505)

## Description:

QuirkScript is a playful, creatively designed programming language that embraces humor and simplicity while maintaining the ability to perform essential programming tasks. Featuring unconventional syntax, quirky keywords, and a fun approach to code execution, QuirkScript makes programming an entertaining experience.

## Supporting Platform:

Windows and Mac

### Purpose

QuirkScript aims to make programming feel less intimidating and more enjoyable. Whether you're a beginner or an experienced coder, this language will challenge conventions while keeping things amusing.

### Features

- **Quirky Data Types & Operators**
  - `yep` and `nope` for Boolean values, supporting `meh`, `uh-huh`, and `no-way` as logical operators.
  - Numeric types (`num`, `big-num`) supporting operations like `plus`, `minus`, `times`, and `divide-by`.
  - Relational operators (`way-bigger`, `way-smaller`, `same-same`).
  - String assignments with `say = "Hello!"`.
- **Assignment & Control Flow**
  - Variable assignment using `lemme =`.
  - Conditional constructs:
    - Ternary operator (`if-yes : do-this ? otherwise-do-this`).
    - Traditional `if-maybe-else` structure.
- **Looping Constructs**
  - `keep-doing` loop (while loop variant).
  - `loopity-loop` (for loop variant).
- **Printing Output**
  - `shout()` construct for displaying values of all supported types.
- **Development Tools**
  - Built with open-source tools such as `cmake`, `make`, `ant`, or `qmake`.
  - No proprietary tools are required for compilation and execution.
- **Command-line Execution**
  - The interpreter or compiler is invoked via the command-line using a single argument, e.g.:
    ```sh
    ./obj/quirkscript Data/HelloWorld.qs
    ```
    or (if written in Java):
    ```sh
    java -cp classes quirk.Main HelloWorld.qs
    ```

## Required Tools

To build and run QuirkScript, you need the following tools:

- **Compiler/Interpreter Development:**
  - C++ or Java (for lexer, parser, and runtime implementation)
  - Flex & Bison (for lexical analysis and parsing in C++)
  - ANTLR (for parsing if implemented in Java)
- **Build System:**
  - CMake, Make, Ant, or QMake (to manage builds and dependencies)
- **Version Control:**
  - Git and GitHub (for collaboration and source code management)
- **Testing Frameworks:**
  - Google Test (for C++) or JUnit (for Java) to validate language behavior
- **Text Editor/IDE:**
  - VS Code, CLion, IntelliJ IDEA, or any preferred development environment
- **Command-Line Interface:**
  - Terminal, PowerShell, or Command Prompt for executing QuirkScript programs
