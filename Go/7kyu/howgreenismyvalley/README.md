# How Green Is My Valley?

- Input : an array of integers.

- Output : this array, but sorted in such a way that there are two wings:

  - the left wing with numbers decreasing,

  - the right wing with numbers increasing.

- the two wings have the same length. If the length of the array is odd the wings are around the bottom, if the length is even the bottom is considered to be part of the right wing.

- each integer l of the left wing must be greater or equal to its counterpart r in the right wing, the difference l - r being as small as possible. In other words the right wing must be nearly as steep as the left wing.