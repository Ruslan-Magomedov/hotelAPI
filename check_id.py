def check(data: list[dict], query_id: int) -> tuple[int, bool]:
    for i, d in enumerate(data):
        if data[i]["id"] == query_id:
            return i, True,
    return 0, False
