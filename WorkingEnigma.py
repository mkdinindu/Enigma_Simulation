import random

# below variables stores the starting positions or 'codes' for enigma machine rotors.
# in the war there was a document which specifies an amount of key combinations for each day in month.
# every base has this document.
# by using the same key combinations that used to encrypt data recievers can decrypt the data.
r1_start_position = 0
r2_start_position = 0
r3_start_position = 0


# this array is used to specify the alphabetical letters.
# in enigma machines only english alphebetical letters were used as input. this was most due to the fact that MORSE code was already standardized for the english language.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#below array is used to generate random value arrays for rottors and does not serve to any process of the code
#nums = [0,1,2,3,4,5,6,7,8,9,10,11,12, 13,14,15,16,17,18,19,20, 21,22,23,24,25]
#random.shuffle(nums)
#print("Shuffled")
#print(nums)

# below arrays are used to define rotors with random wirings.
# in the time of ww2 a set of 5 rotors were used by soldiers and picked 3 of them for use.
rotor1 = [12, 9, 18, 20, 25, 8, 22, 7, 23, 1, 3, 16, 17, 2, 15, 10, 13, 21, 24, 11, 14, 5, 4, 0, 6, 19]

rotor2 = [0,1,2,3,4,5,6,7,8,9,10,11,12, 13,14,15,16,17,18,19,20, 21,22,23,24,25]

rotor3 = [24, 22, 21, 12, 11, 6, 20, 3, 14, 5, 18, 19, 17, 16, 15, 1, 25, 23, 13, 9, 0, 10, 2, 4, 8, 7]

# in the real enigma machine the reflector serves as a mirror. ones a letter passed forward through the set of rottors
# the reflector will pass the letter back to rottors in opposite side, and the letter will travel back to the input wheel through the rotors.
# the rotor was wired in a coupled letter nature. (A-Z, B-Y)
reflector = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] # Example: 0->25, 1->24, etc.

# below code is used to generate the inverse versions of rotors. this inversed versions are used in backwad pass stage.
def create_inverse_rotor(rotor):
    inversed_rotor = [0] * 26
    for i, val in enumerate(rotor):
        inversed_rotor[val] = i
    return inversed_rotor


rotor1_inversed = create_inverse_rotor(rotor1)
rotor2_inversed = create_inverse_rotor(rotor2)
rotor3_inversed = create_inverse_rotor(rotor3)

# the enigma machine has 3 rotors. in basic settings these  rotors work in the same principle as clock hands.
# when the rightmost rotor completes a full round (26 steps) the middle rotor will step one. and same as rotor one, when the second rotor completed a round the 3rd rotor will take a step.
# letters from the keyboard comes through wires and reach the input wheel, which is numbered and mapped (a-z | 1 -26)
# when a key pressed the rotor will take a step before the electricity pass through the input wheel.
# this creates an offset. imagine that if the rotor positions were 0-0-0 and the letter 'a' was pressed
# and the rightmost rotor steps a one. now the input wheels number 1 pin is conected with the rotor ones number 2.
# this is the offset we have to handle to.
def apply_offset(position, offset):
    return (position + offset) % 26

def remove_offset(position, offset):
    return (position - offset + 26) % 26

r1_start_position = input("start position of rotor 1: ")
r2_start_position = input("start position of rotor 2: ")
r3_start_position = input("start position of rotor 3: ")

# after letter was entered, the electric signal will travel through each rotor.
# in each rotor the letter will changed in to a random letter.
# the pattern which letters will change is controlled by the starting position of each rotor.

def scramble(char, rp1, rp2, rp3):
    lposition = alphabet.index(char)

    inposition = apply_offset(lposition, rp1)
    inposition = rotor1[inposition]
    inposition = remove_offset(inposition, rp1)

    inposition = apply_offset(inposition, rp2)
    inposition = rotor2[inposition]
    inposition = remove_offset(inposition, rp2)

    inposition = apply_offset(inposition, rp3)
    inposition = rotor3[inposition]
    inposition = remove_offset(inposition, rp3)

    reflected_position = reflector[inposition]

    #--Backward pass--

    inposition = apply_offset(reflected_position, rp3)
    inposition = rotor3_inversed[inposition]
    inposition = remove_offset(inposition, rp3)

    inposition = apply_offset(inposition, rp2)
    inposition = rotor2_inversed[inposition]
    inposition = remove_offset(inposition, rp2)

    inposition = apply_offset(inposition, rp1)
    inposition = rotor1_inversed[inposition]
    inposition = remove_offset(inposition, rp1)


    print("final ciphered", inposition, alphabet[inposition])


char = input()
rp1 = int(r1_start_position)
rp2 = int(r2_start_position)
rp3 = int(r3_start_position)

#below is the main loop that keeps the code running unitil the letter "*" is typed.
# and it maintains the rotor stepping mechanism
while char != '*':

    rp1 += 1
    if rp1 > 25:
        rp1 = 0
        rp2 += 1
    if rp2 > 25:
        rp2 = 0
        rp3 += 1
    print("rp1", rp1)
    scramble(char, rp1, rp2, rp3)
    char = input()

    print()

