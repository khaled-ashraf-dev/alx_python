for i in range(0, 100):
    if '{:02d}'.format(i)[0] < '{:02d}'.format(i)[1]:
        if i != 89:
            print('{:02d}'.format(i), end=", ")
        else:
            print('{:02d}'.format(i))