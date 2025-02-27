from invitation.models import SignUpModel
from django import forms
from invitation.task import send_email_task
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = "__all__"


    def send_email(self):
        details = {
            "full_name":self.cleaned_data['full_name'],
            "email":self.cleaned_data['email'],
            "phone_number":self.cleaned_data['phone_number'],
            "full_address":self.cleaned_data['full_address']
        }
        send_email_task.delay(details) # delay sends it to queue

        