# Poker cards encoder/decoder

Consider a deck of 52 cards, which are represented by a string containing their suit and face value.

Your task is to write two functions encode and decode that translate an array of cards to/from an array of integer codes.

- function `encode`:  
    input: array of strings (symbols)  
    output: array of integers (codes) sorted in ascending order

- function `decode`:  
    input: array of integers (codes)   
    output: array of strings (symbols) sorted by code values 

The returned array must be sorted from lowest to highest priority (value or precedence order, see below).