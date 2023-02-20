import math

coxa    = 26      # coxa length
femur   = 42      # femur length
tibia   = 88      # tibia length
bodyHeight = 36  # body height

def getAnglesByIK(x,y,z):
    coxaAngle = math.degrees(math.atan2(y, x))

    y = abs(y)

    L = math.sqrt(z**2 + (y-coxa)**2)
    alphaOne = math.acos(z / L)
    alphaTwo = math.acos((tibia**2 - femur**2 - L**2) / (-2 * femur * L))
    alpha = alphaOne + alphaTwo

    femurAngle = math.degrees(alpha)

    beta = math.acos((L**2 - tibia**2 - femur**2) / (-2 * tibia * femur))

    tibiaAngle = math.degrees(beta)

    return coxaAngle, femurAngle, tibiaAngle

angles = getAnglesByIK(50,100, 30 + bodyHeight)
print(f'coxa = {angles[0]}, femur = {angles[1]}, tibia = {angles[2]}')
