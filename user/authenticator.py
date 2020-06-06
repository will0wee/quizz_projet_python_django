from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class Authenticator():

    def authenticate(self,request,  username, password):
        user = User.objects.raw("SELECT id, username, password FROM auth_user WHERE username = '" + username + "'")
        try:
            if (check_password(password, user[0].password)):
                user = User.objects.filter(id=user[0].id)[0]
                if(user.is_active == 1):
                    request.session['userId'] = user.id
                    request.session['userLastLogin'] = user.last_login
                    request.session['userUsername'] = user.username
                    request.session['userFirstName'] = user.first_name
                    request.session['userLastName'] = user.last_name
                    request.session['userEmail'] = user.email
                    return True
                else:
                    return False
            return False
        except IndexError:
            return False
