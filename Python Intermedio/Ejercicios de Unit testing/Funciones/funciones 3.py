def calculate_total_payout(bonus_list):
    # LOCAL VARIABLE: 
    total_payout = 0 
    
    for amount in bonus_list:
        total_payout += amount
        
    return total_payout

# Usage:
team_bonuses = [4, 6, 2, 29]
final_report_sum = calculate_total_payout(team_bonuses)
print(f"Corporate Payout Total: ${final_report_sum}k")