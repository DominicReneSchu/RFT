# Parameter
start_investition = 3_000_000_000  # 3 Milliarden €
wachstumsrate = 0.10               # 10 % p.a.
jahre = 100                        # Betrachtungszeitraum (z.B. 4 Generationen)

# Berechnung
output = start_investition * (1 + wachstumsrate) ** jahre

# Ausgabe
print(f"Nach {jahre} Jahren ergibt eine Investition von 3 Mrd €:")
print(f"=> {output:,.0f} € (≈ {output/1_000_000_000:.0f} Milliarden €)")
