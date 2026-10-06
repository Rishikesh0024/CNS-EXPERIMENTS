import hmac
import hashlib

secret_key = b"mysecretkey"

original_message = input("Enter the Original Message: ")

original_hmac = hmac.new(
    secret_key,
    original_message.encode(),
    hashlib.sha256
).hexdigest()

print("\nGenerated HMAC:")
print(original_hmac)

received_message = input("\nEnter the Received Message: ")

received_hmac = hmac.new(
    secret_key,
    received_message.encode(),
    hashlib.sha256
).hexdigest()

print("\nReceived HMAC:")
print(received_hmac)

print("\n" + "=" * 45)
print("VERIFICATION RESULT")
print("=" * 45)

if hmac.compare_digest(original_hmac, received_hmac):
    print("Message Integrity Verified.")
    print("No Tampering Detected.")
else:
    print("Message Tampering Detected.")
    print("Integrity Verification Failed.")