import random
a = ["monday", "Tuesday", "Wednesday", "Thursday"]
b = ["Januray", "February", "March", "April"]
c = ["winter", "summer", "spring", "autumn"]
lst = [a, b, c]
def rndm():
    rslt = ""
    for i in range(0,3):
        rndm_in = random.randint(0,3)
        rslt = rslt + lst[i][rndm_in] + " "
    return rslt
print(rndm())