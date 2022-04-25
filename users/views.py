import profile
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from users.forms import RegisterForm, LoginForm, ProfileForm, ProfileUpdateForm, RegisterUpdateForm
from users.models import Profile 
# import method decorator
# add login required mixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from django.utils.decorators import method_decorator
from django.views.generic import View, CreateView, FormView, UpdateView, DetailView, DeleteView, ListView


# Create your views here.

User = get_user_model()


def register(request):
    """

        register a new user with the given details
    Args:
        request (_type_): _description_
    """    
    # print('not in')
    if request.method == 'POST':
        # print('after post')
        form = RegisterForm(request.POST, request.FILES)
        # print(form)
        # print(request.FILES["profile_pic"])
        if form.is_valid():
            # print('after valid')
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            profile_pic = form.cleaned_data.get('profile_pic')
            # print(profile_pic, 99999)
            # email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {first_name} {last_name}!!!')
            return redirect('login')
    else:
        # print('new')
        form = RegisterForm()
        messages.error(request, 'Please fill the form correctly')
    return render(request, 'users/auth/register.html', {'form': form})



class UserLoginView(FormView):
    """
        login a user with the given details
    """
    template_name = 'users/auth/login.html'
    form_class = LoginForm
    success_url = '/'
    
    def form_valid(self, form):
        request = self.request
        next = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next or next_post or None
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {email}')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid email or Password')
            return redirect('login')
        
    # def form_valid(self, form):
    #     email = form.cleaned_data.get('email')
    #     password = form.cleaned_data.get('password')
    #     user = authenticate(self.request, username=email, password=password)
    #     if user is not None:
    #         login(self.request, user)
    #         return super().form_valid(form)
    #     else:
    #         messages.error(self.request, 'Invalid credentials')
    #         return super().form_invalid(form)


@login_required
def edit_profile(request):
    """
        view profile of the logged in user
    Args:
        request (_type_): _description_
    """
    # messages.success(request, f'You are now logged in as {request.user.email}')
    if request.method == 'POST':
        # print('post')
        u_form  = RegisterUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        profile = Profile.objects.get(user=request.user)
        # profile = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # print(u_form, p_form)
        if u_form.is_valid() and p_form.is_valid():
            # print('inner-post')
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('edit-profile')
    else: 
        u_form = RegisterUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        profile = Profile.objects.get(user=request.user)
        messages.info(request, 'Please fill the form correctly')
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile,
    }
    # print(messages)
    return render(request, 'users/profiles/editProfile.html', context)






def logout(request):
    """
        logout a user
    """
    return redirect('login')



# def edit_profile(request):
#     """
#         edit a user profile
#     """
#     return render(request, 'users/profile/editProfile.html')
#     # if request.method == 'POST':
#     #     form = ProfileForm(request.POST, request.FILES)
#     #     if form.is_valid():
#     #         form.save()
#     #         first_name = form.cleaned_data.get('first_name')
#     #         last_name = form.cleaned_data.get('last_name')
#     #         profile_pic = form.cleaned_data.get('profile_pic')
#     #         messages.success(request, f'Profile updated for {first_name} {last_name}!!!')
#     #         return redirect('edit-profile')
#     # else:
#     #     form = ProfileForm()
#     #     messages.error(request, 'Please fill the form correctly')
#     # return render(request, 'users/auth/edit_profile.html', {'form': form})



@method_decorator(login_required, name='dispatch')
class UserProfileView(LoginRequiredMixin, View):
    """
        check if user is authenticated or login
     

    Args:
        View (_type_): _description_
    """    
    profile = None 
    def dispatch(self, request, *args, **kwargs):
        """
            check if user is authenticated 
        """
        self.profile = get_object_or_404(Profile, user=request.user)
        print(self.profile, 'new me')
        if not request.user.is_authenticated:
            return redirect('login')
        return super(UserProfileView, self).dispatch(request, *args, **kwargs)
    

    def get(self, request):
        """
            get the user profile
        """
        # print('getter', request.user)
        context = {
            'profile': self.profile,
            'user': request.user


        }
        # print(self.profile.education)

        return render(request, 'users/profiles/userDashboard.html', context)
    
    def post(self, request):
        
        # print('settien')
        pass
    #     """
    #         update the user profile
    #     """
    #     form = ProfileForm(request.POST, request.FILES, instance=self.profile)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Profile updated successfully')
    #         return redirect('user-profile')
    #     else:
    #         messages.error(request, 'Please fill the form correctly')
    #         return redirect('edit-profile')