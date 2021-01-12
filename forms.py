from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,InputRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateTimeLocalField
from datetime import date, datetime
from wtforms.fields import SelectField



class PredictionForm(FlaskForm):
    Dep_Time = DateTimeLocalField('Dep_Time', validators=[DataRequired()],format='%Y-%m-%dT%H:%M')
    Arrival_Time = DateTimeLocalField('Arrival_Time', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
    Source = SelectField('Source', choices=[('Delhi', 'Delhi'), ('Kolkata','Kolkata'),('Mumbai','Mumbai'),('Chennai','Chennai')],validators=[DataRequired()])
    Destination = SelectField('Destination', choices=[('Cochin','Cochin'),('Delhi', 'Delhi'), ('New Delhi','New Delhi'),('Hyderabad','Hyderabad'),('Kolkata','Kolkata')],validators=[DataRequired()])
    Stops = SelectField('Stops', choices=[('0', 'Non-Stop'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], validators=[InputRequired()])
    airline = SelectField('airline', choices=[('Jet Airways', 'Jet Airways'), ('IndiGo', 'IndiGo'), ('Air India', 'Air India'), ('Multiple carriers', 'Multiple carriers'), ('SpiceJet', 'SpiceJet'), ('Vistara', 'Vistara'), ('GoAir', 'GoAir'), ('Jet Airways Business', 'Jet Airways Business'), ('Vistara Premium economy', 'Vistara Premium economy')], validators=[DataRequired()])
    submit = SubmitField('Predict')
    def validate_time(self):
        if self.Dep_Time.data < self.Arrival_Time.data:
            return True
        else:
            return False

    def validate_dest(self):
        if self.Source.data != self.Destination.data:
            return True
        else:
            return False

    def validate_curr_dep_time(self):
        now = datetime.now()
        dt_string = now.strftime('%Y-%m-%dT%H:%M')
        date_time_str = dt_string
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M')
        if(self.Dep_Time.data > date_time_obj):
            return True
        else:
            return False

    def validate_curr_arr_time(self):
        now = datetime.now()
        dt_string = now.strftime('%Y-%m-%dT%H:%M')
        date_time_str = dt_string
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M')
        if(self.Arrival_Time.data > date_time_obj):
            return True
        else:
            return False


