async def GeometriaCommand(ctx):
    wzory = """
    **Najważniejsze wzory geometryczne:**
    1. Pole i obwód prostokąta:
       - Pole: P = a * b
       - Obwód: O = 2a + 2b

    2. Pole i obwód kwadratu:
       - Pole: P = a²
       - Obwód: O = 4a

    3. Pole i obwód trójkąta:
       - Pole: P = ½ * a * h
       - Obwód: O = a + b + c

    4. Pole i obwód koła:
       - Pole: P = π * r²
       - Obwód: O = 2π * r

    5. Pole i obwód trapezu:
       - Pole: P = (a + b) * h / 2
       - Obwód: O = a + b + c + d

    6. Pole równoległoboku:
       - Pole: P = a * h

    7. Pole rombu:
       - Pole: P = e * f / 2
       - Obwód: O = 4a

    8. Pole elipsy:
       - Pole: P = π * a * b

    9. Twierdzenie Pitagorasa (dla trójkąta prostokątnego):
       - a² + b² = c²

    10. Objętość i pole powierzchni sześcianu:
        - Objętość: V = a³
        - Pole powierzchni: S = 6a²

    11. Objętość i pole powierzchni prostopadłościanu:
        - Objętość: V = a * b * c
        - Pole powierzchni: S = 2ab + 2ac + 2bc

    12. Objętość i pole powierzchni kuli:
        - Objętość: V = 4/3 * π * r³
        - Pole powierzchni: S = 4π * r²

    13. Objętość i pole powierzchni walca:
        - Objętość: V = π * r² * h
        - Pole powierzchni: S = 2π * r * (r + h)

    14. Objętość i pole powierzchni stożka:
        - Objętość: V = ⅓ * π * r² * h
        - Pole powierzchni: S = π * r * (r + l)
    """
    await ctx.send(wzory)