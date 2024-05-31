# Fingerprint Locking System
fingerprints = {
    "fingerprint1": "Alice",
    "fingerprint2": "Bob",
    "fingerprint3": "Charlie"
}

input_fingerprint = input("Scan your fingerprint: ")

if input_fingerprint in fingerprints:
    print(f"Welcome, {fingerprints[input_fingerprint]}! Access granted.")
else:
    print("Access denied. Unknown fingerprint.")
