def memoized_func(n, memo={}): 
 if n == 0 or n == 1: 
    return n 
 if n in memo:
  return memo[n]
 else: 
    memo[n] = memoized_func(n-1, memo) + memoized_func(n-2, memo) 

 return memo[n]
