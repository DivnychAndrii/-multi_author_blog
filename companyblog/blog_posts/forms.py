from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):

    title = StringField("Enter your title: ", validators=[DataRequired()])
    text = TextAreaField("And text here: ",validators=[DataRequired()])
    submit = SubmitField("Post")
