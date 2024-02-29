from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from django.core.validators import MinValueValidator
from .models import *

class Leader_lookup_all(forms.Form):
      stat_types = []
      distinct_group_names = stat_type_table.objects.exclude(group_name__in=['game','catching','fielding']).values_list('group_name', flat=True).distinct()
      for name in distinct_group_names:
        type_name = (name,name)
        stat_types.append(type_name)
    
      
      category = forms.ChoiceField(required=False,choices=stat_types,label='',widget=forms.Select(attrs={'class': 'btn dropdown-toggle', 'style': 'background-color: white; width:170px;text-align: center;'}))
      stat =forms.ChoiceField(required=False,choices=[], label='',widget=forms.Select(attrs={'class': 'btn dropdown-toggle', 'style': 'background-color: white; width:170px;text-align: center;'}))

class Leader_lookup_hitting(forms.Form):
   
      hitting_stats = []
      distinct_stat_names_hitting = stat_type_table.objects.exclude(group_name__in=['game', 'pitching', 'catching','fielding']).values_list('display_name','lookup_name','group_name').distinct()
      for name in distinct_stat_names_hitting:
        # print(name)
        setname = (name[0],name[1])
        hitting_stats.append(setname)

      # category = forms.ChoiceField(required=False,choices=stat_types,label='',widget=forms.Select(attrs={'class': 'btn dropdown-toggle', 'style': 'background-color: white; width:170px;text-align: center;'}))
      stat =forms.ChoiceField(required=False,choices=hitting_stats, label='',widget=forms.Select(attrs={'class': 'btn dropdown-toggle', 'style': 'background-color: white; width:260px;text-align: center;'}))
      # stat =forms.ChoiceField(required=False,choices=stats, label='',widget=forms.Select(attrs={'class': 'btn dropdown-toggle', 'style': 'background-color: white; width:170px;text-align: center;'}))

class Leader_lookup_hiting(forms.Form):

      stats = []
      distinct_stat_names = stat_type_table.objects.exclude(group_name__in=['game', 'pitching', 'catching','fielding']).values_list('display_name','lookup_name','group_name').distinct()
      for name in distinct_stat_names:
        # print(name)
        setname = (name[0],name[1])
        stats.append(setname)

class Leader_lookup_pitching(forms.Form):

      stats = []
      distinct_stat_names = stat_type_table.objects.exclude(group_name__in=['game', 'hitting', 'catching','fielding']).values_list('display_name','lookup_name','group_name').distinct()
      for name in distinct_stat_names:
       
        setname = (name[0],name[1])
        # print(setname)
        stats.append(setname)
  
      stat =forms.ChoiceField(required=False,choices=stats, label='',widget=forms.Select(attrs={'class': 'btn dropdown-toggle', 'style': 'background-color: white; width:255px;text-align: center;'}))
class MyForm(forms.Form):
    CATEGORY_CHOICES = [
        ('hitting', 'Hitting'),
        ('pitching', 'Pitching'),
    ]
    
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    stat_options = forms.ChoiceField()
