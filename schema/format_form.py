#Schema formulari, s´ha eliminat el camp password per alta sensibilitat
def list_format_game_schema(list_response):
    keys = ["Name", "Surname", "email", "address", "CP","description","age"]
    return [{key: value} for key, value in zip(keys, list_response)]