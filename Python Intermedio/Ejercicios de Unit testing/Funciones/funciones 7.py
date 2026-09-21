def check_prime_security(number):
    if number < 2:
        return False
    # Efficiency: check until the square root
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def extract_valid_tokens(user_input_string):
    raw_list = user_input_string.split(",")
    
    valid_tokens = []
    
    for item in raw_list:
        token_value = int(item.strip()) # Convert to integer locally
        if check_prime_security(token_value):
            valid_tokens.append(token_value)
            
    return valid_tokens

print("=== PYCORP SECURITY SYSTEM ===")
user_data = input("Enter serial numbers to verify (separate by commas ','): ")

# Processing the tokens locally
secure_list = extract_valid_tokens(user_data)

print("\n--- SECURITY AUDIT REPORT ---")
if not secure_list: # Si la lista está vacía
    print("STATUS: NO VALID SECURITY TOKENS FOUND IN THIS BATCH.")
else:
    print(f"The following numbers are Valid Security Tokens (Primes): {secure_list}")