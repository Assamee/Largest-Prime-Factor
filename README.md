# Project Euler: Largest Prime Factor

An efficient Python solution for [Project Euler Problem 3](https://projecteuler.net/problem=3): *"What is the largest prime factor of the number 600,851,475,143?"*

## 🚀 Overview
This project implements a **Trial Division algorithm** to decompose large composite integers into their prime factors. Unlike naive iteration which checks factors up to $N$, this solution leverages square-root bounding and iterative reduction to handle large datasets with minimal latency.

## ⚙️ Technical Approach

### 1. Iterative Factor Reduction
**The Concept:** The Fundamental Theorem of Arithmetic.
**The Implementation:**
Every time a factor `i` is found, the target number `num` is updated to `num // i`.
* **Result:** This ensures that subsequent factors found are guaranteed to be prime (since all smaller composite factors have already been divided out). It also rapidly shrinks the magnitude of the number being processed.

### 2. Search Space Pruning (Square Root Bound)
**The Concept:** A composite number $N$ must have a factor less than or equal to $\sqrt{N}$.
**The Implementation:**
The loop constraint is calculated as `int(num**0.5) + 1` rather than iterating up to `num`.
* **Result:** drastically reduces the time complexity from $O(N)$ to approximately $O(\sqrt{N})$, transforming an impossible brute-force calculation into a sub-second operation.

## ⏱️ Performance
* **Language:** Python 3.x
* **Algorithm:** Optimised Trial Division.
* **Outcome:** Solves for the 12-digit input `600,851,475,143` almost instantly by aggressively pruning the candidate pool.

## 💻 Usage
Run the script directly from the terminal:

```bash
python3 "Largest Prime Factor.py"
