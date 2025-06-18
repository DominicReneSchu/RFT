# Parameters
start_investment = 3_000_000_000   # 3 billion €
growth_rate = 0.10                 # 10% p.a.
years = 100                        # Time horizon (e.g., 4 generations)

# Calculation
output = start_investment * (1 + growth_rate) ** years

# Output
print(f"After {years} years, an investment of 3 billion € yields:")
print(f"=> {output:,.0f} € (≈ {output/1_000_000_000:.0f} billion €)")
#