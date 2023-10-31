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
		fields = [ 'ville_depart', 'ville_arrive', 'agences', 'type', 'nombre_services', 'date', 'nom', 'email', 'phone', 'somme_paye', 'details',]

		labels = {
			'ville_depart': 'Depart', 
			'ville_arrive': 'Destination',   
			'agences': 'Choisir une agence',
			'type': 'Selectionner le type de service ', 
			'nombre_services': 'Entrer le nombre de services souhaités',
			'date': 'date de voyage',
			'nom': 'Votre nom',
			'email':'Votre adresse mail', 
			'phone': 'Votre numero de telephone',
			'somme_paye': 'Sommes du service',
            'details': 'Entrer votre message'
        }

		widgets = {
			'ville_depart': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre ville de depart',}), 
			'ville_arrive': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre destination',}), 
			'agences': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Agence',}),
   			'type': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Type',}), 
			'nombre_services': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir les nombres de service souhaités',}),
			'date': forms.DateInput(attrs={'class': 'form-control','type':'datetime-local'}),
			'nom': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Votre nom',}),
			'matricule': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Votre matricule',}),
            'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre numero de telephone',}),
            'somme_paye': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir la sommes total du service',}),
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
		fields = [ 'nom', 'email', 'agences', 'somme', 'service', 'destination', 'telephone', ]

		labels = {
			'nom': 'Votre nom', 
			'email': 'Email',
			'agences': 'Selection Agence',
			'somme': 'Payer le montant de :',
			'service': 'Selectionner le type de reservation ', 
			'destination': 'Destination',
			'telephone': 'Votre numero de téléphone',

        }

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom',}), 
			'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'Email'}),
			'agences': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Agence',}),
			'somme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir la sommes total du service',}),
   			'service': forms.Select(attrs={'class': 'form-select', 'placeholder': 'service',}), 
			'destination': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Destination',}),               
            'telephone': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre numero de telephone',}),
		}


class PayeagenForm(forms.ModelForm):
	class Meta:
		model = PayeAgence
		fields = [ 'nom', 'email', 'agences', 'somme', 'service', 'destination', ]

		labels = {
			'nom': 'Votre nom', 
			'email': 'Email',
			'agences': 'Selection Agence',
			'somme': 'Payer le montant de :',
			'service': 'Selectionner le type de reservation ', 
			'destination': 'Destination',

        }

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom',}), 
			'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'Email'}),
			'agences': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Agence',}),
			'somme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir la sommes total du service',}),
   			'service': forms.Select(attrs={'class': 'form-select', 'placeholder': 'service',}), 
			'destination': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Destination',}),               
		}

class PayeBancForm(forms.ModelForm):
	class Meta:
		model = PayeBan
		fields = [ 'nom', 'email', 'somme', 'agences', 'service', 'destination', 'banque', ]

		labels = {
			'nom': 'Votre nom', 
			'email': 'Email',			
			'somme': 'Payer le montant de :',
			'agences': 'Selection Agence',
			'service': 'Selectionner le type de reservation ', 
			'destination': 'Destination',
			'banque': 'Votre nom de votre banque',

        }

		widgets = {
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom',}), 
			'email': forms.EmailInput(attrs={'class': 'form-select', 'placeholder': 'Email'}),
			'agences': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Agence',}),
			'somme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir la sommes total du service',}),
   			'service': forms.Select(attrs={'class': 'form-select', 'placeholder': 'service',}), 
			'destination': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Destination',}),               
            'banque': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Saisir votre banque',}),
		}
