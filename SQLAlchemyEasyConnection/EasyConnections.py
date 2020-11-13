from sqlalchemy import create_engine
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy.orm import sessionmaker, scoped_session
from SQLAlchemyEasyConnection import Utilities


class EasyConnection:
    def __init__(self):
        self.engine = None
        self.session = None

    def connect_to_database(self, type_database: str = "", user: str = "", password: str = "", host: str = "localhost",
                            port: str = "", database: str = "", sqlite_check_same_thread: bool = False,
                            pool_size: int = 600, max_overflow: int = 0, pool_recycle: int = 1) -> bool:
        connection_string = Utilities.generate_connection_string(type_database=type_database, user=user,
                                                                 password=password, host=host, port=port,
                                                                 database=database)
        if type_database.lower() == "sqlite":
            if sqlite_check_same_thread:
                connection_string = connection_string + '?check_same_thread=False'
            self.engine = create_engine(connection_string,
                                        poolclass=SingletonThreadPool)
            print("Using SQLite on file: " + sqlite_check_same_thread.connection_string())
            session = sessionmaker(bind=self.engine)
            self.session = scoped_session(session)
        else:
            self.engine = create_engine(connection_string, pool_size=pool_size, max_overflow=max_overflow,
                                        pool_recycle=pool_recycle)
            session = sessionmaker(bind=self.engine)
            self.session = session()

    def session_commit(self) -> None:
        """
        Commit changes into database.

        :return:
        """
        self.session.commit()

    def session_rollback(self):
        """
        Rollback last not committed changes.

        :return:
        """
        self.session.rollback()

    def insert_item(self, element):
        """
        Add new item.

        :param element: ORM instance.
        :return:
        """
        self.session.add(element)

    def insert_items(self, elements):
        """
        Add many items.

        :param elements: list: List of ORM instances.
        :return:
        """
        if isinstance(elements, list):
            self.session.add_all(elements)

    def delete_item(self, element):
        """
        Delete a item.

        :param element: ORM instance.
        :return:
        """
        self.session.delete(element)

    @property
    def get_engine(self):
        return self.engine

    @property
    def get_session(self):
        return self.session
