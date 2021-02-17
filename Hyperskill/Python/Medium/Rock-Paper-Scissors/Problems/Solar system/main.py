# create the planets.txt

planets = ["Mercury\n", "Venus\n", "Earth\n", "Mars\n", "Jupiter\n", "Saturn\n", "Uranus\n", "Neptune"]

planets_file = open('planets.txt', 'w')

for planet in planets:
    planets_file.write(planet)

planets_file.close()
