ip = "192.168.1.10"
attempts = 5

print(ip)
print(attempts)

if attempts >= 3:
    print("Possible brute force attack")
else:
    print("No worries, nothing is happening at the moment")

failed_ips = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.10"
]

print(len(failed_ips))

for ip in failed_ips:
    print("Failed login from", ip)
