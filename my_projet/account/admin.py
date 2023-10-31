from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
#admin.site.register(Coures)
@admin.register(Contact)
class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('nom','email', 'sujet', 'message')
    ordering = ('nom', )
    search_fields = ('nom', )
@admin.register(Reservation)
class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('ville_depart', 'ville_arrive', 'agences', 'type', 'nombre_services', 'date', 'nom', 'email', 'phone', 'somme_paye', 'details', )
    ordering = ('nom', )
    search_fields = ('nom', )

@admin.register(PayeTel)
class GestionnaireAmin(admin.ModelAdmin): 
    list_display=('nom', 'email', 'agences', 'somme', 'service', 'destination', 'telephone',)
    ordering = ('nom',)
    

@admin.register(PayeAgence)
class GestionnaireAmin(admin.ModelAdmin):
    list_display=('nom', 'email', 'agences', 'somme', 'service', 'destination', )
    ordering = ('nom',)
    
@admin.register(PayeBan)
class GestionnaireAmin(admin.ModelAdmin):
    list_display=('nom', 'email', 'somme', 'agences', 'service', 'destination', 'banque', )
    ordering = ('nom',)
    

    
    
    
    
       
@admin.register(Camion)
class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('marque','plaque', )
    ordering = ('plaque', )
    search_fields = ('plaque', )
    
@admin.register(Chauffer)
class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'matricule',  )
    ordering = ('nom' ,)
    search_fields = ('nom', )
    
@admin.register(Agence)
class GestionnaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'reservation', )
    ordering = ('nom',)
    search_fields = ('nom',)
    

    