# from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(FlaskForm):
    """Image upload form."""
    upload = FileField(
        'image',
        [FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images of format .png or .jpg')]
    )
    submit = SubmitField('Submit')