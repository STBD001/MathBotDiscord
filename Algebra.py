async def AlgebraCommand(ctx):
    wzory = """
        **Najważniejsze wzory algebry:**

        1. Wzory skróconego mnożenia:
           - (a + b)² = a² + 2ab + b²
           - (a - b)² = a² - 2ab + b²
           - (a + b)(a - b) = a² - b²

        2. Rozkład na czynniki:
           - a² - b² = (a - b)(a + b)
           - a³ - b³ = (a - b)(a² + ab + b²)
           - a³ + b³ = (a + b)(a² - ab + b²)

        3. Równania kwadratowe:
           - ax² + bx + c = 0
           - x₁, x₂ = (-b ± √(b² - 4ac)) / 2a
           - Delta (Δ) = b² - 4ac

        4. Wzory funkcji kwadratowej:
           - Postać kanoniczna: f(x) = a(x - p)² + q, gdzie p = -b/2a, q = f(p)
        """
    await ctx.send(wzory)