from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=4, max=50)])
    middle_name = StringField('Middle Name', validators=[DataRequired(), Length(min=1, max=40)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=4, max=40)])
    email = StringField('Email', validators=[DataRequired(), Length(min=4, max=50), Email()])
    mother_name = StringField("Mother's Name", validators=[DataRequired(), Length(min=4, max=40)])
    father_name = StringField("Father's Name", validators=[DataRequired(), Length(min=4, max=40)])
    address = StringField('Contact Address', validators=[DataRequired(), Length(min=2, max=80)])
    submit = SubmitField('SIGN UP')