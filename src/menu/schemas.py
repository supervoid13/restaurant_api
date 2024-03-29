from pydantic import BaseModel


class MenuCreateUpdate(BaseModel):
    title: str
    description: str


class MenuRetrieve(BaseModel):
    id: str
    title: str
    description: str
    submenus_count: int
    dishes_count: int


class SubmenuCreateUpdate(BaseModel):
    title: str
    description: str


class SubmenuRetrieve(BaseModel):
    id: str
    title: str
    description: str
    dishes_count: int


class DishRetrieve(BaseModel):
    id: str
    title: str
    description: str
    price: str


class DishCreateUpdate(BaseModel):
    title: str
    description: str
    price: str
