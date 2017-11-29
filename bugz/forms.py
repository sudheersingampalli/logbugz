from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
	class Meta:
		model = Bug
		fields = ['employee_id','message']

class BugFormReason(forms.ModelForm):
	class Meta:
		model = Bug
		fields = ['record_stat','reason']
