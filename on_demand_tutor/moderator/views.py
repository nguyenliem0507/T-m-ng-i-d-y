from django.shortcuts import render
from django.http import HttpResponse
from .forms import ModeratorRegisterForm  # Tạo form đăng ký

class ModeratorLoginView(View):
    def get(self, request):
        return render(request, 'moderator/auth.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.Role == 'moderator':
            login(request, user)
            return redirect('moderator_dashboard')  # Chuyển đến dashboard của Moderator
        else:
            return render(request, 'moderator/auth.html', {'error_message': 'Invalid credentials or not a moderator'})

class ModeratorRegisterView(View):
    def get(self, request):
        return render(request, 'moderator/auth.html')

    def post(self, request):
        form = ModeratorRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.Role = 'moderator'  # Gán vai trò moderator
            user.save()
            return redirect('moderator_login')
        return render(request, 'moderator/auth.html', {'form': form})
