"""
URL configuration for service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('about',views.about),
    path('terms',views.terms),
    path('jobs',views.jobs),
    path('job_details/<user>',views.job_details),
    path('property-details.html',views.property),

    path('admin/',admin.site.urls),
    path('adm_index',views.adm_index),
    path('adm_form', views.adm_form),
    path('adm_table', views.adm_table),
    path('userlist',views.userlist),
    path('accept',views.accept),
    path('', views.index),
    path('p',views.ad_request),
    path('profile1',views.profile1),
    path('profile2',views.profile2),
    path('profile3',views.profile3),
    path('profile4',views.profile4),
    path('index',views.index),
    path('index1', views.user_index),
    path('EM', views.EM),
    path('emp_index',views.emp_index),
    # path('emp_viewww',views.emp_viewww),
    path('emp_view', views.emp_view),
    path('emp_feedback',views.emp_feed),
    path('emp_profeed',views.emp_profeed),
    path('msg',views.message_admin),
    path('user_reg',views.user_reg),
    # path('pay', views.payment),
    path('un_profile',views.emp_profile),
    path('login',views.login),
    # path('login1',views.login1),
    path('logout',views.logout),

    path('feed',views.feedcreate),
    path('cfeed',views.common_feed),
    path('cfeed_list',views.common_feedlist),
    path('feedback_list',views.feedlist),

    path('newadm',views.new_admin),
    path('newadmin_table',views.newadmin_table),
    path('newadm_msg',views.newadm_message),
    path('remove',views.remove),
    path('remove1',views.remove1),

    path('admn',views.admn),    #------------------------admin dashboard-----------------
    path('emplist',views.emp_list),
    path('empreq',views.manage),
    path('emp_proedit',views.emp_proedit),

    # path('emp_delete',views.emp_delete),

    # path('reject',views.reject),
    path('contact',views.contact),
    # path('acceptemp',views.empaccept),
    path('rejectemp',views.empreject),
    path('photographer', views.photographer),
    path('stillphoto_gallery',views.stillphoto_gallery),
    path('stillphoto_gallery',views.stillphoto_gallery),
    path('fashionphoto_gallery',views.fashionphoto_gallery),

    # path('inter1_gallery', views.inter1_gallery),
    # path('interior', views.interior),

    # path('artist', views.artist),
    # path('sclp_gallery',views.sclp_gallery),
    # path('portrait_gallery',views.portpaint_gallery),


    path('forget_pwd',views.forget_pwd),
    #path('emplist', views.list),
    path('portfolio',views.portfolio),
    path('profile5',views.profile5),
    path('empworks',views.works),
    path('index_work',views.index_work),
    path('location',views.locationfilter),
    path('m', views.autnew),
    path('accepting', views.phaccept),
    path('deleting', views.phreject),
    path('search',views.search),
    path('book_photo/<user>',views.book_photo),
    path('book',views.book),
    path('book_accept',views.book_accept),
    path('booking_list',views.booking_list),
    # path('final_pay/<l>',views.final_pay),
    path('user_inbox',views.user_inbox),
    path('book_confirm',views.book_confirm),
    path('newadmn_booking',views.bookkings),
    path('gallery/<user>',views.gallery),
    path('reviewlist',views.reviewlist),
    path('remove_review',views.remove_review),
    path('your_booking',views.your_booking),
    path('emp_addphoto',views.emp_addphoto),
    # path('emp_photo',views.emp_photo),
    path('emp_gallery',views.gallery_emp),
    # path('profile/', views.profile, name='profile'),
    path('update_user',views.update_user),
    path('user_edit',views.user_edit),
    path('payment',views.payment1),
    path('pay/<int:id>',views.pay),
    path('emp_forget_pwd1',views.forget_pwd1),
    path('paycancel',views.cancel),
    path('cancelled_booking',views.your_cancelledbooking),
    path('your_pendingbooking',views.your_pendingbooking),
    path('forgot',views.forgot_password,name="forgot"),
    path('reset/<token>',views.reset_password,name='reset_password'),
    path('employee_revieww/<user>',views.employeeee_review),
    path('success',views.success),
    path('emp_viewgaley',views.empview_galley),
    path('addpaymt',views.emp_addpayment),
    path('location',views.location),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)