# Matrix Multiplication from Scratch

**C++ · no external libraries**

A program that multiplies any two matrices with compatible dimensions, written while I was teaching myself linear algebra so I could understand the computation itself rather than relying on a library.

## How it works

Two matrices can be multiplied when the number of columns in the first equals the number of rows in the second. Multiplying an (n × m) matrix **A** by an (m × p) matrix **B** gives an (n × p) matrix **C**, where each entry is:

> C[i][j] = Σₖ A[i][k] · B[k][j]  (for k = 1 to m)

In words: each entry of the result is the dot product of a row of **A** with a column of **B**.

## Development

1. **Started small.** I wrote out a 2 × 2 example by hand and in code to see the pattern.
2. **Generalized.** I turned that pattern into nested loops that work for any compatible dimensions.
3. **No shortcuts.** The program uses no external libraries or matrix packages. I paid attention to memory efficiency when storing the matrices.

## How to run

```
g++ -std=c++17 matrix_multiplication.cpp -o matrix_multiplication
./matrix_multiplication
```
