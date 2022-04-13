from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Profile



User = get_user_model()



class UserAdminCreationForm(forms.ModelForm):
    """
        A form for creating new users. Includes all the required
        fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """
        A form for updating users. Includes all the fields on
        the user, but replaces the password field with admin's
        password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class RegisterForm(forms.ModelForm):
    """
        A form for creating new users. Includes all the required
        fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    profile_pic = forms.ImageField(label="choose your profile picture", required=False)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',  'password1', 'password2', 'profile_pic')

    def __init__(self, *args, **kwargs):
        """
            overwriting the user registration form to add custom fields 
        """        
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
                                'class': 'form-control form-control-user',
                                'placeholder': 'Enter Email Address...',
                                'aria-label': 'Email Address',
                                'id':'email',
                                'name':'email',
                                'type':'email',
                                'required':'required',
                                'autofocus':'autofocus',
                                'autocomplete':'off'

                                })
        self.fields['first_name'].widget.attrs.update({
                                'class': 'form-control form-control-user',
                                'placeholder': 'Enter First Name...',
                                'aria-label': 'First Name',
                                'id':'first_name',
                                'name':'first_name',
                                'type':'text',
                                'required':'required',
                                'autofocus':'autofocus',
                                'autocomplete':'off'

                                })
        self.fields['last_name'].widget.attrs.update({
                                'class': 'form-control form-control-user',
                                'placeholder': 'Enter Last Name...',
                                'aria-label': 'Last Name',
                                'id':'last_name',
                                'name':'last_name',
                                'type':'text',
                                'required':'required',
                                'autofocus':'autofocus',
                                'autocomplete':'off'

                                })
        self.fields['password1'].widget.attrs.update({
                                'class': 'form-control form-control-user',
                                'placeholder': 'Enter Password...',
                                'aria-label': 'Password',
                                'id':'password1',
                                'name':'password1',
                                'type':'password',
                                'required':'required',
                                'autofocus':'autofocus',
                                'autocomplete':'off'

                                })
        self.fields['password2'].widget.attrs.update({
                                'class': 'form-control form-control-user',
                                'placeholder': 'Confirm Password...',
                                'aria-label': 'Password',
                                'id':'password2',
                                'name':'password2',
                                'type':'password',
                                'required':'required',
                                'autofocus':'autofocus',
                                'autocomplete':'off'

                                })
        # self.fields['profile_pic'].widget.attrs.update({
        #                         'class': 'form-control form-control-user',
        #                         'placeholder': 'Enter Profile Picture...',
        #                         'aria-label': 'Profile Picture',
        #                         'id':'profile_pic',
        #                         'name':'profile_pic',
        #                         'type':'file',
        #                         'required':'required',
        #                         'autofocus':'autofocus',
        #                         'autocomplete':'off'

        #                         })


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """
        A form for creating new users. Includes all the required
        fields, plus a repeated password.
    """
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        """
            overwriting the user registration form to add custom fields 
        """        
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
                                'class': 'login__input',
                                'placeholder': 'Email',
                                # 'aria-label': 'Email Address',
                                'id':'email',
                                'name':'email',
                                'type':'email',
                                'required':'required',
                                # 'autofocus':'autofocus',
                                'autocomplete':'off'

                                })
        self.fields['password'].widget.attrs.update({
                                'class': 'login__input',
                                'placeholder': 'Enter Password...',
                                'aria-label': 'Password',
                                'id':'password',
                                'name':'password',
                                'type':'password',
                                'required':'required',
                                'autofocus':'autofocus',
                                'autocomplete':'off'

                                })


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        # get all fields 
        # fields = '__all__'
        exclude = ['user']

    # def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['age'] = forms.IntegerField(label='Age', widget=forms.NumberInput)
    #     self.fields['education'] = forms.CharField(label='Education', widget=forms.TextInput)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        # get all fields 
        # fields = '__all__'
        exclude = ['user']

    # def __init__(self, *args, **kwargs):
    #     super(ProfileUpdateForm, self).__init__(*args, **kwargs)
    #     self.fields['age'] = forms.IntegerField(label='Age', widget=forms.NumberInput)
    #     self.fields['education'] = forms.CharField(label='Education', widget=forms.TextInput)
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['age'].widget.attrs.update({
                                'class': 'form-control',
                                'placeholder': 'enter Age...',
                                'style':'border: none; width: 13rem; height: 1.3rem; margin-top: 13px;',

        })
        self.fields['education'].widget.attrs.update({
                                'class': 'form-control',
                                'placeholder': 'enter Education...',
                                'style':'border: none; width: 13rem; height: 1.3rem; margin-top: 13px;',

        })
        self.fields['country'].widget.attrs.update({
                                'class': 'form-control',
                                'placeholder': 'enter Country...',
                                'style':'border: none; width: 13rem; height: 1.3rem; margin-top: 13px;',

        })
        self.fields['title'].widget.attrs.update({
                                'class': 'form-control',
                                'placeholder': 'enter Title...',
                                'style':'border: none; width: 13rem; height: 1.3rem; margin-top: 13px;',

        })
        self.fields['year'].widget.attrs.update({
                                'class': 'form-control',
                                'placeholder': '1999 - 2024',
                                'style':'border: none; width: 13rem; height: 1.3rem; margin-top: 13px;',

        })
        self.fields['professional_summary'].widget.attrs.update({
                                'class': 'form-control',
                                'placeholder': 'about profession',
                                'style':'height: 99px;',

        })
        self.fields['city'].widget.attrs.update({
                                'class': 'form-control',
                                'placeholder': 'enter City...',
                                'style':'border: none; width: 13rem; height: 1.3rem; margin-top: 13px;',

        })






class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super(RegisterUpdateForm, self).__init__(*args, **kwargs)
        # self.fields['email'].widget.attrs.update({
        #                         'class': 'form-control',
        #                         # 'placeholder': 'Enter Email...',
        #                         # 'aria-label': 'Email',
        #                         # 'id':'email',
        #                         # 'name':'email',
        #                         # 'type':'email',
        #                         # 'required':'required',
        #                         # 'autofocus':'autofocus',
        #                         # 'autocomplete':'off'

        #                         })
        self.fields['first_name'].widget.attrs.update({
                                'class': 'form-control',
                                'style':'border: none; width: 13rem; height: 1.3rem; margin-top: 13px;',
                                # 'placeholder': 'Enter First Name...',
                                # 'aria-label': 'First Name',
                                # 'id':'first_name',
                                # 'name':'first_name',
                                # 'type':'text',
                                # 'required':'required',
                                # 'autofocus':'autofocus',
                                # 'autocomplete':'off'

                                })
        self.fields['last_name'].widget.attrs.update({
                                'class': 'form-control',
                                'style':'border: none; width: 13rem; height: 1.3rem; margin-top: 13px;',
                                # 'placeholder': 'Enter Last Name...',
                                # 'aria-label': 'Last Name',
                                # 'id':'last_name',
                                # 'name':'last_name',
                                # 'type':'text',
                                # 'required':'required',
                                # 'autofocus':'autofocus',
                                # 'autocomplete':'off'

                                })
        self.fields['profile_pic'].widget.attrs.update({
                                'class': 'form-control',
                                'placeholder': 'Enter Profile Picture...',
                                'aria-label': 'Profile Picture',
                                'id':'profile_pic',
                                'name':'profile_pic',
                                'type':'file',
                                'required':'required',
                                'autofocus':'autofocus',
                                'autocomplete':'off'

                                })
    # def __init__(self, *args, **kwargs):
    #     """
    #         overwriting the user registration form to add custom fields 
    #     """        
    #     super(RegisterUpdateForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs.update({
    #                             'class': 'form-control form-control-user',
    #                             'placeholder': 'Enter Email Address...',
    #                             'aria-label': 'Email Address',
    #                             'id':'email',
    #                             'name':'email',
    #                             'type':'email',
    #                             'required':'required',
    #                             'autofocus':'autofocus',
    #                             'autocomplete':'off'

    #                             })
    #     self.fields['first_name'].widget.attrs.update({
    #                             'class': 'form-control form-control-user',
    #                             'placeholder': 'Enter First Name...',
    #                             'aria-label': 'First Name',
    #                             'id':'first_name',
    #                             'name':'first_name',
    #                             'type':'text',
    #                             'required':'required',
    #                             'autofocus':'autofocus',
    #                             'autocomplete':'off'

    #                             })
    #     self.fields['last_name'].widget.attrs.update({
    #                             'class': 'form-control form-control-user',
    #                             'placeholder': 'Enter Last Name...',
    #                             'aria-label': 'Last Name',
    #                             'id':'last_name',
    #                             'name':'last_name',
    #                             'type':'text',
    #                             'required':'required',
    #                             'autofocus':'autofocus',
    #                             'autocomplete':'off'

    #                             })









# class UserAdmin(admin.ModelAdmin):
#     """
#         The admin page for the User model
#     """
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     list_display = ('email', 'first_name', 'last_name', 'admin', 'staff', 'active')
#     list_filter = ('admin', 'staff', 'active')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'profile_pic')}),
#         ('Permissions', {'fields': ('admin', 'staff', 'active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()