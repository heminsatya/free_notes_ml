# Dependencies
import importlib
from aurora import Controller, View

# The controller class
class NotFound(Controller):

	# HTTP GET Method
    def get(self):
        consts = importlib.import_module(f"assets.consts.{Controller().active_lang}")
        return View('404', code=404, consts=consts, LANGUAGE=Controller().LANGUAGE)
