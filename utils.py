def radio(ind):
    text_radios = ["Я буду не один/одна", "Я буду один/одна", "Я не смогу прийти"]
    return text_radios[ind]


def get_index(items):
    for key, value in items:
        if "radio" in key:
            return int(key.split("_")[1])
