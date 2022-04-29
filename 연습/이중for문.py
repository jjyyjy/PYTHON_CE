i = 1
for i in range(1, 10):
    a = 1
    for a in range(1, 10):
        print("%s x %s = %s" % (i, a, i*a))
        a += 1
    i += 1
    if a + 1:
        print("\n")