from django.forms import ModelForm
from app.models import Student
class myStudent(ModelForm):
	class Meta:
		model=Student
		fields='__all__'