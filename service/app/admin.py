from django.contrib import admin

# Register your models here.
from.models import log_in
admin.site.register(log_in)
from.models import employee_registration
admin.site.register(employee_registration)
from.models import user_registration
admin.site.register(user_registration)
from.models import payment
admin.site.register(payment)
from.models import feedback1
admin.site.register(feedback1)
from.models import common_feedback
admin.site.register(common_feedback)
from.models import Mesage
admin.site.register(Mesage)
from.models import booking
admin.site.register(booking)
from.models import emp_gallery
admin.site.register(emp_gallery)
from.models import PasswordReset
admin.site.register(PasswordReset)
from.models import amountdetails
admin.site.register(amountdetails)
