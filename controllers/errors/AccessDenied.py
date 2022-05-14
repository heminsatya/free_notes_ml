# Dependencies
import importlib
from aurora import Controller, View

# The controller class
class AccessDenied(Controller):

	# HTTP GET Method
    def get(self):
        consts = importlib.import_module(f"assets.consts.{Controller().active_lang}")
        return View('403', code=403, consts=consts, LANGUAGE=Controller().LANGUAGE)
