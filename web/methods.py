from django.conf import settings
from django.core.mail import send_mail

def sendmail(subject, message, mailid):
    try:
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [mailid, ]
        send_mail( subject, message, email_from, recipient_list )
    finally:
        return None
    
def setrecentHinglish(request,html,word):
    try: 
        recenth2 = request.COOKIES['recenth1']  
        recenth3 = request.COOKIES['recenth2']
        html.set_cookie("recenth3",recenth3)
        html.set_cookie("recenth2",recenth2)
        html.set_cookie("recenth1",word)
    except:
        html.set_cookie("recenth3",word)
        html.set_cookie("recenth2",word)
        html.set_cookie("recenth1",word)
    

def setrecentEnglish(request,html,word):
    try:
        recente2 = request.COOKIES['recente1']  
        recente3 = request.COOKIES['recente2']
        html.set_cookie("recente3",recente3)
        html.set_cookie("recente2",recente2)
        html.set_cookie("recente1",word)
    except:
        html.set_cookie("recente3",word)
        html.set_cookie("recente2",word)
        html.set_cookie("recente1",word)
    


def getrecentEnglish(request):
    recent = []
    try:
        recent.append(request.COOKIES['recente1']  )
        recent.append(request.COOKIES['recente2']  )
        recent.append(request.COOKIES['recente3']  )
    finally:
        return recent

def getrecentHinglish(request):
    recent = []
    try:
        recent.append(request.COOKIES['recenth1']  )
        recent.append(request.COOKIES['recenth2']  )
        recent.append(request.COOKIES['recenth3']  )
    finally:
        return recent