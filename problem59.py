# XOR decryption
# Problem 59

def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 

f = open("p059_cipher.txt", 'r')
for line in f:
    letters = []
    letter = ''
    for char in line:
        if char != ',':
            letter += char
        elif char == ',':
            letters.append(letter)
            letter = ''
f.close()

space = most_frequent(letters)
key1 = int(space) - 32
key2 = 32 - int(space)
print(f"key1: {key1}")
print(f"key2: {key2}")

nf = open("message.txt","w+")
def unencrypt(key):
    line = ''
    for item in letters:
        trueascii = int(item) + key
        letter = chr(trueascii)
        line = line + letter
    return line

line1 = unencrypt(key1)
line2 = unencrypt(key1)
nf.write(line1 + "\n" + line2)

nf.close()