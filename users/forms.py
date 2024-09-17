from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'username',
            'password1',
            'password2',
                  ]
        labels = {
            'first_name':'Name'
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Masukkan Judul'})
        # self.fields['demo_link'].widget.attrs.update({'class':'input', 'placeholder':'Masukkan demo_link'})
        # self.fields['source_link'].widget.attrs.update({'class':'input', 'placeholder':'Masukkan source_link'})

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class SkillForm(ModelForm):
    
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ["owner"]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
