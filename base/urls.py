from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from .views import LoginView, RegisterView, HomeView, LogoutView, RFPView, VendorView, AddRFPView, CategoryView, RemoveVendorView, AddCategoryView, ApproveVendorView, RemoveRFPView, ApplyRFPView, GetQuotesView, VendorQuotesView, RegisterAdminView, GetCategoryRequestsView

urlpatterns = [
    # path('', AdminRegisterView, name='admin-login'),
    path('', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('registervendor/', RegisterView, name='register'),
    path('registeradmin/', RegisterAdminView, name='registeradmin'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='base/password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='base/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='base/password_reset_complete.html'), name='password_reset_complete'),
    

    path('dashboard/', HomeView, name='home'),

    path('getrfp/', RFPView, name='rfp'),
    path('addrfp/', AddRFPView, name='add-rfp'),
    path('removerfp/<int:pk>', RemoveRFPView, name='remove-rfp'),

    path('getvendors/', VendorView, name='vendors'),
    path('approvevendor/<int:pk>', ApproveVendorView, name='approve-vendor'),
    path('removevendor/<int:pk>', RemoveVendorView, name='remove-vendor'),

    path('getcategories/', CategoryView, name='categories'),
    path('addcategory/', AddCategoryView, name='add-category'),
    path('getcategoryrequests/<int:pk>', GetCategoryRequestsView, name='categoryrequests'),

    path('applyrfp/<int:pk>', ApplyRFPView, name='apply-rfp'),

    path('getquotes/<int:pk>', GetQuotesView, name='getquotes'),
    path('vendorquotes/', VendorQuotesView, name='vendorquotes'),

]