# BASICS

for x in range(0, 151):
    print(x)


# =======================================
# MULTIPLES OF FIVE

for s in range(5, 1001, 5):
    print(s)


# =======================================
# COUNTING, THE DOJO WAY

for t in range(0, 101):
    if(t % 10 == 0):
        print("Coding Dojo")
    elif(t % 5 == 0):
        print("Coding")
    else:
        print(t)


# ======================================
# WHOA, THAT SUCKER'S HUGE

sum = 0

for i in range(0, 500000):
    if(i % 2 != 0):
        sum = sum + i
print(sum)


# ======================================
# COUNTDOWN BY FOURS

for y in range(2018, 0, -4):
    print(y)


# =====================================
# FLEXIBLE COUNTER

lowNum = 2
highNum = 9
mult = 3

for p in range(lowNum, highNum + 1):
    if (p % mult == 0):
        print(p)
