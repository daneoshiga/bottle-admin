# coding: utf-8


class Admin():
    """
    Creates an admin interface for models
    """

    def __init__(self, app=None):
        self.app = app
        self._models = []

    @classmethod
    def register(self, model=None, modeladmin=None):
        self._models.append((model, modeladmin))
        print(self._models)
