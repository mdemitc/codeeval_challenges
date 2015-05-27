import sys

with open(sys.argv[1]) as f:
    for line in f:
        doors = int(line.split(' ')[0])
        n_timer = int(line.split(' ')[1])
        list_doors = list('T'*doors)

        for i in range(n_timer-1):
            for i in range(len(list_doors)):
                if (i+1)%2 == 0:
                    list_doors[i] = "F"

                if (i+1)%3 == 0:
                    if list_doors[i] == 'T':
                        list_doors[i] = "F"
                    else:
                        list_doors[i] = "T"

        if list_doors[-1] == 'T':
            list_doors[-1] = "F"
        else:
            list_doors[-1] = "T"

        print list_doors.count('T')
