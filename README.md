# LogicGates
The intention of this repo is to build circuits with logic gates in Python for the inteded use in BitVM.

For a simple explanation and how-to, check out this video and example.ipynb :
https://www.youtube.com/watch?v=cnijtOVRwgg&ab_channel=BagzTech

HorseMove is the beginning of implementing chess rules.

Sha256Parts includes smaller aspects of the Sha256 hashing algorithm, which could be combined with other Bitcoin opcodes to recreate the function.

PDH is the Poorly Designed Hashing algorithm. It takes a 32-bit input and creates a 32-bit hash. My intention is to use this to build unsecure proof of concepts of merkle trees and other tools on Bitcoin. The reason this is 32 bits in input and output is that arithmetic can be done natively in Bitcoin script with 32-bit integers.
