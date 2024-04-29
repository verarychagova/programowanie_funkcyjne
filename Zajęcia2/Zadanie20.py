def analyze_data(data):
    match data:
        case []:
            return "Pusta lista"
        case [_]:
            return "Lista z jednym elementem"
        case [_, _]:
            return "Lista z dwoma elementami"
        case [_, *rest]:
            return f"Lista z wieloma elementami, gdzie pierwszy to {data[0]} i reszta to {rest}"
        case ():
            return "Pusta krotka"
        case (_,):
            return "Krotka z jednym elementem"
        case (_, _):
            return "Krotka z dwoma elementami"
        case (_, *rest):
            return f"Krotka z wieloma elementami, gdzie pierwszy to {data[0]} i reszta to {rest}"
        case _:
            return "Nieznany typ danych"


print(analyze_data([]))
print(analyze_data([1]))
print(analyze_data([1, 2]))
print(analyze_data([1, 2, 3, 4, 5]))
print(analyze_data(()))
print(analyze_data((1,)))
print(analyze_data((1, 2)))
print(analyze_data((1, 2, 3, 4, 5)))