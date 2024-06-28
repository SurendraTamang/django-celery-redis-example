from django.contrib import admin
from invitation.models import SignUpModel

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    pass


admin.site.register(SignUpModel, SignupAdmin)