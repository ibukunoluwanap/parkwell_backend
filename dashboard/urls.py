from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('company/', views.DashboardCompany.as_view(), name='dashboard_company'),
    path('company_detail/<int:pk>/', views.DashboardCompanyDetail.as_view(), name='dashboard_company_detail'),
    path('company_add/', views.DashboardCompanydAdd.as_view(), name='dashboard_company_add'),
    path('company_edit/<int:pk>/', views.DashboardCompanyEdit.as_view(), name='dashboard_company_edit'),
    path('company_delete/<int:pk>/', views.DashboardCompanyDelete.as_view(), name='dashboard_company_delete'),

    path('park/', views.DashboardPark.as_view(), name='dashboard_park'),
    path('park_detail/<int:pk>/', views.DashboardParkDetail.as_view(), name='dashboard_park_detail'),
    path('park_add/', views.DashboardParkdAdd.as_view(), name='dashboard_park_add'),
    path('park_edit/<int:pk>/', views.DashboardParkEdit.as_view(), name='dashboard_park_edit'),
    path('park_delete/<int:pk>/', views.DashboardParkDelete.as_view(), name='dashboard_park_delete'),

    path('check_email/<email>/', views.DashboardCheckEmail.as_view(), name='dashboard_check_email'),
    path('waitlist/', views.DashboardWaitlist.as_view(), name="dashboard_waitlist"),

    path('export_waitlist/', views.export_waitlist, name="export_waitlist"),
    path('export_verified_company_admin/', views.export_verified_company_admin, name="export_verified_company_admin"),
    path('export_non_verified_company_admin/', views.export_non_verified_company_admin, name="export_non_verified_company_admin"),
    path('export_park_admin/', views.export_park_admin, name="export_park_admin"),
    path('export_all_users/', views.export_all_users, name="export_all_users"),

    path('cadmin/', views.DashboardCompanyAdmin.as_view(), name='dashboard_cadmin'),
    path('cadmin/delete/<int:pk>/', views.DashboardCompanyAdminDelete.as_view(), name='dashboard_cadmin_delete'),
    path('cadmin/verify_admin/<int:pk>/', views.VerifyAdmin.as_view(), name='dashboard_verify_admin'),
    path('padmin/', views.DashboardParkAdmin.as_view(), name='dashboard_padmin'),
    path('padmin/delete/<int:pk>/', views.DashboardParkAdminDelete.as_view(), name='dashboard_padmin_delete'),
    path('bookings/', views.DashboardBookings.as_view(), name='dashboard_bookings'),

    path('users_info/', views.DashboardUsersInfo.as_view(), name='dashboard_users_info'),
    path('users_info_delete/<int:pk>/', views.DashboardUsersInfoDelete.as_view(), name='dashboard_users_info_delete'),
]