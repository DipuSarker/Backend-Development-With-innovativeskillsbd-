from user.models import User
from django.http import JsonResponse

def dup_check(request):
    email = request.GET.get('email')

    user_obj = User.objects.filter(email=email)

    if user_obj.exists():
        return JsonResponse({"message": "Already exist", "status": 400})

    return JsonResponse({"message": "OK", "status": 200}) 