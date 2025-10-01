from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.inspect import inspect

DATABASE_URL = "csce-315-db.engr.tamu.edu" 

engine = create_engine(DATABASE_URL)
metadata = MetaData()

metadata.reflect(bind=engine)

table_names = list(metadata.tables.keys())

mapper = inspect("ingredients")
ingredients_keys = [col.name for col in mapper.ingredient_id]

mapper = inspect("menu")
ingredients_keys = [col.name for col in mapper.item_id]

session.close()