# Dependencies
import importlib
from aurora import Controller, View

# The controller class
class MethodForbidden(Controller):

	# HTTP GET Method
    def get(self):
        consts = importlib.import_module(f"assets.consts.{Controller().active_lang}")
        return View('405', code=405, consts=consts, LANGUAGE=Controller().LANGUAGE)
