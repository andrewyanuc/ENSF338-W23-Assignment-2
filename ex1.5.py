import time
import matplotlib.pyplot as plt

def memoized_func(n, memo={}): 
 if n == 0 or n == 1: 
    return n 
 if n in memo:
  return memo[n]
 else: 
    memo[n] = memoized_func(n-1, memo) + memoized_func(n-2, memo) 

 return memo[n]

def func(n): 
    if n == 0 or n == 1: 
        return n 
    else: 
        return func(n-1) + func(n-2)

n_values = range(36)
times_memo = []
times = []

for n in n_values:
    start_time = time.time()
    result = memoized_func(n)
    end_time = time.time()
    times_memo.append(end_time - start_time)
    
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(n_values, times_memo, label='Memoized')
plt.plot(n_values, times, label='Non-memoized')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Execution Time for func and memo_func')
plt.legend()
plt.ylim(0, max(max(times_memo), max(times)) * 1.1)
plt.show()
