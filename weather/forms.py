from django import forms


class CityForm(forms.Form):
	city = forms.CharField(max_length=25, label='',
							widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter any City'}))