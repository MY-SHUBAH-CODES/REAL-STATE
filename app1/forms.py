from django.forms import ModelForm
from .models import Addland,Addplot
from django import forms

class Addlandform(ModelForm):
    class Meta:
        model = Addland
        fields = ['land_pic1','land_pic2','land_pic3','land_pic4','land_pic5','land_description']


class Addplotform(ModelForm):
    class Meta:
        model = Addplot
        fields = ['plot_pic1','plot_pic2','plot_pic3','plot_pic4','plot_pic5','plot_description']

