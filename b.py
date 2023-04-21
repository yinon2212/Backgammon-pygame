from timeit import default_timer as timer

start = timer()
while timer() - start < 2:
    continue
end = timer()
print(end - start) # Time in seconds, e.g. 5.38091952400282