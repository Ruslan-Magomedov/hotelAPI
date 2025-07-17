def check(data: list[dict], query_id: int) -> tuple[int, bool]:
    """
    Функция принимает список словарей и id, с помошью цикла смотрит вхождение по id
    и возврощает кортеж из индекса словоря и bool
    """
    for i, d in enumerate(data):
        if data[i]["id"] == query_id:
            return i, True,
    return 0, False
