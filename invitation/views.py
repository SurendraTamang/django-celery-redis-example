from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from invitation.forms import SignUpForm
# Create your views here.
class SignUpView(FormView):
    template_name ="invitation/signup.html"
    form_class = SignUpForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form=form)
    

class SuccessView(TemplateView):
    template_name = "invitation/success.html"