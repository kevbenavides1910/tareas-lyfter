def encrypt_corporate_data(raw_text):
 
    encrypted_string = raw_text[::-1]
    return encrypted_string

user_input = input("ENTER THE DATA TO ENCRYPT: ")

secure_code = encrypt_corporate_data(user_input)

print("-" * 30)
print(f"ORIGINAL DATA: {user_input}")
print(f"SECURE ENCRYPTED DATA: {secure_code}")
print("-" * 30)