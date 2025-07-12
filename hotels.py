from fastapi import FastAPI, APIRouter, Body

from typing import Annotated

import check_id
from dependencies.pages import PagenationDep
from openapi_examples import EX_DATA
from schema.hotels import Hotel, HotelPatch


router = APIRouter(prefix="/hotels", tags=["Отели"])
data = [
    {"id": 1, "title": "Rim", "name": "Sora"},
    {"id": 2, "title": "NY", "name": "Star"},
    {"id": 3, "title": "Chana", "name": "laka"},
    {"id": 4, "title": "Sochi", "name": "Miramar"},
    {"id": 5, "title": "Moscow", "name": "Octopus"},
    {"id": 6, "title": "Moscow", "name": "Laina"},
    {"id": 7, "title": "Rim", "name": "Sora"},
    {"id": 8, "title": "NY", "name": "Star"},
    {"id": 9, "title": "Chana", "name": "laka"},
    {"id": 10, "title": "Sochi", "name": "Miramar"},
    {"id": 11, "title": "Moscow", "name": "Octopus"},
    {"id": 12, "title": "Moscow", "name": "Laina"},
]


@router.get("")
def get_all_hotels(page: PagenationDep):
    """
    Ручка для получения всех отелей
    """
    return data[page.quantity * (page.page-1):][:page.quantity]


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
def create_hotel(hotel: Hotel = Body(openapi_examples=EX_DATA)):
    """
    Ручка для создания отеля
    """
    if type(hotel.title) == str and type(hotel.name) == str:
        new_id = data[-1]["id"] + 1
        data.append({"id": new_id, "title": hotel.title, "name": hotel.name})
        return {"message": "OK"}
    return {"message": "Bad Data"}


@router.put("/{hotel_id}")
def change_hotel_by_id(hotel_id: int, hotel: Hotel = Body(openapi_examples=EX_DATA)):
    """
    Ручка для изменения отеля по id
    """
    index, check_bool = check_id.check(data, hotel_id)
    if check_bool:
        data[index]["title"] = hotel.title
        data[index]["name"] = hotel.name
        return {"message": "OK"}
    return {"message": f"Not Found by id {hotel_id}"}


@router.patch("/{hotel_id}")
def change_hotel_by_id_patch(hotel_id: int, hotel: HotelPatch = Body(openapi_examples=EX_DATA)):
    """
    Ручка для изменения отеля по id (частично)
    """
    index, check_bool = check_id.check(data, hotel_id)
    if check_bool:
        if hotel.title != None:
            data[index]["title"] = hotel.title
        if hotel.name != None:
            data[index]["name"] = hotel.name
        return {"message": "OK"}
    return {"message": f"Not Found by id {hotel_id}"}
