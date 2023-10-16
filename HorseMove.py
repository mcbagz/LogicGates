h = circuit()
#First 13 bits is the current state of the game
g0 = h.gate(op.id_, is_input=True) #which horse is moving, 0 or 1

#The x and y coordinates of horse 0
g2 = h.gate(op.id_, is_input=True)
g3 = h.gate(op.id_, is_input=True)
g4 = h.gate(op.id_, is_input=True)

g5 = h.gate(op.id_, is_input=True)
g6 = h.gate(op.id_, is_input=True)
g7 = h.gate(op.id_, is_input=True)

#The x and y coordinates of horse 1
g9 = h.gate(op.id_, is_input=True)
g10 = h.gate(op.id_, is_input=True)
g11 = h.gate(op.id_, is_input=True)

g12 = h.gate(op.id_, is_input=True)
g13 = h.gate(op.id_, is_input=True)
g14 = h.gate(op.id_, is_input=True)

#Next six bits are the proposed move. First bit is forward or backward, then the change to x coord. Same for y.
g15 = h.gate(op.id_, is_input=True)
g16 = h.gate(op.id_, is_input=True)
g17 = h.gate(op.id_, is_input=True)

g18 = h.gate(op.id_, is_input=True)
g19 = h.gate(op.id_, is_input=True)
g20 = h.gate(op.id_, is_input=True)

#Check if the proposed move is of the proper shape: 2 spaces in one direction and 1 space in the other.
g21 = h.gate(op.xor_, [g16, g17])
g22 = h.gate(op.xor_, [g19, g20])
g23 = h.gate(op.and_, [g21, g22])
g24 = h.gate(op.xor_, [g16, g19])
g25 = h.gate(op.xor_, [g17, g20])
g26 = h.gate(op.and_, [g24, g25])
g27 = h.gate(op.and_, [g23, g26]) #Horse is moving 2 spaces in one direction and 1 space in the other.

#Check if the proposed move is valid, in that it does not go outside of the bounds of the board.
#First check the x direction
g28 = h.gate(op.xnor_, [g2, g15])
g29 = h.gate(op.xnor_, [g2, g3])
g30 = h.gate(op.and_, [g28, g29]) #Horse is in either the front two positions moving forward or back two moving backwards

g31 = h.gate(op.and_, [g30, g16]) #Illegal move
g32 = h.gate(op.xnor_, [g3, g4])
g33 = h.gate(op.and_, [g30, g32]) #Illegal move

g34 = h.gate(op.nor_, [g31, g33]) #Neither of those two illegal moves.

#Next check the y direction
g35 = h.gate(op.xnor_, [g5, g18])
g36 = h.gate(op.xnor_, [g5, g6])
g37 = h.gate(op.and_, [g35, g36]) #Horse is in either the front two positions moving forward or back two moving backwards

g38 = h.gate(op.and_, [g37, g19]) #Illegal move
g39 = h.gate(op.xnor_, [g6, g7])
g40 = h.gate(op.and_, [g37, g39]) #Illegal move

g41 = h.gate(op.nor_, [g38, g40]) #Neither of those two illegal moves.

g42 = h.gate(op.and_, [g34, g41]) #Move is legitimate for horse 0.

#Repeat above for horse 1.
#First check the x direction
g43 = h.gate(op.xnor_, [g9, g15])
g44 = h.gate(op.xnor_, [g9, g10])
g45 = h.gate(op.and_, [g43, g44]) #Horse is in either the front two positions moving forward or back two moving backwards

g46 = h.gate(op.and_, [g45, g16]) #Illegal move
g47 = h.gate(op.xnor_, [g10, g11])
g48 = h.gate(op.and_, [g45, g47]) #Illegal move

g49 = h.gate(op.nor_, [g46, g48]) #Neither of those two illegal moves.

#Next check the y direction
g50 = h.gate(op.xnor_, [g12, g18])
g51 = h.gate(op.xnor_, [g12, g13])
g52 = h.gate(op.and_, [g50, g51]) #Horse is in either the front two positions moving forward or back two moving backwards

g53 = h.gate(op.and_, [g52, g19]) #Illegal move
g54 = h.gate(op.xnor_, [g13, g14])
g55 = h.gate(op.and_, [g52, g54]) #Illegal move

g56 = h.gate(op.nor_, [g53, g55]) #Neither of those two illegal moves.

g57 = h.gate(op.and_, [g49, g56]) #Move is legitimate for horse 1.

g58 = h.gate(op.not_, [g0])
g59 = h.gate(op.and_, [g0, g57])
g60 = h.gate(op.and_, [g58, g42])
g61 = h.gate(op.or_, [g59, g60]) #Move is legitimate for selected horse.
g62 = h.gate(op.and_, [g27, g61]) #Move is proper shape and legitimate.

g63 = h.gate(op.id_, [g62], is_output=True) #1 is a successful move, 0 is not successful.
