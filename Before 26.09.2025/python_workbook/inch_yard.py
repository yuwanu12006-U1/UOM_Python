distance = float(input("Enter a distance in inch: "))

conversions = [63360, 36, 12, 1]

converts = []
for conversion in conversions:
    con_count = 0
    while distance // conversion != 0:
        con_count += 1
        distance -= conversion
    converts.append(con_count)

print(f"{converts[0]} miles\n{converts[1]} yards\n{converts[2]} feets\n{converts[3]} inches")
