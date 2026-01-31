## Data Generator

A small, focused Python utility that generates mock user data for development and testing.

The script produces usernames, emails, Indonesian-style phone numbers, and strong random passwords from a single name input.

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

---
