import time

print("1. time()")
print(time.time())

print("\n2. ctime()")
print(time.ctime())

print("\n3. localtime()")
print(time.localtime())

print("\n4. gmtime()")
print(time.gmtime())

print("\n5. asctime()")
print(time.asctime())

print("\n6. sleep()")
print("Waiting for 2 seconds...")
time.sleep(2)
print("Done!")

print("\n7. strftime()")
print(time.strftime("%d-%m-%Y %H:%M:%S"))

print("\n8. strptime()")
print(time.strptime("05 Jun 2026", "%d %b %Y"))

print("\n9. mktime()")
print(time.mktime(time.localtime()))

print("\n10. perf_counter()")
start = time.perf_counter()
for i in range(100000):
    pass
end = time.perf_counter()
print("Execution Time:", end - start, "seconds")