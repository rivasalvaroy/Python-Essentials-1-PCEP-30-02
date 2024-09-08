rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True

rooms[0][4][1] = False

vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print("{}".format(vacancy))
