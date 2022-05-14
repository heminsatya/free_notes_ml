# Dependencies
import importlib
from aurora import Controller, View
from models import Users, Notes as NotesModel
from aurora.security import request, get_session, login_required

# The controller class
class Notes(Controller):

    # Constructor
    def __init__(self):
        super().__init__()
        self.consts = importlib.import_module(f'assets.consts.{self.active_lang}')

    # GET Method
    @login_required(app='users')
    def get(self):
        # The required models
        user = Users().read(where={'username':get_session('user')}).first()
        notes = NotesModel().read(where={'user_id':user['id']}, order_by={'id':'DESC'}).all()

        return View('notes', consts=self.consts, LANGUAGE=self.LANGUAGE, user=user, notes=notes)

    # DELETE Method
    @login_required(app='users')
    def delete(self):
        # The required models
        user = Users().read(where={'username':get_session('user')}).first()
        notes = NotesModel()

        # Form data
        data = request.json
        id = data['id']

        # Check if the note is users' note
        if notes.read(where={'id':id, 'user_id':user['id']}).count() != 1:
            return {
                'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Forbidden data requested!',
            }, 400

        # Everything is fine
        # Delete note from the database
        notes.delete(where={'id':id})

        # Return the result
        return {
            'success': '<i class="fas fa-check-circle mr-1"></i> The note deleted successfully!',
        }, 200

