#The purpose of these circuits is to create logic circuits for two of the building blocks of the sha256 algorithm.
#The inputs and outputs of each of these circuits are 32-bit numbers. 
#The next step of the algorithm is to add them together and to two other 32-bit numbers, but I believe OP_ADD would be more efficient than recreating addition with logic gates.
from circuit import op, circuit

#For the first part, a 32-bit input is rotated 7 bits to the right(wrapping), rotated 18 bits to the right(wrapping), and shifted 3 bits to the right(non-wrapping).
#The output is the XOR of the bits in all three of those numbers.
s0 = circuit()
s0_input = []
xor = []
s0_output = []
#Take a 32-bit number as the input.
for a in range(32):
    s0_input.append(s0.gate(op.id_, is_input=True))

for i in range(3):
    #For efficiency, the first 3 bits of the output is the XOR of the two rotated numbers.
    s0_output.append(s0.gate(op.xor_, [s0_input[i-7],s0_input[i-18]]))
for i in range(3,32):
    xor.append(s0.gate(op.xor_, [s0_input[i-7],s0_input[i-18]]))
    s0_output.append(s0.gate(op.xor_, [s0_input[i-3],xor[-1]]))

#The circuit module will only allow 'id' gates to be the output
for each in s0_output:
    s0.gate(op.id_, [each], is_output=True)

#For the next step, a 32-bit input is rotated 17 bits to the right(wrapping), rotated 19 bits to the right(wrapping), and shifted 10 bits to the right(non-wrapping).
#The output is the XOR of the bits in all three of those numbers.
s1 = circuit()
s1_input = []
xor = []
s1_output = []
#Take a 32-bit number as the input.
for a in range(32):
    s1_input.append(s1.gate(op.id_, is_input=True))

for i in range(10):
    #For efficiency, the first 10 bits of the output is the XOR of the two rotated numbers.
    s1_output.append(s1.gate(op.xor_, [s1_input[i-17],s1_input[i-19]]))
for i in range(10,32):
    xor.append(s1.gate(op.xor_, [s1_input[i-17],s1_input[i-19]]))
    s1_output.append(s1.gate(op.xor_, [s1_input[i-10],xor[-1]]))

#The circuit module will only allow 'id' gates to be the output
for each in s1_output:
    s1.gate(op.id_, [each], is_output=True)
