class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year_of_creation):
        self.painter = painter
        self.title = title
        self.year_of_creation = year_of_creation


painting = Painting(input(), input(), input())
print(f'"{painting.title}" by {painting.painter} ({painting.year_of_creation}) hangs in the {painting.museum}.')
