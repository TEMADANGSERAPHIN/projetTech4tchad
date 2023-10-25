from django import forms
from django.forms import ModelForm 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets={
			'username': forms.TextInput(),
			'email': forms.EmailInput()
		}
        
    password1 = forms.CharField()
    password2 = forms.CharField()

class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = [ 'ville_depart', 'ville_arrive', 'type', 'date', 'nom', 'email','phone','details',]

		labels = {
			'ville_depart': 'Depart', 
			'ville_arrive': 'Destination',       
			'type': 'Selectionner le type de reservation ', 
			'date': 'date de voyage',
			'nom': 'Votre nom',
			'email':'Votre adresse mail', 
			'phone': 'Votre numero de telephone',
            'details': 'Entrer votre message'
        }

		widgets = {
			'ville_depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre ville de depart',}), 
			'ville_arrive': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre destination',}), 
   			'type': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Type',}), 
			'date': forms.DateInput(attrs={'class': 'form-control','type':'datetime-local'}),
			'nom': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Votre nom',}),
            'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre numero de telephone',}),
            'details': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre message',}), 
		}

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'email', 'sujet', 'message']
        
        labels = {
			'nom': 'votre nom',       
			'email': 'Entrer votre adresse electronique ', 
			'sujet': 'Votre sujet',
			'message':'Votre message'
			
        }
        
        widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre ville de depart',}), 
			'ville_arrive': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre destination',}), 
            'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'email'}),
            'sujet': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre numero de telephone',}),
            'message': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre message',}), 
		}

class PayetelForm(forms.ModelForm):
	class Meta:
		model = PayeTel
		fields = [ 'nom', 'email', 'service', 'destination','telephone',]

		labels = {
			'nom': 'Votre nom', 
			'email': 'Email',       
			'service': 'Selectionner le type de reservation ', 
			'destination': 'Destination',
			'telephone': 'Votre numero de téléphone',

        }

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom',}), 
			'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'email'}),
   			'service': forms.Select(attrs={'class': 'form-select', 'placeholder': 'service',}), 
			'destination': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Destination',}),               
            'telephone': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre numero de telephone',}),
		}


class PayeagenForm(forms.ModelForm):
	class Meta:
		model = PayeAgence
		fields = [ 'nom', 'email', 'service', 'destination',]

		labels = {
			'nom': 'Votre nom', 
			'email': 'Email',       
			'service': 'Selectionner le type de reservation ', 
			'destination': 'Destination',

        }

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom',}), 
			'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'email'}),
   			'service': forms.Select(attrs={'class': 'form-select', 'placeholder': 'service',}), 
			'destination': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Destination',}),               
		}

class PayeBancForm(forms.ModelForm):
	class Meta:
		model = PayeBan
		fields = [ 'nom', 'email', 'service', 'destination','banque',]

		labels = {
			'nom': 'Votre nom', 
			'email': 'Email',       
			'service': 'Selectionner le type de reservation ', 
			'destination': 'Destination',
			'banque': 'Votre nom de votre banque',

        }

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom',}), 
			'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'email'}),
   			'service': forms.Select(attrs={'class': 'form-select', 'placeholder': 'service',}), 
			'destination': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Destination',}),               
            'banque': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre banque',}),
		}
#################################

class PayeBancForm(forms.ModelForm):
	class Meta:
		model = PayeBan
		fields = [ 'nom', 'email', 'service', 'destination','banque',]

		labels = {
			'nom': 'Votre nom', 
			'email': 'Email',       
			'service': 'Selectionner le type de reservation ', 
			'destination': 'Destination',
			'banque': 'Votre nom de votre banque',

        }

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom',}), 
			'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'email'}),
   			'service': forms.Select(attrs={'class': 'form-select', 'placeholder': 'service',}), 
			'destination': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Destination',}),               
            'banque': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre banque',}),
		}


############
class PayeBancForm(forms.ModelForm):
	class Meta:
		model = PayeBan
		fields = [ 'nom', 'email', 'service', 'destination','banque',]

		labels = {
			'nom': 'Votre nom', 
			'email': 'Email',       
			'service': 'Selectionner le type de reservation ', 
			'destination': 'Destination',
			'banque': 'Votre nom de votre banque',

        }

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom',}), 
			'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'email'}),
   			'service': forms.Select(attrs={'class': 'form-select', 'placeholder': 'service',}), 
			'destination': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Destination',}),               
            'banque': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre banque',}),
		}
#####################