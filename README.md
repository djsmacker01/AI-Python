# My AI/ML & Python Learning Journey

Hey! Welcome to my repo. This is basically where I document everything I'm learning as I work through Python, AI, and Machine Learning. It's not a polished library or a finished product — it's more like my personal notebook, just written in code.

If you're here, you're probably curious about what I've been building and experimenting with. Let me walk you through it.

---

## What This Repo Is About

I started this to get serious about Python and actually understand how AI and ML work under the hood — not just copy-paste tutorials, but really get my hands dirty. So everything in here is stuff I've personally written, broken, fixed, and learned from.

The repo covers a few things:

- **Core Python practice** — the basics that make everything else possible
- **Building small useful programs** — actual mini-apps I built from scratch
- **AI/LLM interaction** — experimenting with how to send prompts and get responses
- **Data handling for ML** — cleaning data, dealing with missing values, the unglamorous stuff that real ML actually needs

---

## What's Inside

### `basic_variables.py`
Where it all started. This file is me practising Python fundamentals — variables, user input, lists, loops, dictionaries. Nothing fancy, but you have to walk before you run. I was exploring things like how to loop through a list of fruits, how to store a tech stack, how to work with dictionaries. The commented-out lines are things I tried and kept for reference.

### `data.py`
A quick file I used to get comfortable with Python data types. Just printing things, checking types, understanding how Python thinks about data. Short and simple, but it was a useful starting point.

### `GuessNumber.py`
This one is actually fun. I built a number guessing game — the computer picks a random number between 1 and 10, and you have to guess it. It tells you if you're too high, too low, and then congratulates you when you get it right. It also tracks how many guesses it took. Good practice for `while` loops, conditionals, and the `random` module.

### `helper_functions.py`
This is where things get interesting. I built a function called `print_llm_response()` that simulates how a language model would respond to a prompt. It's a rule-based system that handles questions about capital cities, basic facts, and simple maths. I wanted to understand the *structure* of LLM interaction — input a prompt, get a response — before working with actual APIs. It's essentially me building a tiny knowledge base from scratch.

### `llm_prompt_response.py`
This file uses the helper function I wrote to send prompts and print responses. I asked it things like "What is the capital of Nigeria?", "What is Python?", and simple maths. It's a hands-on way to practice how prompts and responses work in AI systems, even with a custom-built response engine.

### `To_do_app`
A full CLI to-do list application. You can:
- View all your tasks
- Add a new task
- Remove a task by number
- Quit the app

This one taught me a lot about structuring a program with multiple functions, handling user input properly, and dealing with errors (like when someone types a letter instead of a number). It was a proper mini-project.

### `Handling_missing_value/`
This is my ML documentation folder. Inside, there's a Jupyter notebook (`Missing_value.ipynb`) and a real dataset (`college_missing.csv`). I worked through how to identify, handle, and clean missing values in a dataset — which is one of the most common and important steps in any data science or ML pipeline. If your data is messy, your model will be too.

---

## Why I'm Doing This

Honestly? I want to understand AI and ML for real. Not just use tools that other people built, but actually know what's happening. Python is the language that makes that possible, so I'm building the foundation here — one script, one notebook, one idea at a time.

This repo is going to keep growing as I learn more. New projects, new experiments, more ML notebooks. It's a living record of the work.

---

## Tools & Tech

- **Python 3** — the main language for everything
- **Jupyter Notebooks** — for ML experiments and data work
- **Pandas / data libraries** — for data handling (in the notebook)
- `random` module — for the guessing game
- `requests` module — imported in helper functions for future API work

---

## Running the Projects

Most scripts just run with Python directly:

```bash
python GuessNumber.py
python llm_prompt_response.py
python To_do_app
```

For the Jupyter notebook:

```bash
jupyter notebook Handling_missing_value/Missing_value.ipynb
```

---

## A Note

This isn't meant to be perfect code. It's meant to be honest learning. Some files have commented-out lines where I was experimenting. Some things are simple on purpose because I was focused on understanding the concept, not showing off. If you're also learning, I hope seeing someone else's messy, real practice work makes it feel a bit less intimidating.

---

*— Nurudee Adedeji*
