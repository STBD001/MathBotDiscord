async def TrygonometriaCommand(ctx):
    wzory = """
    **Najważniejsze wzory trygonometryczne:**

    1. Podstawowe tożsamości trygonometryczne:
       - sin²(θ) + cos²(θ) = 1
       - 1 + tan²(θ) = sec²(θ)
       - 1 + cot²(θ) = csc²(θ)

    2. Wzory redukcyjne:
       - sin(180° - θ) = sin(θ)
       - cos(180° - θ) = -cos(θ)
       - sin(90° - θ) = cos(θ)
       - cos(90° - θ) = sin(θ)

    3. Wzory na sinus, cosinus, tangens sumy i różnicy kątów:
       - sin(α + β) = sin(α)cos(β) + cos(α)sin(β)
       - sin(α - β) = sin(α)cos(β) - cos(α)sin(β)
       - cos(α + β) = cos(α)cos(β) - sin(α)sin(β)
       - cos(α - β) = cos(α)cos(β) + sin(α)sin(β)
       - tan(α + β) = (tan(α) + tan(β)) / (1 - tan(α)tan(β))
    """
    await ctx.send(wzory)
