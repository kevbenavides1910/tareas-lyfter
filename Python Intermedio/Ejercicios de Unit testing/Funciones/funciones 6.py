def organize_inventory_report(raw_inventory_data):
   
    # LOCAL STEP 1: Convert the input string into a Python List
    items_list = raw_inventory_data.split("-")

    items_list.sort()
    
    sorted_report = "-".join(items_list)
    
    return sorted_report

# --- Warehouse Interface ---

print("=== PYCORP INVENTORY SYSTEM ===")
user_inventory = input("Enter items received (separate by hyphens '-'): ")

final_report = organize_inventory_report(user_inventory)

# Display the professional report
print("\n--- OFFICIAL INVENTORY REPORT ---")
print(f"STATUS: Organized and Validated")
print(f"ITEMS: {final_report}")
print("---------------------------------")