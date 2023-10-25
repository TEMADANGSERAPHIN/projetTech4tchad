from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static





from account.views import (
    sing_in, singin, singinD, singinS, sing_up, dashboard, log_out, contact_list, employes_lists,
    forgot_password, update_password, index, reservation, contact, service, reduction, tache,tache1, tache2, payetel, payeagence,payeban, ServiceDetail,
    chargement, dechargement, preparation, propos, paye
)


urlpatterns = [
    
    
    path('', index, name='index'),
    
    path('home.html', views.home, name='home'),
    path('home1.html', views.home1, name='home1'),
    path('homeS.html', views.homeS, name='homeS'),
    path('homeD.html', views.homeD, name='homeD'),
    path('singin', singin, name='singin'),
    path('singinS', singinS, name='singinS'),
    path('singinD', singinD, name='singinD'),
    
    path('contact_list', contact_list, name='contact_list'),
    path('employes_lists', views.employes_lists, name='employes_lists'),
    
    path('recu_list', views.recu_list, name='recu_list'),
    path('add_recu', views.add_recu, name='add_recu'),
    path('update_recu/<payetel_id>', views.update_recu, name='update_recu'),
    path('delete_recu/<payetel_id>', views.delete_recu, name='delete_recu'),
    path('search_employe', views.search_employe, name='search_employe'),
    
    path('recu_listAg', views.recu_listAg, name='recu_listAg'),
    path('add_recuAg', views.add_recuAg, name='add_recuAg'),
    path('update_recuAg/<agence_id>', views.update_recuAg, name='update_recuAg'),
    path('delete_recuAg/<agence_id>', views.delete_recuAg, name='delete_recuAg'),
    path('search_employeAg', views.search_employe, name='search_employeAg'),
    
    path('recu_listBan', views.recu_listBan, name='recu_listBan'),
    path('add_recuBan', views.add_recuBan, name='add_recuBan'),
    path('update_recuBan/<banque_id>', views.update_recuBan, name='update_recuBan'),
    path('delete_recuBan/<banque_id>', views.delete_recuBan, name='delete_recuBan'),
    path('search_employe', views.search_employe, name='search_employe'),
    
    
    path('employes_list', views.employes_list, name='employes_list'),
    path('add_employe', views.add_employe, name='add_employe'),
    path('show_employe/<reservation_id>', views.show_employe, name='show_employe'),
    path('delete_employe/<reservation_id>', views.delete_employe, name='delete_employe'),
    path('update_employe/<reservation_id>', views.update_employe, name='update_employe'),
    
    
    path('contact', contact, name='contact'),
    
    
    
    path('service', service, name='service'),
    
    
    path('reduction', reduction, name='reduction'),
    
        
    path('tache', tache, name='tache'),
    path('tache1', tache1, name='tache1'),
    path('tache2', tache2, name='tache2'),
    
    path('payetel', payetel, name='payetel'),
    path('payeagence', payeagence, name='payeagence'),
    path('payeban', payeban, name='payeban'),
    
    path('serviceDetail', ServiceDetail, name='ServiceDetail'),
    
    path('chargement', chargement, name='chargement'),
    path('dechargement', dechargement, name='dechargement'),
    path('preparation', preparation, name='preparation'),
    
    path('propos', propos, name='propos'),
    path('paye', paye, name='paye'),
    
    
    path('reservation', reservation, name='reservation'),
    path('#', dashboard, name='dashboard'),
    path('login', sing_in, name='sing_in'),
    path('register', sing_up, name='sing_up'),
    path('logout', log_out, name='log_out'),
    path('forgot-password', forgot_password, name='forgot_password'),
    path('update-password', update_password, name='update_password'),
]


