# GLOBAL SCOPE: Company-wide policy
company_status = "Operational"

def log_system_update():
    print("-> System Log: Executing background synchronization...")

def initialize_department_server():
    # LOCAL SCOPE: Only exists inside this specific server boot
    server_token = "TEMP-9982"
    print(f"Server initialized with local token: {server_token}")
    log_system_update() # Calling the second function

# EXPERIMENT: Modifying the Global Policy
def emergency_shutdown():
    global company_status
    company_status = "Maintenance Mode"
    print(f"!!! ATTENTION: Status changed to {company_status} !!!")

# Execution Flow
initialize_department_server()
emergency_shutdown()
print(f"Final Corporate Status: {company_status}")