"""****************Grid**********************"""
grid = {}
key = 33
index = []
for x in range(1, 4):
    c = x
    for y in range(1, 9):
        b = y
        for z in range(1, 5):
            a = z
            index = []
            for f in (c, b, a):
                index.append(str(f))
            grid[chr(key)] = index
            key += 1


"""*************Encryption********************"""
encryption = []
password = raw_input("enter your pass: ")
for p in range(0, len(password)):
    encryption.append("".join(grid[password[p]])) #encrypts the pass
print "Encrypted pass : " + "".join(encryption) #prints encrypted pass


"""*************Decryption********************"""
decryption = []
ecn_pass = raw_input("Enter Encrypted pass: ") #will be changed to a 
var taking ecrypted_pass as input
n = 0
dec = []
for g in range(0, (len(ecn_pass)/3)):
    dec = []
    for e in range(n, n+3):
        dec.append(ecn_pass[e])
    decryption.append(dec)
    n = n + 3
for h in range(0, len(decryption)):
    print grid.keys()[grid.values().index(decryption[h])], #prints decrypted pass
