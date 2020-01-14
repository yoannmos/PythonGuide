from datetime import datetime
import re

from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Integer,
    Numeric,
    String,
    DateTime,
    Boolean,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import functions
from sqlalchemy.sql import selectable

Base = declarative_base()


class Cookie(Base):

    __tablename__ = "cookies"

    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

    def __repr__(self) -> str:
        msg = (
            "Cookie : \n"
            + f"   cookie_name = '{self.cookie_name}'\n"
            + f"   cookie_recipe_url = '{self.cookie_recipe_url}'\n"
            + f"   cookie_sku = '{self.cookie_sku}'\n"
            + f"   quantity = '{self.quantity}'\n"
            + f"   unit_cost = '{self.unit_cost}'"
        )
        return msg


class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer(), primary_key=True)
    user_mame = Column(String(15), nullable=False, unique=True)
    email_adress = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())

    def __repr__(self) -> str:
        msg = (
            "User : \n"
            + f"   user_mame = '{self.user_mame}'\n"
            + f"   email_adress = '{self.email_adress}'\n"
            + f"   phone = '{self.phone}'\n"
            + f"   password = '{self.password}'\n"
        )
        return msg


class Order(Base):

    __tablename__ = "orders"

    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.user_id"))
    shipped = Column(Boolean(), default=False)

    user = relationship("User", backref=backref("orders", order_by=order_id))

    def __repr__(self) -> str:
        msg = (
            "Order : \n"
            + f"   user_id = '{self.user_id}'\n"
            + f"   shipped = '{self.shipped}'\n"
        )
        return msg


class LineItem(Base):

    __tablename__ = "line_items"

    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey("orders.order_id"))
    cookie_id = Column(Integer(), ForeignKey("cookies.cookie_id"))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))

    order = relationship("Order", backref=backref("line_items", order_by=line_item_id))
    cookie = relationship("Cookie", uselist=False)

    def __repr__(self) -> str:
        msg = (
            "LineItem : \n"
            + f"   order_id = '{self.order_id}'\n"
            + f"   cookie_id = '{self.cookie_id}'\n"
            + f"   quantity = '{self.quantity}'\n"
            + f"   extended_cost = '{self.extended_cost}'\n"
        )
        return msg


if __name__ == "__main__":

    from sqlalchemy import create_engine, desc, func, cast
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # --------------------------------------------------------------------------------
    print("Exemple 7.1")
    print(11 * "-")

    cc_cookie = Cookie(
        cookie_name="chocolate chip",
        cookie_recipe_url="awesome.cookies.miam/cookie/cc/recipe.html",
        cookie_sku="CC01",
        quantity=12,
        unit_cost=0.50,
    )

    session.add(cc_cookie)
    session.commit()

    print(cc_cookie.cookie_id)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.2")
    print(11 * "-")

    dcc_cookie = Cookie(
        cookie_name="dark chocolate chip",
        cookie_recipe_url="awesome.cookies.miam/cookie/dcc/recipe.html",
        cookie_sku="CC02",
        quantity=1,
        unit_cost=0.75,
    )

    mol_cookie = Cookie(
        cookie_name="molasses",
        cookie_recipe_url="awesome.cookies.miam/cookie/mol/recipe.html",
        cookie_sku="MOL01",
        quantity=1,
        unit_cost=0.80,
    )

    session.add(dcc_cookie)
    session.add(mol_cookie)
    session.flush()

    print(dcc_cookie.cookie_id)
    print(mol_cookie.cookie_id)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.3")
    print(11 * "-")

    pnb_cookie = Cookie(
        cookie_name="peanut butter",
        cookie_recipe_url="awesome.cookies.miam/cookie/pnb/recipe.html",
        cookie_sku="PNB01",
        quantity=24,
        unit_cost=0.25,
    )

    oat_cookie = Cookie(
        cookie_name="oatmeal resin",
        cookie_recipe_url="awesome.cookies.miam/cookie/oat/recipe.html",
        cookie_sku="EWW01",
        quantity=100,
        unit_cost=1,
    )

    session.bulk_save_objects([pnb_cookie, oat_cookie])
    session.commit()
    print(pnb_cookie.cookie_id)
    print(oat_cookie.cookie_id)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.4")
    print(11 * "-")

    cookies = session.query(Cookie).all()
    print(cookies)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.5")
    print(11 * "-")

    # Better aproach than all -> iterable
    for cookie in session.query(Cookie):
        print(cookie)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.6")
    print(11 * "-")

    only_name_qty = session.query(Cookie.cookie_name, Cookie.quantity).first()
    print(only_name_qty)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.7")
    print(11 * "-")

    for cookie in session.query(Cookie).order_by(Cookie.quantity):
        print(f"{cookie.quantity:3} - {cookie.cookie_name}")
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.8")
    print(11 * "-")

    for cookie in session.query(Cookie).order_by(desc(Cookie.quantity)):
        print(f"{cookie.quantity:3} - {cookie.cookie_name}")
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.9")
    print(11 * "-")

    for cookie in session.query(Cookie).order_by(Cookie.quantity)[:2]:
        print(f"{cookie.quantity:3} - {cookie.cookie_name}")
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.10")
    print(12 * "-")

    query_lim = session.query(Cookie).order_by(Cookie.quantity).limit(2)
    print([result.cookie_name for result in query_lim])
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.11")
    print(12 * "-")

    inv_count = session.query(func.sum(Cookie.quantity)).scalar()
    print(inv_count)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.12")
    print(12 * "-")

    rec_count = session.query(func.count(Cookie.cookie_name)).first()
    print(rec_count)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.13")
    print(12 * "-")

    rec_count_label = session.query(
        func.count(Cookie.cookie_name).label("inventory_count")
    ).first()
    print(rec_count_label.keys(), rec_count_label.inventory_count)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.14")
    print(12 * "-")

    rec_filt = (
        session.query(Cookie).filter(Cookie.cookie_name == "chocolate chip").first()
    )
    print(rec_filt)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.15")
    print(12 * "-")

    rec_filtby = session.query(Cookie).filter_by(cookie_name="chocolate chip").first()
    print(rec_filtby)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.16")
    print(12 * "-")

    rec_like = session.query(Cookie).filter(Cookie.cookie_name.like("%chocolate%"))
    for record in rec_like:
        print(record.cookie_name)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.17")
    print(12 * "-")

    rec_conc = session.query(Cookie.cookie_name, "SKU-" + Cookie.cookie_sku).all()
    for row in rec_conc:
        print(row)
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.18")
    print(12 * "-")

    rec_cast = session.query(
        Cookie.cookie_name,
        cast((Cookie.quantity * Cookie.unit_cost), Numeric(12, 2)).label("inv_cost"),
    )

    for res in rec_cast:
        print(f"{res.cookie_name} - {res.inv_cost}")
    print("")

    # --------------------------------------------------------------------------------
    print("Exemple 7.19")
    print(12 * "-")

    print("TBD")
    print("")
