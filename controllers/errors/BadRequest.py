# Dependencies
import importlib
from aurora import Controller, View

# The controller class
class BadRequest(Controller):

	# HTTP GET Method
    def get(self):
        consts = importlib.import_module(f"assets.consts.{Controller().active_lang}")
        return View('400', code=400, consts=consts, LANGUAGE=Controller().LANGUAGE)
