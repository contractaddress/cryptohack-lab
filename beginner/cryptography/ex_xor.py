stringlist = list(b'label')

xorresults = [c ^ 13 for c in stringlist]

results = ''.join(chr(char) for char in xorresults)

print(results)
