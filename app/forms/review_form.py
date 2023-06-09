from flask_wtf import FlaskForm
from wtforms.fields import (StringField, SubmitField, IntegerField, FloatField, DateTimeField)
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    # user_id = IntegerField("User Id", validators=[(DataRequired())])
    product_id = IntegerField("Product Id", validators=[(DataRequired())])
    review = StringField("Review", validators=[(DataRequired())])
    rating = FloatField("Rating", validators=[(DataRequired())])
    created_at = StringField("Created At")
    submit = SubmitField("Submit")
