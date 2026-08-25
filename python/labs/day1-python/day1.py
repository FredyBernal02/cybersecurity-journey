ip = "192.168.1.10"
attempts = 5

print(ip)
print(attempts)

if attempts >= 3:
    print("Possible brute force attack")
else:
    print("No worries, nothing is happening at the moment")
