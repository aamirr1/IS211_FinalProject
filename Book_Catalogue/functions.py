from sqlalchemy import  *
import conf


def get_user(username,password):
    getUser = select([conf.Users]).where(and_(conf.Users.c.username == username, conf.Users.c.password == password))
    getUser = conf.connection.execute(getUser).first()
    return getUser


def getAllBooks(id):
    getBooks = select([conf.BookCatalogue]).where(
        conf.BookCatalogue.c.user_id == id)
    getBooks = conf.connection.execute(getBooks)
    result = []
    for item in getBooks:
        result.append(dict(item))

    return result
