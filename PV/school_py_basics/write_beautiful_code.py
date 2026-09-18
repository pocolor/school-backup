is_rainy = True
is_windy = True
is_cloudy = True

if not is_rainy and not is_windy and not is_cloudy:
    print("Krasne pocasi. Destnik neni potreba.")
elif is_cloudy or is_rainy and not is_windy:
    print("Vem si destnik.")
elif is_windy and not is_rainy:
    print("Vem si cepici.")
elif is_windy and not is_rainy and is_cloudy:
    print("Vem si reflexni obleceni.")