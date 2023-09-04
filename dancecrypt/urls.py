from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myaccounts import views as account_views
from myfolio import views as folio_views
from myreports import views as report_views
from myresearch import views as research_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', folio_views.dashboard, name='dashboard'),

    path('dashboard/', folio_views.dashboard, name='dashboard'),
    path('dashboard/reports', report_views.reports_dashboard, name='reports_dashboard'),

    path('users/username', folio_views.public_timeline, name='user_public_timeline'),
    path('users/username/archive', folio_views.public_archive, name='user_public_archive'),
    path('about/', research_views.about, name='about'),

    path('accounts/signup', account_views.account_signup, name='account_signup'),
    path('accounts/signin', account_views.account_sign_in, name='account_sign_in'),
    path('accounts/personal', account_views.account_personal_settings, name='account_personal_settings'),
    path('accounts/security', account_views.account_security_settings, name='account_security_settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)