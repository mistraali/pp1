npa = {
  "A": "Alfa",
  "B": "Bravo",
  "C": "Charlie",
  "D": "Delta",
  "E": "Echo",
  "F": "Foxtrot",
  "G": "Golf",
  "H": "Hotel",
  "I": "India",
  "J": "Juliett",
  "K": "Kilo",
  "L": "Lima",
  "M": "Mike",
  "N": "November",
  "O": "Oscar",
  "P": "Papa",
  "Q": "Quebec",
  "R": "Romeo",
  "S": "Sierra",
  "T": "Tango",
  "U": "Uniform",
  "V": "Victor",
  "W": "Whiskey",
  "X": "X-ray",
  "Y": "Yankee",
  "Z": "Zulu",
  " ": "Space",
  ".": "Point",
  ",": "Point"
}

text = input("Enter text: ")
print("Spelled text: ", end="")
for i in text:
    print(npa[i.upper()], end=" ")