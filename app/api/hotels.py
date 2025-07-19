from fastapi import APIRouter, Body
from sqlalchemy import insert

import app.dependencies.check_id as check_id
from app.dependencies.pages import PagenationDep
from app.openapi_examples import EX_DATA
from app.schema.hotels import Hotel, HotelPatch

from app.db import async_session_maker
from app.models.hotels import HotelsOrm


router = APIRouter(prefix="/hotels", tags=["Отели"])


# @router.get("")
# def get_all_hotels(page: PagenationDep):
#     """Ручка для получения всех отелей c пагинацией"""
#     return data[page.quantity * (page.page-1):][:page.quantity]


@router.post("")
async def create_hotel(hotel: Hotel = Body(openapi_examples=EX_DATA)):
    """Ручка для создания отеля"""
    async with async_session_maker() as session:
        SQL_QUERY = insert(HotelsOrm).values(**hotel.model_dump())
        await session.execute(SQL_QUERY)
        await session.commit()
    return {"message": "hotel created"}


# @router.delete("/{hotel_id}")
# def delete_hotel_by_id(hotel_id: int):
#     """Ручка для удаления отеля по id"""
#     index, check_bool = check_id.check(data, hotel_id)
#     if check_bool:
#         data.pop(index)
#         return data
#     return {"message": f"Not Found by id {hotel_id}"}


# @router.put("/{hotel_id}")
# def change_hotel_by_id(hotel_id: int, hotel: Hotel = Body(openapi_examples=EX_DATA)):
#     """Ручка для изменения отеля по id"""
#     index, check_bool = check_id.check(data, hotel_id)
#     if check_bool:
#         data[index]["title"] = hotel.title
#         data[index]["name"] = hotel.name
#         return {"message": "OK"}
#     return {"message": f"Not Found by id {hotel_id}"}


# @router.patch("/{hotel_id}")
# def change_hotel_by_id_patch(hotel_id: int, hotel: HotelPatch = Body(openapi_examples=EX_DATA)):
#     """Ручка для изменения отеля по id (частично)"""
#     index, check_bool = check_id.check(data, hotel_id)
#     if check_bool:
#         if hotel.title != None:
#             data[index]["title"] = hotel.title
#         if hotel.name != None:
#             data[index]["name"] = hotel.name
#         return {"message": "OK"}
#     return {"message": f"Not Found by id {hotel_id}"}
