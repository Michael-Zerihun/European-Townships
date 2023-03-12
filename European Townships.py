inputFile = open('./inputs/ET_small.txt', 'r')
lines = inputFile.readlines()

lineList = []

for line in lines:
    toList = line.strip().split(',')
    toNum = [int (i) for i in toList]
    lineList.append(toNum)

inputFile.close()

# this will be our end point
lineList.append([])

wall = [3,4,6]

case = []
accentTime,regularTime, accentPaint,regularPaint = 0,0,0,0

fff = [[2],[1],[4, 1, 4, 1],[2],[5, 2, 4, 1],[4, 1, 4, 1], []]
for rooms in lineList[2:]:
    if len(rooms) > 1:
        for index in range(len(wall)):
            accentTime += wall[index]*rooms[index + 1]/3 * 2.5
            regularTime += wall[index]*2*rooms[index + 1]/3 * 3.25

            accentPaint += wall[index]*rooms[index + 1]/3 * 1.5
            regularPaint += wall[index]*2*rooms[index + 1]/3 * 2.25
    else:
        case.append(["{0:.2f}, {1:.2f}, {2:.2f}".format((accentTime+regularTime),accentPaint,regularPaint)])
        bucket = []
        accentTime,regularTime, accentPaint,regularPaint = 0,0,0,0

ET_output = open("./ET_output.txt", 'w')
for i in range(len(case)):
    ET_output.writelines(f"Case #{i+1}: " +case[i][0] +'\n' )
ET_output.close()