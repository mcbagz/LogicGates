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
g27 = h.gate(op.and_, [g23, g26])

#Move the horse in the proposed move, and 
#First grab the coordinates for the selected horse
g28 = h.gate(op.and_, [g0, g9])
g29 = h.gate(op.and_, [g0, g10])
g30 = h.gate(op.and_, [g0, g11])
g31 = h.gate(op.and_, [g0, g12])
g32 = h.gate(op.and_, [g0, g13])
g33 = h.gate(op.and_, [g0, g14])
g34 = h.gate(op.not_, [g0])
g35 = h.gate(op.and_, [g2, g34])
g36 = h.gate(op.and_, [g3, g34])
g37 = h.gate(op.and_, [g4, g34])
g38 = h.gate(op.and_, [g5, g34])
g39 = h.gate(op.and_, [g6, g34])
g40 = h.gate(op.and_, [g7, g34])

g41 = h.gate(op.or_, [g28, g35]) #The three x coordinates
g42 = h.gate(op.or_, [g29, g36])
g43 = h.gate(op.or_, [g30, g37])
g44 = h.gate(op.or_, [g31, g38]) #The three y coordinates
g45 = h.gate(op.or_, [g32, g39])
g46 = h.gate(op.or_, [g33, g40])

#Add the move (moving forward), and check if it goes over
g47 = h.gate(op.xor_, [g17, g43]) #2^0 place x
g48 = h.gate(op.and_, [g17, g43]) #carry over
g49 = h.gate(op.or_, [g16, g48]) #is there either a movement of 2 or a carryover; impossible to have both
g50 = h.gate(op.xor_, [g42, g49]) #2^1 place x
g51 = h.gate(op.and_, [g42, g49]) #carry over
g52 = h.gate(op.xor_, [g41, g51]) #2^2 place x
g53 = h.gate(op.and_, [g41, g51]) #overflow, move is out of bounds
g54 = h.gate(op.and_, [g15, g53]) #move is illegal

g55 = h.gate(op.xor_, [g20, g46]) #2^0 place y
g56 = h.gate(op.and_, [g20, g46]) #carry over
g57 = h.gate(op.or_, [g19, g56]) #is there either a movement of 2 or a carryover; impossible to have both
g58 = h.gate(op.xor_, [g45, g57]) #2^1 place y
g59 = h.gate(op.and_, [g45, g57]) #carry over
g60 = h.gate(op.xor_, [g44, g59]) #2^2 place y
g61 = h.gate(op.and_, [g44, g59]) #overflow, move is out of bounds
g62 = h.gate(op.and_, [g18, g61]) #move is illegal

#Subtract the move (moving backward), and check if it goes under
g63 = h.gate(op.xor_, [g17, g43]) #2^0 place x
g64 = h.gate(op.not_, [g43])
g65 = h.gate(op.and_, [g17, g64]) #borrowed
g66 = h.gate(op.or_, [g16, g65]) #is there either a movement of 2 or a borrow; impossible to have both
g67 = h.gate(op.xor_, [g66, g42]) #2^1 place x
g68 = h.gate(op.not_, [g42])
g69 = h.gate(op.and_, [g66, g68]) #borrowed
g70 = h.gate(op.xor_, [g69, g41]) #2^2 place x
g71 = h.gate(op.not_, [g41])
g72 = h.gate(op.and_, [g69, g71]) #underflow, move is out of bounds
g73 = h.gate(op.not_, [g15])
g74 = h.gate(op.and_, [g72, g73]) #move is illegal


g75 = h.gate(op.xor_, [g20, g46]) #2^0 place y
g76 = h.gate(op.not_, [g46])
g77 = h.gate(op.and_, [g20, g76]) #borrowed
g78 = h.gate(op.or_, [g19, g77]) #is there either a movement of 2 or a borrow; impossible to have both
g79 = h.gate(op.xor_, [g78, g45]) #2^1 place y
g80 = h.gate(op.not_, [g45])
g81 = h.gate(op.and_, [g78, g80]) #borrowed
g82 = h.gate(op.xor_, [g81, g44]) #2^2 place y
g83 = h.gate(op.not_, [g44])
g84 = h.gate(op.and_, [g81, g83]) #underflow, move is out of bounds
g85 = h.gate(op.not_, [g18])
g86 = h.gate(op.and_, [g84, g85]) #move is illegal

#Select which x coordinates are correct based on forward/backward
g87 = h.gate(op.and_, [g15, g52])
g88 = h.gate(op.and_, [g15, g50])
g89 = h.gate(op.and_, [g15, g47])
g90 = h.gate(op.not_, [g15])
g91 = h.gate(op.and_, [g90, g70])
g92 = h.gate(op.and_, [g90, g67])
g93 = h.gate(op.and_, [g90, g63])

g94 = h.gate(op.or_, [g87, g91]) #The three x coordinates
g95 = h.gate(op.or_, [g88, g92])
g96 = h.gate(op.or_, [g89, g93])

g97 = h.gate(op.and_, [g18, g60])
g98 = h.gate(op.and_, [g18, g58])
g99 = h.gate(op.and_, [g18, g55])
g100 = h.gate(op.not_, [g18])
g101 = h.gate(op.and_, [g100, g82])
g102 = h.gate(op.and_, [g100, g79])
g103 = h.gate(op.and_, [g100, g75])

g104 = h.gate(op.or_, [g97, g101]) #The three y coordinates
g105 = h.gate(op.or_, [g98, g102])
g106 = h.gate(op.or_, [g99, g103])

#Grab the coordinates for the opposing horse and check if they line up. If so, the game is won.
g107 = h.gate(op.and_, [g0, g2])
g108 = h.gate(op.and_, [g0, g3])
g109 = h.gate(op.and_, [g0, g4])
g110 = h.gate(op.and_, [g0, g5])
g111 = h.gate(op.and_, [g0, g6])
g112 = h.gate(op.and_, [g0, g7])
g113 = h.gate(op.not_, [g0])
g114 = h.gate(op.and_, [g9, g113])
g115 = h.gate(op.and_, [g10, g113])
g116 = h.gate(op.and_, [g11, g113])
g117 = h.gate(op.and_, [g12, g113])
g118 = h.gate(op.and_, [g13, g113])
g119 = h.gate(op.and_, [g14, g113])

g120 = h.gate(op.or_, [g107, g114]) #The three x coordinates
g121 = h.gate(op.or_, [g108, g115])
g122 = h.gate(op.or_, [g109, g116])
g123 = h.gate(op.or_, [g110, g117]) #The three y coordinates
g124 = h.gate(op.or_, [g111, g118])
g125 = h.gate(op.or_, [g112, g119])

#Check if they collide
g126 = h.gate(op.xnor_, [g94, g120])
g127 = h.gate(op.xnor_, [g95, g121])
g128 = h.gate(op.xnor_, [g96, g122])
g129 = h.gate(op.xnor_, [g104, g123])
g130 = h.gate(op.xnor_, [g105, g124])
g131 = h.gate(op.xnor_, [g106, g125])
g132 = h.gate(op.and_, [g126, g127])
g133 = h.gate(op.and_, [g128, g129])
g134 = h.gate(op.and_, [g130, g131])
g135 = h.gate(op.and_, [g132, g133])
g136 = h.gate(op.and_, [g134, g135])
g137 = h.gate(op.id_, [g136], is_output=True) #1 = winner, 0 = no winner

#Check illegal moves for second output
g138 = h.gate(op.or_, [g54, g62])
g139 = h.gate(op.or_, [g74, g86])
g140 = h.gate(op.or_, [g138, g139])
g141 = h.gate(op.not_, [g140])
g142 = h.gate(op.and_, [g141, g27]) #correct shape and does not go out of bounds
g143 = h.gate(op.id_, [g142], is_output=True) #0 = illegal move, 1 = legal move

#00 or 10 means illegal move, other person gets funds
#11 means winning move, winner gets funds
#01 means legal move, no winner, no funds move
