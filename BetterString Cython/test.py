from BetterString import BetterString
import time

x = BetterString("#"*3000)

for i in range(1, 100):
    start = time.time()
    x.rainbow()
    time_took = time.time()-start
    print(time_took)
