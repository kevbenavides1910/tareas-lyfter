def audit_text_casing(business_text):
    # LOCAL VARIABLES: They reset to 0 every time the function is called
    upper_count = 0
    lower_count = 0
    
    for character in business_text:
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1

    return f"Analysis complete: {upper_count} uppercase and {lower_count} lowercase letters found."

# --- Corporate Interface ---

user_string = input("PLEASE ENTER THE TEXT FOR QUALITY AUDIT: ")

audit_report = audit_text_casing(user_string)

print("-" * 40)
print(f"INPUT DATA: '{user_string}'")
print(audit_report)
print("-" * 40)