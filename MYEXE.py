# reverse_challenge.py

import base64
import hashlib

# Replace this with your video URL before building the EXE
VIDEO_URL = "https://youtu.be/OkNo_N85em0?si=2gCfzPd0M2UhLuSZ"

# The link is encoded so it isn't immediately visible in the source
ENCODED_URL = base64.b64encode(VIDEO_URL.encode()).decode()

# Challenge password hash
PASSWORD_HASH = hashlib.sha256(
    b"vsugfsFgiucg@@subCce378qyr9fusbdAuchs,*"
).hexdigest()


def verify_password(password):
    return hashlib.sha256(password.encode()).hexdigest() == PASSWORD_HASH


def get_video_url():
    return base64.b64decode(ENCODED_URL).decode()


def premium_algorithm(x):
    value = x
    for _ in range(1000):
        value = ((value * 31337) ^ 0xDEADBEEF) & 0xFFFFFFFF
    return value


def main():
    print("=== Reverse Engineering Challenge ===")
    print("Find the hidden video link.")

    password = input("Password: ")

    if verify_password(password):
        print("Access granted.")
        print("Algorithm result:", premium_algorithm(12345))
        print("Video:", get_video_url())
    else:
        print("Access denied.")


if __name__ == "__main__":
    main()