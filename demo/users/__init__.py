from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username == 'rajesh' and password == 'kaushik':
        return True
    else:
        return False
