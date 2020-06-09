from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .models import User_data, User_type
import logging

class Authenticator():
    def authenticate(self, request,  username, password):
        user = User.objects.raw("SELECT id, username, password FROM auth_user WHERE username = '" + username + "'")
        try:
            if (check_password(password, user[0].password)):
                user = User.objects.filter(id=user[0].id)[0]
                userData = User_data.objects.filter(user=user.id)[0]
                userType = User_type.objects.filter(id=userData.user_type.id)[0]
                if(user.is_active == 1):
                    request.session['userId'] = user.id
                    request.session['userUsername'] = user.username
                    request.session['userFirstName'] = user.first_name
                    request.session['userLastName'] = user.last_name
                    request.session['userEmail'] = user.email
                    request.session['userType'] = userData.user_type.id
                    request.session['userTypeLibelle'] = userType.libelle
                    return True
                else:
                    return False
            return False
        except IndexError:
            return False
