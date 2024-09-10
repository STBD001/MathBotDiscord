async def CiagiCommnad(ctx):
    wzory = """
    **Wzory na ciągi:**

    1. Ciąg arytmetyczny:
       - Wzór na n-ty wyraz: aₙ = a₁ + (n - 1)r
       - Suma n początkowych wyrazów: Sₙ = n / 2 * (a₁ + aₙ)

    2. Ciąg geometryczny:
       - Wzór na n-ty wyraz: aₙ = a₁ * qⁿ⁻¹
       - Suma n początkowych wyrazów: Sₙ = a₁ * (1 - qⁿ) / (1 - q)  dla q ≠ 1
    """
    await ctx.send(wzory)
