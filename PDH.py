#This is the Poorly Designed Hashing algorithm.
#It takes a 32-bit input and generates a 32-bit hash.
#This is intended for testing concepts, not for real world use.
from circuit import op, circuit
PDH = circuit()

#Similar to SHA256, the PDH splits the 32-bit input into four 8-bit segments to be manipulated.
rows = []
for a in range(4):
    row = []
    for b in range(8):
        row.append(PDH.gate(op.id_, is_input=True))
    rows.append(row)
bit0 = PDH.gate(op.nf_) #Boolean False
bit1 = PDH.gate(op.nt_) #Boolean True
rows.append([bit1,bit0,bit0,bit1,bit0,bit0,bit0,bit1]) #The next row is filled in for extra 1s and 0s.
for x in range(20):
    a0 = [] #This will be the result of ((rows[-2] shift right 2) XOR (rows[-2] rotate right 5))
    row = [] #This is the placeholder for the next 8-bit row.
    carry = [] #The final entry is whether or not a 1 is carried from addition.
    a0.append(rows[-2][3])
    a0.append(rows[-2][4])
    for a in range(2,8):
        a0.append(PDH.gate(op.xor_, [rows[-2][a-2], rows[-2][a-5]]))
    for b in range(8): #The new 8-bit row is the sum of a0 and rows[-5].
        if (b==0): #There are no carries yet to check against.
            row.append(PDH.gate(op.xor_, [a0[7-b],rows[-5][7-b]]))
            carry.append(PDH.gate(op.and_, [a0[7-b],rows[-5][7-b]]))
        elif (b<7):
            extra = PDH.gate(op.xor_, [a0[7-b],rows[-5][7-b]])
            row.append(PDH.gate(op.xor_, [extra,carry[-1]]))
            carry.append(PDH.gate(op.and_, [a0[7-b],rows[-5][7-b]]))
            carry.append(PDH.gate(op.and_, [rows[-5][7-b],carry[-2]]))
            carry.append(PDH.gate(op.and_, [a0[7-b],carry[-3]]))
            carry.append(PDH.gate(op.or_, [carry[-3],carry[-2]]))
            carry.append(PDH.gate(op.or_, [carry[-2],carry[-1]])) #The final entry is whether or not a 1 is carried over.
        else: #No need to check for carries at the final bit.
            extra = PDH.gate(op.xor_, [a0[7-b],rows[-5][7-b]])
            row.append(PDH.gate(op.xor_, [extra,carry[-1]]))
    row.reverse() #The bits were generated starting from the end.
    rows.append(row)
    
output = []
for row in rows[21:25]: #The final 32 bits constitute the output hash.
    for each in row:
        output.append(PDH.gate(op.id_, [each], is_output=True))
