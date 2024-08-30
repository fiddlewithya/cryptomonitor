from .models import UserProfile

def user_profile(request):
    if UserProfile.objects.exists():
        profile = UserProfile.objects.first()
    else:
        profile = None
    return {'profile': profile}
