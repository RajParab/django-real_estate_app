from django import forms
from .models import Reserve


class ReserveForm(forms.ModelForm):
	class Meta:
		model = Reserve
		fields = "__all__"
		widgets = {
            'start_date': forms.DateInput(attrs={'class':'datepicker'}),
            'end_date': forms.DateInput(attrs={'class':'datepicker'}),

            }
