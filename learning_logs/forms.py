# starting ch 19 - 9/23/2019 
from django import forms 

from .models import Topic, Entry 

class TopicForm(forms.ModelForm): 
	class Meta: 
		model = Topic 
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm): 
	class Meta: 
		model = Entry  
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs = {'cols': 80})}