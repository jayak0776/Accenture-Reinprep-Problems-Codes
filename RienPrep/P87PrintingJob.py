def printingJob(n, t):
    arrival = (n * t) - t
    completion = (n - 1) * 10
    waitTime = 0
    if completion > arrival:
        waitTime = completion - arrival
    return waitTime
n, t = map(int, input().split())
print(printingJob(n, t))
