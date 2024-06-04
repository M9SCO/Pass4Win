import os

import pydantic


class Config(pydantic.BaseModel):
    __resource_path = f"resources{os.sep}"
    __logging_file = __resource_path + ".log"
    __db_file = __resource_path + "local.db"

    @property
    def resource_path(self):
        return self.__resource_path

    @property
    def logging_file(self):
        return self.__logging_file

    @property
    def db_file(self):
        return self.__db_file

    @property
    def db_url(self):
        return "sqlite:///" + self.db_file


config = Config()
