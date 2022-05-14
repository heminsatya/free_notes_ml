# Dependencies
import importlib
from aurora import Controller, View

# The controller class
class ServerError(Controller):

	# HTTP GET Method
    def get(self):
        consts = importlib.import_module(f"assets.consts.{Controller().active_lang}")
        return View('500', code=500, consts=consts, LANGUAGE=Controller().LANGUAGE)
