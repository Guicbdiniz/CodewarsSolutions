# Maximum Length Difference

### [Link](https://www.codewars.com/kata/5663f5305102699bad000056)

You are given two arrays `a1` and `a2` of strings. Each string is composed with letters from `a` to `z`. Let `x` be any string in the first array and `y` be any string in the second array.

`Find max(abs(length(x) − length(y)))`

If `a1` and/or `a2` are empty return `-1` in each language except in Haskell (F#) where you will return `Nothing` (None).

### Example:
```py
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# mxdiflg(a1, a2) --> 13
```
