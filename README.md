## Sample output for now

![image](https://github.com/user-attachments/assets/6e6cd65c-2636-4187-91f0-5019db29f29a)

# SER502: Group Project

# BolBachchan Language

BolBachchan is a creative, humorous programming language that blends Hindi-English keywords with traditional programming constructs. Designed to be fun and expressive, it is backed by a custom lexer and parser written in Python using PLY (Python Lex-Yacc).

## 🎯 Project Purpose

To design and implement a custom programming language from scratch that supports standard programming features while incorporating Hinglish (Hindi-English) syntax.

## 🚀 Features

- 🧮 Primitive types: int, bool, string
- 🔢 Arithmetic operators: jodo (+), ghatao (-), guna (\*), bhaag (/)
- 🔍 Relational operators: badaHai (>), chhotaHai (<), barabarHai (==)
- 🔁 Loops: baarBaar (for), jabTak (while)
- ❓ Conditionals: agar-toh-nahiToh (if-then-else), ternary (? :)
- 📢 Output: bolBhai() prints any data type
- 🪄 Assignments: rakho keyword assigns values to variables
- 😎 Logical operators: & (and), | (or)

## 📁 Project Structure

```
SER502_QuirkScript_Team32/
├── src/
│   ├── lexer.py            # Tokenizer
│   ├── parser.py           # Parser with AST support
│   ├── main.py             # Entry point for execution
├── data/
│   └── Sample3.bb          # Test case covering all language constraints
├── doc/
│   ├── grammar.pdf         # Formal grammar in EBNF
│   └── contribution.txt    # Team contributions and plan
├── README.md               # Project overview and instructions
├── requirements.txt        # Python dependencies
```

## ⚙️ Setup Instructions

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the parser and view the parse tree:

```bash
python src/main.py data/Sample3.bb
```

## 🧪 Testing Language Constraints

Sample3.bb includes:

- All data types: int, bool, string
- Arithmetic, logical, and relational operators
- Ternary and if-else constructs
- for-loop and while-loop support
- Printing outputs with bolBhai

## 📄 Documentation

- Formal grammar: `doc/grammar.pdf`
- Team work log: `doc/contribution.txt`

## 💻 Tools Used

- Python 3.9+
- PLY (Python Lex-Yacc)
- Git/GitHub

---

Created with ❤️ by Team 32
