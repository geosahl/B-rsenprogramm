def bewertung_berechnen(kgv, dividende):
    score = 100 - (kgv * 2) + (dividende * 5)
    return max(0, min(score, 100))  # Score zwischen 0 und 100 begrenzen