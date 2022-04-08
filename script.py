s = list(input().split(" "))
minute = []
hour = []
day_of_month = []
month = []
day_of_week = []
command = s[-1]
l = [minute, hour, day_of_month, month, day_of_week]
l1 = [60, 12, 31, 12, 7 ]
for i in range(0, len(l)):
    temp = s[i]
    if('*'== s[i]):
        for j in range(1, l1[i]+1):
            l[i].append(j)
    elif('-' in s[i]):
        a, b = s[i].split("-")
        a = int(a)
        b = int(b)
        for j in range(a, b+1):
            l[i].append(j)
    elif('/' in s[i]):
        a, b = s[i].split("/")
        b = int(b)
        if(a=='*'):
            for j in range(0, l1[i], b):
                l[i].append(j)
        temp = list(s[i].split("/"))
    elif(',' in s[i]):
        temp = list(s[i].split(","))
        for j in range(0, len(temp)):
            l[i].append(int(temp[j]))
    else:
        l[i].append(int(s[i]))
res = ["minute", "hour", "day_of_month", "month", "day_of_week"]
for i in range(0, len(res)):
    temp = len(res[i])
    t = " "*(14-temp)
    print(res[i]+t, end="")
    r = l[i]
    for i in range(0, len(r)):
        print(r[i], end=" ")
    print()
print("command       "+command)
