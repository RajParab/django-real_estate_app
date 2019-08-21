from django import forms


class ContactForm(forms.Form):
	subject=forms.CharField(max_length=20)
	email=forms.EmailField(required=True)
	message=forms.CharField(widget=forms.Textarea, required=True)

	
