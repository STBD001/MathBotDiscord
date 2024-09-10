async def KombinatorykaCommand(ctx):
    wzory = """
    **Najważniejsze wzory kombinatoryczne:**

    1. Liczba permutacji elementów:
       - P(n) = n!

    2. Liczba kombinacji:
       - C(n, k) = n! / (k!(n - k)!)
    """
    await ctx.send(wzory)
