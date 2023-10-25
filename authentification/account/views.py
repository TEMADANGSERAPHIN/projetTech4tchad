# from rest_framework import generics, status, viewsets, response

import csv
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import*
from django.http import  HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages  
from . forms import UserForm

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def home1(request):
  template = loader.get_template('home1.html')
  return HttpResponse(template.render())

def homeD(request):
  template = loader.get_template('homeD.html')
  return HttpResponse(template.render())

def homeS(request):
  template = loader.get_template('homeS.html')
  return HttpResponse(template.render())

def contact_list(request):
	contact = Contact.objects.all().order_by('nom')
	return render(request, 'payement/contact_list.html', {'contact': contact,})

def employes_lists(request):
	reservations = Reservation.objects.all().order_by('nom')
	return render(request, 'gestionnaire/employes_lists.html', {'reservations': reservations,})


################

def recu_list(request):
	payetel = PayeTel.objects.all().order_by('telephone')
	return render(request, 'payement/recu_list.html', {'payetel': payetel,})


def add_recu(request):
  # sourcery skip: assign-if-exp, boolean-if-exp-identity, introduce-default-else, move-assign-in-block, remove-unnecessary-cast
    submitted = False
    if request.method == "POST":
        form = PayetelForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_recu?submitted=True')
    else:
        form = PayetelForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'payement/add_recu.html', {
        'form': form,
        'submitted': submitted,
    })



def update_recu(request, payetel_id):
    payetel = PayeTel.objects.get(pk=payetel_id)
    form = PayetelForm(request.POST or None, instance=payetel)
    if form.is_valid():
        form.save()
        return redirect('recu_list')
    return render(request, 'payement/update_recu.html', {
        'payetel': payetel,
        'form': form,
    })
def delete_recu(request, payetel_id):
    payetel = PayeTel.objects.get(pk=payetel_id)
    payetel.delete()
    return redirect('recu_list')
#########

def recu_listAg(request):
	agence = PayeAgence.objects.all().order_by('nom')
	return render(request, 'payement/recu_listAg.html', {'agence': agence,})


def add_recuAg(request):
  # sourcery skip: assign-if-exp, boolean-if-exp-identity, introduce-default-else, move-assign-in-block, remove-unnecessary-cast
    submitted = False
    if request.method == "POST":
        form = PayeagenForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_recuAg?submitted=True')
    else:
        form = PayeagenForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'payement/add_recuAg.html', {
        'form': form,
        'submitted': submitted,
    })

def update_recuAg(request, agence_id):
    agence = PayeAgence.objects.get(pk=agence_id)
    form = PayeagenForm(request.POST or None, instance=agence)
    if form.is_valid():
        form.save()
        return redirect('recu_listAg')
    return render(request, 'payement/update_recuAg.html', {
        'agence': agence,
        'form': form,
    })
def delete_recuAg(request, agence_id):
    agence = PayeAgence.objects.get(pk=agence_id)
    agence.delete()
    return redirect('recu_listAg')
############
def recu_listBan(request):
	banque = PayeBan.objects.all().order_by('banque')
	return render(request, 'payement/recu_listBan.html', {'banque': banque,})


def add_recuBan(request):
  # sourcery skip: assign-if-exp, boolean-if-exp-identity, introduce-default-else, move-assign-in-block, remove-unnecessary-cast
    submitted = False
    if request.method == "POST":
        form = PayeBancForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_recuBan?submitted=True')
    else:
        form = PayeBancForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'payement/add_recuBan.html', {
        'form': form,
        'submitted': submitted,
    })

def update_recuBan(request, banque_id):
    banque = PayeBan.objects.get(pk=banque_id)
    form = PayeBancForm(request.POST or None, instance=banque)
    if form.is_valid():
        form.save()
        return redirect('recu_listBan')
    return render(request, 'payement/update_recuBan.html', {
        'banque': banque,
        'form': form,
    })
def delete_recuBan(request, banque_id):
    banque = PayeBan.objects.get(pk=banque_id)
    banque.delete()
    return redirect('recu_listBan')

########################################################""
def singin(request):  # sourcery skip: use-named-expression

    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('home1.html')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'login1.html', {})
    
    
def singinD(request):  # sourcery skip: use-named-expression

    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('homeD.html')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'loginD.html', {})
    
def singinS(request):  # sourcery skip: use-named-expression

    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('homeS.html')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'loginS.html', {})
       
   
def employes_list(request):
	reservations = Reservation.objects.all().order_by('nom')
	return render(request, 'gestionnaire/employes_list.html', {'reservations': reservations,})

def add_employe(request):
  # sourcery skip: assign-if-exp, boolean-if-exp-identity, introduce-default-else, move-assign-in-block, remove-unnecessary-cast
      submitted = False
      if request.method == "POST":
            form = ReservationForm(request.POST, request.FILES)
            if form.is_valid():
                  form.save()
            return HttpResponseRedirect('/add_employe?submitted=True')
      else:
            form = ReservationForm
      if 'submitted' in request.GET:
            submitted=True
      return render(request, 'gestionnaire/add_employe.html', {
        'form': form,
        'submitted': submitted,
        })

def show_employe(request, reservation_id):
    reservations = Reservation.objects.get(pk=reservation_id)
    return render(request, 'gestionnaire/show_employe.html', {'reservations': reservations,})
      
def delete_employe(request, reservation_id):
    employe = Reservation.objects.get(pk=reservation_id)
    employe.delete()
    return redirect('employes_list')


def update_employe(request, reservation_id):
    employe = Reservation.objects.get(pk=reservation_id)
    form = ReservationForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
        return redirect('employes_list')
    return render(request, 'gestionnaire/update_employe.html', {
        'employe': employe,
        'form': form,
    })  

def search_employe(request):
  # sourcery skip: remove-unnecessary-else, use-named-expression
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            mutiple_q = Q (Q(matricule=query) | Q(nom=query))
        reservations = Reservation.objects.filter(mutiple_q)
        if reservations:
            return render(request, 'gestionnaire/employes_list.html', {
                'reservation': reservations
            })
        else:
            print('Not found ...')
            return render(request, 'gestionnaire/not_found.html', {})


# from django.conf import settings
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.urls import reverse
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode

# # from . import serializers


# class PasswordReset(generics.GenericAPIView):
#     """
#     Request for Password Reset Link.
#     """

#     serializer_class = serializers.EmailSerializer

#     def post(self, request):
#         """
#         Create token.
#         """
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.data["email"]
#         if user := User.objects.filter(email=email).first():
#             encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
#             token = PasswordResetTokenGenerator().make_token(user)
#             reset_url = reverse(
#                 "reset-password",
#                 kwargs={"encoded_pk": encoded_pk, "token": token},
#             )
#             reset_link = f"localhost:8000{reset_url}"

#             # send the rest_link as mail to the user.

#             return response.Response(
#                 {
#                     "message": 
#                     f"Your password rest link: {reset_link}"
#                 },
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return response.Response(
#                 {"message": "User doesn't exists"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )


# class ResetPasswordAPI(generics.GenericAPIView):
#     """
#     Verify and Reset Password Token View.
#     """

#     serializer_class = serializers.ResetPasswordSerializer

#     def patch(self, request, *args, **kwargs):
#         """
#         Verify token & encoded_pk and then reset the password.
#         """
#         serializer = self.serializer_class(
#             data=request.data, context={"kwargs": kwargs}
#         )
#         serializer.is_valid(raise_exception=True)
#         return response.Response(
#             {"message": "Password reset complete"},
#             status=status.HTTP_200_OK,
#         )




# def register1(request):
#     return render(request, "resister.htmlt")


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context) 

def service(request):
  return render(request, 'services.html')

def reduction(request):
  return render(request, 'pricing.html')

def client(request):
  return render(request, 'contact_admin.html')

def chargement(request):
  return render(request, 'chargement.html')

def preparation(request):
  return render(request, 'preparation.html')

def dechargement(request):
  return render(request, 'dechargement.html')

## Reservation

def propos(request):
  return render(request, 'propos.html')

def paye(request):
  return render(request, 'paye.html')

def tache(request):
  return render(request, 'tache.html')

def tache1(request):
  return render(request, 'tache1.html')

def tache2(request):
  return render(request, 'tache2.html')

def ServiceDetail(request):
  return render(request, 'service-details.html')

 
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre réservation a été créée avec succès.")  # Message de succès
            return redirect('paye.html')  # Rediriger vers la page de confirmation
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")  # Message d'erreur
    else:
        form = ReservationForm()

    context = {
        'form': form,
    }

    return render(request, 'get-a-quote.html', context)


  
def payetel(request):
    if request.method == 'POST':
        form = PayetelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre réservation a été créée avec succès.")  # Message de succès
            return redirect('tache1')  # Rediriger vers la page de confirmation
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")  # Message d'erreur
    else:
        form = PayetelForm()

    context = {
        'form': form,
    }

    return render(request, 'payetel.html', context)  
  
  
def payeagence(request):
    if request.method == 'POST':
        form = PayeagenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre réservation a été créée avec succès.")  # Message de succès
            return redirect('tache2')  # Rediriger vers la page de confirmation
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")  # Message d'erreur
    else:
        form = PayeagenForm()

    context = {
        'form': form,
    }

    return render(request, 'payeagen.html', context)  
  
def payeban(request):
    if request.method == 'POST':
        form = PayeBancForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre réservation a été créée avec succès.")  # Message de succès
            return redirect('tache')  # Rediriger vers la page de confirmation
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")  # Message d'erreur
    else:
        form = PayeBancForm()

    context = {
        'form': form,
    }

    return render(request, 'payeban.html', context)  
 
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre réservation a été créée avec succès.")  # Message de succès
            return redirect('paye')  # Rediriger vers la page de confirmation
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")  # Message d'erreur
    else:
        form = ReservationForm()

    context = {
        'form': form,
    }

    return render(request, 'get-a-quote.html', context)
  


def sing_in(request):  # sourcery skip: use-named-expression

    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('reservation')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'login.html', {})



def sing_up(request):
    # sourcery skip: extract-method, simplify-boolean-comparison, swap-nested-ifs, use-named-expression
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except Exception:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False and password != repassword:
            error = True
            message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"

        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('sing_in')

            #print("=="*5, " NEW POST: ",name,email, password, repassword, "=="*5)

    context = {
        'error':error,
        'message':message
    }
    return render(request, 'register.html', context)


@login_required(login_url='sing_in')
def dashboard(request):
    return render(request, 'admin.html', {})

def log_out(request):
    logout(request)
    return redirect('sing_in')


def forgot_password(request):
    error = False
    success = False
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        if user := User.objects.filter(email=email).first():
            print("processing forgot password")
            html = """
                <p> Hello, merci de cliquer pour modifier votre email </p>
            """

            msg = EmailMessage(
                "Modification de mot de pass!",
                html,
                "soroib0879@gmail.com",
                ["soro4827@gmail.com"],
            )

            msg.content_subtype = 'html'
            msg.send()

            message = "processing forgot password"
            success = True
        else:
            print("user does not exist")
            error = True
            message = "user does not exist"

    context = {
        'success': success,
        'error':error,
        'message':message
    }
    return render(request, "forgot_password.html", context)


def update_password(request):
    return render(request, "update_password.html", {})
