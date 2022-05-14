# Dependencies
import importlib
from aurora import Controller, View, Forms
from models import Users, Notes
from aurora.security import request, login_required, get_session

# The controller class
class NewNote(Controller):

    # Constructor
    def __init__(self):
        super().__init__()
        self.consts = importlib.import_module(f'assets.consts.{self.active_lang}')

    # POST Method
    @login_required(app='users')
    def post(self):
        # The required models
        user = Users().read(where={'username':get_session('user')}).first()
        notes = Notes()

        # Form data
        data = request.form
        form = Forms(data)

        # Valid form data
        if form.validate():
            # Collect form inputs
            title = data.get('title')
            content = data.get('content')

            # Required fields
            if not title or not content:
                return {
                    'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Form data is invalid!',
                }, 400

            # Everything is fine
            # Insert new note into the database
            data = {
                'user_id': user['id'],
                'title': title,
                'content': content,
                # 'date': datetime.now().strftime("%m-%d-%Y")
            }
            notes.create(data=data)

            # Return the result
            return {
                'success': '<i class="fas fa-check-circle mr-1"></i> The new note created successfully!',
            }, 200

        # Invalid form data
        else:
            # Return the result
            return {
                'error': '<i class="fas fa-exclamation-triangle mr-1"></i> Form data is invalid!',
            }, 400


    # GET Method
    @login_required(app='users')
    def get(self):
        # The required models
        user = Users().read(where={'username':get_session('user')}).first()
        notes = Notes().read(where={'user_id':user['id']}, order_by={'id':'DESC'}).all()

        form = Forms()
        
        return View('create', consts=self.consts, LANGUAGE=self.LANGUAGE, user=user, form=form)

