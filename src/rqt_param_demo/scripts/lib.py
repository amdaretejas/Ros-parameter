import sqlite3
import json
import time
import threading
from dynamic_reconfigure.server import Server
from sql import SQLiteParamStore
from copy import deepcopy

class ParamStore:
    def __init__(self, configFile, key, callback = None, dbName="params.db"):
        self.key = key
        print("This is config file: ")
        self.database = SQLiteParamStore(dbName)
        self.user_callback = callback
        self.server = Server(configFile, self._callback_function)
        self.default = True

    def _callback_function(self, parameters, level):
        # parameters["groups"]["parameters"]["linear_speed"] = 0.5
        # parameters["groups"]["parameters"]["angular_speed"] = 1.0
        # parameters["groups"]["parameters"]["acceleration_limit"] = 1.0
        # parameters["groups"]["parameters"]["enable_motion"] = True
        # print("I am inside config")
        # print(parameters)
        # print(parameters["groups"]["parameters"])
        self.config = deepcopy(parameters)
        for values in parameters["groups"]["parameters"]:
            if values != "groups":
                default_value = self.database.get(f"{self.key}.{values}", parameters["groups"]["parameters"][values])
                # print("default: ", default_value)
                if parameters["groups"]["parameters"][values] == parameters[values]:
                    parameters[values] = default_value
                if parameters["groups"]["parameters"][values] != default_value:
                    parameters["groups"]["parameters"][values] = default_value

        for values in parameters:
            if values != "groups":
                # print(parameters["groups"]["parameters"][values])
                if parameters["groups"]["parameters"][values] != parameters[values]:
                    self.database.set(f"{self.key}.{values}", parameters[values])
                self.config[values] = self.database.get(f"{self.key}.{values}", parameters["groups"]["parameters"][values])
        if self.user_callback:
            self.user_callback(self.config, level)
        return parameters
