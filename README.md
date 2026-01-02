## Data Generator

A small, focused Python utility that generates mock user data for development and testing.
The script produces usernames, emails, Indonesian-style phone numbers, and strong random passwords from a single name input.

This project is intentionally minimal and dependency-free, making it easy to audit, extend, or embed into larger tooling.

---

## Description

This repository contains a single Python script, [`main.py`](./main.py), that demonstrates clean separation of concerns for generating synthetic user data. It is suitable for local testing, demos, seed data generation, or quick prototyping where realistic—but fake—credentials are needed.

The script favors clarity over abstraction and uses only Python’s standard library.

---

## Techniques Used

* **Deterministic string normalization**
  Usernames are derived from normalized input (`lower()` and whitespace removal) to ensure predictable base identifiers.
  Python reference:
  [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

* **Randomized suffix generation**
  Numeric suffixes are appended using `random.randint` to reduce collisions while remaining human-readable.
  Python reference:
  [https://docs.python.org/3/library/random.html#random.randint](https://docs.python.org/3/library/random.html#random.randint)

* **Random selection from constrained sets**
  Email domains are chosen via `random.choice`, keeping output realistic without external configuration.
  Python reference:
  [https://docs.python.org/3/library/random.html#random.choice](https://docs.python.org/3/library/random.html#random.choice)

* **Variable-length data generation**
  Phone numbers use randomized digit lengths to better simulate real-world inconsistencies.
  Python reference:
  [https://docs.python.org/3/library/random.html#random.choices](https://docs.python.org/3/library/random.html#random.choices)

* **Password entropy composition**
  Passwords are built from mixed character classes (letters, digits, symbols) using a configurable length.
  Python reference:
  [https://docs.python.org/3/library/string.html](https://docs.python.org/3/library/string.html)

* **Clear functional boundaries**
  Each generator is implemented as a pure function, making the code easy to test, reuse, or refactor.

---

## Technologies and Libraries of Interest

While no third-party dependencies are used, the script makes effective use of less-obvious parts of the Python standard library:

* **`random`**
  Pseudo-random generation for controlled variability
  [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)

* **`string`**
  Predefined character sets for safer and clearer password construction
  [https://docs.python.org/3/library/string.html](https://docs.python.org/3/library/string.html)

No external libraries, frameworks, or fonts are used in this project.

---

## Project Structure

```text
.
├── main.py
```

**Notes**

* `main.py`
  Contains all generator utilities and the CLI entry point.