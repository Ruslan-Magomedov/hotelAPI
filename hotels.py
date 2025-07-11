from fastapi import FastAPI, APIRouter, Query, Body

import check_id


router = APIRouter(prefix="/hotels", tags=["Отели"])
data = [
    {"id": 1, "title": "Rim", "name": "Sora"},
    {"id": 2, "title": "NY", "name": "Star"},
    {"id": 3, "title": "Chana", "name": "laka"},
    {"id": 4, "title": "Sochi", "name": "Miramar"},
    {"id": 5, "title": "Moscow", "name": "Octopus"},
    {"id": 6, "title": "Moscow", "name": "Laina"},
]


@router.get("")
def get_all_hotels():
    """
    Ручка для получения всех отелей
    """
    return data


@router.delete("/{hotel_id}")
def delete_hotel_by_id(hotel_id: int):
    """
    Ручка для удаления отеля по id
    """
    index, check_bool = check_id.check(data, hotel_id)
    if check_bool:
        data.pop(index)
        return data
    return {"message": f"Not Found by id {hotel_id}"}


@router.post("")
def create_hotel(title: str, name: str):
    """
    Ручка для создания отеля
    """
    if type(title) == str and type(name) == str:
        new_id = data[-1]["id"] + 1
        data.append({"id": new_id, "title": title, "name": name})
        return {"message": "OK"}
    return {"message": "Bad Data"}


@router.put("/{hotel_id}")
def change_hotel_by_id(hotel_id: int, title: str = Body(), name: str = Body()):
    """
    Ручка для изменения отеля по id
    """
    index, check_bool = check_id.check(data, hotel_id)
    if check_bool:
        data[index]["title"] = title
        data[index]["name"] = name
        return {"message": "OK"}
    return {"message": f"Not Found by id {hotel_id}"}


@router.patch("/{hotel_id}")
def change_hotel_by_id_patch(hotel_id: int, title: str | None = Body(None), name: str | None = Body(None)):
    """
    Ручка для изменения отеля по id (частично)
    """
    index, check_bool = check_id.check(data, hotel_id)
    if check_bool:
        if title != None:
            data[index]["title"] = title
        if name != None:
            data[index]["name"] = name
        return {"message": "OK"}
    return {"message": f"Not Found by id {hotel_id}"}
