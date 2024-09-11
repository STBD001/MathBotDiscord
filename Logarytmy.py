async def LogarytmyCommand(ctx):
    wzory = """
    **Najważniejsze wzory logarytmiczne:**

    1. Definicja logarytmu:
       - logₐ(b) = x  ⇔  aˣ = b

    2. Własności logarytmów:
       - logₐ(x * y) = logₐ(x) + logₐ(y)
       - logₐ(x / y) = logₐ(x) - logₐ(y)
       - logₐ(xⁿ) = n * logₐ(x)
       - logₐ(1) = 0
       - logₐ(a) = 1
    """
    await ctx.send(wzory)
