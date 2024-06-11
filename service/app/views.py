from django.shortcuts import render, redirect
import razorpay
from django.http import HttpResponse
from.models import *
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib import messages



# Create your views here.
# ------------commented-------------------

# def login(re):
#     return render(re,'login.html')

def accept(request):     #accepting pro
    if request.method == "POST":
        r = request.POST['n1']
        d = employee_registration.objects.filter(username=r)
        d.update(action="Confirm")
        # return HttpResponse("Accepted")
        return HttpResponse("<script>alert('Accepted') </script>")
    else:
        return render(request, 'emplist.html')


# def reject(request):
#
#     if request.method == 'POST':
#         a = request.POST['n1']
#         b = request.POST['action']
#         print(b)
#         if b == 'reject':
#             d = employee_registration.objects.filter(name=a)
#             d.delete()
#             return render(request, 'newadmn.html')
#         elif b == 'accept':
#             d = employee_registration.objects.filter(name=a)
#             d.update(action='confirm',status=2)
#
#             return render(request, 'newadmn.html')

# def login1(request):
#     if request.method == 'POST':
#         x = request.POST['n1']
#         y = request.POST['n2']
#         z = 'incorrect password'
#         w = 'user not found'
#         try:
#             d = log_in.objects.get(username=x)
#             if d.password == y:
#                 request.session['id'] = x
#                 if d.status == '1':
#                     return redirect(profile)
#                 elif d.status == '2':
#                     return redirect(profile)
#                 else:
#                     return redirect(profile)
#             else:
#                 return render(request, 'login.html',{'r':z})
#         except Exception:
#             return render(request, 'login.html', {'r': w})
#     else:
#         return render(request,'login.html')

# def list(request):
#      d1 =employee_registration.objects.all()
#      return render(request,'emplist.html',{'r':d1})

# def reject(request):
#     if request.method == 'POST':
#         a = request.POST['n1']
#         b = request.POST['action']
#         print(b)
#         if b == 'reject':
#             d = employee_registration.objects.filter(username=a)
#             d.delete()
#             return render(request, 'emp_req.html')
#         elif b == 'accept':
#             d = employee_registration.objects.filter(username=a)
#             d.update(action='confirm',status='1')
#             d1 = employee_registration.objects.all()
#
#             return render(request, 'emp_req.html',{'r':d})
#     else:
#         return HttpResponse("error")

# def emp_delete(re):
#     if re.method=='POST':
#         x=re.POST['n1']
#         data=employee_registration.objects.filter(username=x)
#         data.delete()
#         return render(re,'emplist.html')
#     else:
#         return render(re,'emplist.html')


# def feedback(re):
#     return render(re,'feedback.html')





#--------------template html file---------------------
def about(re):
    return render(re, 'about.html')
def contact(re):
    return render(re, 'contact.html')
def jobs(re):
    return render(re, 'jobs.html')

def property(re):
    return render(re, 'property-details.html')
def terms(re):
    return render(re, 'terms.html')

#-----------first index------------------
def index(re):
    return render(re, 'index.html')
#------------user index------------------
def user_index(re):
    return render(re, 'index1.html')

#-----------photographer profile & gallery--------------
def photographer(re):
    d= employee_registration.objects.filter(action="Confirm")
    return render(re, 'Photographers.html',{'r':d})
def stillphoto_gallery(re):
    return render(re,'stillPhoto_gallery.html')
def fashionphoto_gallery(re):
    return render(re, 'fashionphoto_gallery.html')

#---------emp& user registration forgot pwd, etc
def EM(re):
    if re.method=='POST':
        a = re.POST['NAME']
        b = re.POST['EMAIL']
        c = re.POST['PHONE']
        d = re.POST['GENDER']
        e= re.POST['PHOTO']
        f= re.POST['LICENSE']
        g = re.POST['LOCATION']
        j = re.POST['USERNAME']
        o=re.POST['PASSWORD']
        d1=employee_registration.objects.filter(username=j)
        d2=employee_registration.objects.filter(email=b)
        if list(d1) == []:
            if list(d2) == []:
                x = employee_registration.objects.create(name=a,photo=e, license=f, email=b ,phone_no=c,gender=d,location=g, username=j,status=1,action='pending')
                x.save()
                y = log_in.objects.create(username=j, password=o, status=1)
                y.save()
            else:
                return HttpResponse("<script>alert('email already exists');window.location='EM '</script>")
        else:
            return HttpResponse("<script>alert('username already exists');window.location='EM'</script>")

        return HttpResponse("<script>alert('Registered Successfully');window.location='login'</script>")
    else:
        return render(re, "EM_reg1.html")

def emp_addpayment(re):
    if re.method == 'POST':
        m = re.POST['advance_amount']
        n = re.POST['full_amount']
        z = re.session['e_id']
        d=amountdetails.objects.filter(username=z)
        print(d)
        if list(d)==[]:
            print(d)
            x = amountdetails.objects.create(username=z, fullamount=n,advAmound=m)
            x.save()
            return render(re, 'addpaymt.html')
        else:
            d.update(fullamount=n, advAmound=m)
            return render(re, 'addpaymt.html')
    else:
        return render(re, 'addpaymt.html')

# def emp_addpayment(re):
#     # if re.method=='POST':
#     #     a = re.POST['USERNAME']
#     #     m = re.POST['AMOUNT1']
#     #     n = re.POST['AMOUNT2']
#     #     p = amountdetails.objects.create(fullamount=m, advAmound=n, username=j)
#     #     p.save()
#     #     return render(re,'addpaymnt.html')
#     if 'e_id' in re.session:
#         z = re.session['e_id']
#         if re.method=='POST':
#             m = re.POST['advance_amount']
#             n = re.POST['full_amount']
#             x = amountdetails.objects.create(fullamount=m, advAmound=n, username=z)
#             x.save()
#     return render(re, 'addpaymt.html')


def user_reg(re):
    if re.method == 'POST':
        a = re.POST['NAME']
        b = re.POST['EMAIL']
        c = re.POST['PHONE']
        d = re.POST['LOCATION']
        e = re.POST['USERNAME']
        f = re.POST['PASSWORD']
        d1=user_registration.objects.filter(username=e)
        d2 = user_registration.objects.filter(email=b)
        if list(d1) == []:
            if list(d2) == []:
                x = user_registration.objects.create(name=a, email=b, location=d, phone_no=c, username=e)
                x.save()
                y = log_in.objects.create(username=e, password=f, status=2)
                y.save()
            else:
                return HttpResponse("<script>alert('email already exists');window.location='user_reg'</script>")
        else:
            return HttpResponse("<script>alert('username already exists');window.location='user_reg'</script>")

        return HttpResponse("<script>alert('Registered Successfully');window.location='login'</script>")
    else:
        return render(re, "user_registration.html")

def forget_pwd1(re):
    if 'e_id' in re.session:
        y=re.session['e_id']
        d=employee_registration.objects.filter(username=y)
        if re.method == 'POST':
            # u=re.POST['uname']
            p = re.POST['pwd']
            c = re.POST['con_pwd']
            try:
                b = log_in.objects.filter(username=y)
                if p == c:
                    b.update(password=c)
                    return render(re,'login.html')
                else:
                    # return HttpResponse("<script>alert('Password is not matching');windows.location='profile3' </script>")
                    return render(re, 'emp_change_pwd.html', {'message1': 'Password is not matching'})
            except Exception:
                # return HttpResponse( "<script>alert('please write another password');windows.location='profile3' </script>")
                return render(re, 'emp_change_pwd.html', {'message2': 'please write another password'})
        else:
            return render(re, 'emp_change_pwd.html')
def forget_pwd(re):
    if 'u_id' in re.session:
        y=re.session['u_id']
        d=user_registration.objects.filter(username=y)
        if re.method=='POST':
            # u=re.POST['uname']
            p=re.POST['pwd']
            c=re.POST['con_pwd']
            try:
                b = log_in.objects.filter(username=y)
                if p==c:
                    b.update(password=c)
                    return render(re,'login.html')
                else:
                    return HttpResponse("<script>alert('Password is incorrect');windows.location='index1' </script>")
            except Exception:
                return HttpResponse("<script>alert('please write another password');windows.location='index1' </script>")
        else:
            return render(re,'forget_pwd.html')  #forget password
    # else:
    #     return render(re, 'forget_pwd.html')


def chng_pwd(re):
    if re.method=='POST':
        u=re.POST['uname']
        o=re.POST['old_pwd']
        p=re.POST['pwd']
        c=re.POST['con_pwd']
        try:
            b = log_in.objects.filter(username=u)
            if o!=p & p==c:
                b.update(password=c)
                return render(re,'login.html')
        except Exception:
            return HttpResponse('please write another password')
    else:
        return render(re,'forget_pwd.html')  #forget password


def profile1(re):
    if 'a_id' in re.session:
        return render(re,'newadmin.html')
    else:
        return render(re,'login.html')
def profile2(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=user_registration.objects.filter(username=y)
        return render(re,'index1.html',{'r':d})
    else:
        return render(re,'login.html')
def profile3(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=employee_registration.objects.filter(username=z)
        g=amountdetails.objects.filter(username=z)
        return render(re,'emp_proview.html',{'r':d,'r1':g})
    else:
        return HttpResponse("<script>alert('your registration is not yet completed');windows.location='login' </script>")


def profile5(re):
    if 'u_id' in re.session:
        z=re.session['u_id']
        d=user_registration.objects.filter(username=z)
        return render(re,'portfolio.html',{'r':d})
    else:
        return render(re,'login.html')



def login(re):
    if re.method=='POST':
        u=re.POST['n1']
        p=re.POST['n2']
        try:
            d=log_in.objects.get(username=u)
            if d.password==p:
                if d.status=='0':
                    re.session['a_id']=u
                    return redirect(profile1)
                elif d.status == '1':
                    f= employee_registration.objects.get(username=u)
                    if f.action == 'Confirm':
                        re.session['e_id']=u
                        return redirect(profile3)
                    else:
                        return render(re, 'login.html', {'message1': 'login failed,request is processing...'})
                elif d.status == '2':
                    re.session['u_id']=u
                    return redirect(profile2)
            else:
                return render(re, 'login.html', {'message1': ' Incorrect password'})
        except Exception:
            return render(re, 'login.html', {'message2': ' Incorrect username '})
    else:
        return render(re,'login.html')
    # if request.method == "POST":
    #     e = request.POST['n1']
    #     f = request.POST['n2']
    #     try:
    #         data = log_in.objects.get(username=e)
    #         if data.action == 'pending':
    #             return HttpResponse("requesting process")
    #         else:
    #             if data.status == 2:
    #                 if data.password == f:
    #                     request.session['u_id']=e
    #                     return redirect(profile2)
    #                 else:
    #                     return HttpResponse("<script>alert('Invalid Password');window.location='b'</script>")
    #             elif data.rights == 0:
    #                 if data.password == f:
    #                     request.session['a_id']=e
    #                     return redirect(profile1)
    #                 else:
    #                     return HttpResponse("<script>alert('Incorrect username/password');window.location='b'</script>")
    #             elif data.rights == 1:
    #                 if data.password == f:
    #                     request.session['e_id']=e
    #                     return redirect(profile3)
    #                 else:
    #                     return HttpResponse("<script>alert('Incorrect username/password');window.location='login''</script>")
    #     except Exception:
    #         return HttpResponse("<script>alert('Incorrect username/');window.location='login'</script>")
    # else:
    #     return render(request,'login.html')

#--------------employee page--------------------------
def emp_list(request):
    d= employee_registration.objects.filter(action='Confirm')
    return render(request,'newadmtables.html',{'r':d})
def userlist(re):
    d=user_registration.objects.all()
    return render(re,"newadm_userlist.html",{'r':d})


def manage(re):
    d = employee_registration.objects.filter(action='pending')
    return render(re,'emp_req.html',{'r':d})


def ad_request(request):
    datas=employee_registration.objects.all()
    return render(request,'newadmtables.html',{'r':datas})
def accept_request(request,d):
    employee_registration.objects.filter(pk=d).update(action='successfull')
    return redirect(ad_request)

def empaccept(request):     #accepting pro
    if request.method == "POST":
        r = request.POST['n1']
        d =employee_registration.objects.filter(username=r)
        d.update(action="Confirm")
        # d1=login.objects.filter(id=r)
        # d1.update(action="Confirm")
        return HttpResponse("<script>alert('ACCEPTED');windows.location='emp_req' </script>")

def empreject(request):# deleting pro request
    if request.method == "POST":
        r = request.POST['n1']
        d = employee_registration.objects.filter(username=r)
        d.delete()
        d1 =employee_registration.objects.filter(username=r)
        d1.delete()
        return HttpResponse("Rejected")
    else:
        return redirect(manage)


def remove(re):
    if re.method=='POST':
        z=re.POST['uname']
        d=employee_registration.objects.filter(username=z)
        x=log_in.objects.filter(username=z)
        x.delete()
        d.delete()
        return redirect(emp_list)
    else:
        return render(re,'newadmin_table.html')

def remove1(re):
    if re.method == 'POST':
        z = re.POST['uname']
        d = user_registration.objects.filter(username=z)
        x = log_in.objects.filter(username=z)
        x.delete()
        d.delete()
        return redirect(userlist)
    else:
        return render(re, 'newadmin_userlist.html')
def new_admin(re):
    return render(re,'newadmin.html')
def newadmin_table(re):
    d=employee_registration.objects.filter(action='Confirm')
    return render(re,'newadmtables.html',{'r':d})


#-------user profile------------
def emp_profile(re):
    if 'u_id' in re.session:
        u=re.session['u_id']
        d =employee_registration.objects.get(username=u)
        return render(re,'emp_profile.html',{'r':d})
    else:
        return render(re,'emp_profile.html')

def logout(re):
    if 'a_id' in re.session:
        re.session.flush()
        return render(re,'index.html')
    elif 'e_id' in re.session:
        re.session.flush()
        return render(re,'index.html')
    elif 'u_id' in re.session:
        re.session.flush()
        return render(re,'index.html')
    else:
        return render(re, 'index.html')

#-----------old admin-----------------
def admn(re):
    return render(re,'admn.html')
  #------------new admin------------------
def adm_index(re):
    return render(re,'admin_index.html')
def adm_form(re):
    return render(re,'adm_form.html')
def adm_table(re):
    return render(re,'adm_table.html')
def message_admin(re):
    if 'e_id' in re.session:
        x=re.session['e_id']
        d=Mesage.objects.filter(employee_name=x)
        return render(re,'message.html',{'r':d})
    else:
        return HttpResponse('error')
def newadm_message(re):
    if re.method=='POST':
        a=re.POST['n2']
        b=re.POST['n3']
        c=re.POST['n4']
        x=Mesage.objects.create(employee_name=a,email=b,messages=c)
        # return redirect(messages)
        return HttpResponse("<script> alert ('Message send') ; window.location='newadm_msg' </script>")
    else:
        return render(re,'newadm_message.html')

#------------payment--------------
# def payment1(request):
#     if request.method == 'POST':
#             x = request.POST['b1']
#             y = request.POST['b2']
#             z = request.POST['b3']
#             a = request.POST['b4']
#             request.session['p_name'] = a
#             request.session['l_name'] = y
#             d = booking.objects.filter(username=x,patient_name=a,name=y,status='confirm')
#             if list(d) ==[]:
#                 url='viewapp'
#                 msg='''<script>alert('payment not allowed.. your in processing')
#                 window.location='%s'</script>'''%(url)
#                 return HttpResponse(msg)
#             else:
#                 data= service.objects.filter(test=z,name=y)
#                 for i in data:
#                     k=i.amount
#                 return render(request,'payment.html',{'r':d,'r1':k})
#     else:
#         return render(request, 'payment.html')

def feedlist(re):
    d=feedback1.objects.all()
    return render(re,'newadmin_feedback.html',{'r':d})

def feedcreate(re):
    if 'u_id' in re.session:
        y = re.session['u_id']
        g= user_registration.objects.filter(username=y)
        if re.method=='POST':
            a = re.POST['n1']
            b = re.POST['n2']
            c = re.POST['n3']
            d = re.POST['n4']
            x = feedback1.objects.create(username=y, email=b,employee_name=c,review=d)
            y=employee_registration.objects.filter(username=a)
            return HttpResponse("<script>alert('Thanks for the review.');window.location='feed'</script>")
        return render(re, 'feedback.html', { 'r1': g})
        # else:
        #     return render(re, "feedback.html")

def common_feed(re):
    if re.method == 'POST':
        a = re.POST['n1']
        b = re.POST['n2']
        d = re.POST['n4']
        x = common_feedback.objects.create(username=a, email=b, feedback=d)
        x.save()
        return render(re,'COMMON_FEED.html')
    else:
        return render(re,'COMMON_FEED.html')

def common_feedlist(re):
    x = common_feedback.objects.all()
    return render(re,'newadmin_commonfeedback.html',{'r':x})

#-----------------------employee page -----------------------------------
def emp_index(re):
    return render(re,'emp_index.html')

# def emp_viewww(re):
#     x=re.POST['n1']
#     d=employee_registration.objects.filter(username=x)
#     return render(re,'emp_proview.html',{'r':d})
def emp_view(re):
    if re.method=='POST':
        return redirect(profile3)
    else:
        return HttpResponse('employee')
def emp_feed(re):
    d=feedback1.objects.all()
    return render(re,'emp_feedback.html',{'r':d})
def emp_profeed(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=feedback1.objects.filter(employee_name=z)
        return render(re,'emp_profeed.html',{'r':d})
    else:
        return render(re,'login.html')
def profile4(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=employee_registration.objects.filter(username=z)
        return render(re,'emp_proedit.html',{'r':d})
    return redirect(emp_proedit)
def emp_proedit(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=employee_registration.objects.filter(username=z)
        a=re.POST['name']
        b=re.POST['phone_no']
        c = re.POST['location']
        d = re.POST['email']
        # f = re.POST['skill']
        # g=re.FILES['work1']
        # h=re.FILES['work2']
        # i=re.FILES['photo']
        y=employee_registration.objects.filter(username=z)
        x=y.update(name=a,phone_no=b,location=c,email=d)
        return redirect(profile4)
    else:
        return HttpResponse('not okay')

def user_edit(re):
    if 'u_id' in re.session:
        z=re.session['u_id']
        d=user_registration.objects.filter(username=z)
        return render(re,'update_userpro.html',{'r':d})
    return redirect(update_user)

def update_user(re):
    if 'u_id' in re.session:
        z = re.session['u_id']
        s1 = user_registration.objects.filter(username=z)
        a = re.POST['n1']
        b = re.POST['n2']
        c = re.POST['n3']
        d = re.POST['n5']
        f = re.POST['n4']
        y=user_registration.objects.filter(username=z)
        x=y.update(name=a,phone_no=b,email=c,location=f)
        return HttpResponse("<script> alert ('Details updated') ; window.location='profile5' </script>")
    else:
        return HttpResponse("NOT UPDATED")

def portfolio(re):
    return render(re,'portfolio.html')

def works(re):
    return render(re,'emp_work3.html')

def index_work(re):
    return render(re,'index_work.html')

def phaccept(request):     #accepting author
    if request.method == "POST":
        r = request.POST['n1']
        d = employee_registration.objects.filter(id=r)
        print(d)
        d.update(action="Confirm")
        return HttpResponse("<script>alert('Accepted');window.location='newadmin_table'</script>")
    else:
        return render(request, 'emp_req.html')

def autnew(request):    #author request
    if request.method == "GET":
        data = employee_registration.objects.all()
        return render(request, 'emp_req.html', {'r': data})
    else:
        return render(request, 'emp_req.html')

def phreject(request):      # rejecting book
    if request.method == "POST":
        r = request.POST['n1']
        d = employee_registration.objects.filter(id=r)
        d.delete()
        return HttpResponse("<script>alert('Rejected');window.location='newadmin_table'</script>")
    else:
        return render(request, 'emplist.html')

def job_details(re,user):
    d = employee_registration.objects.filter(username=user)
    x=amountdetails.objects.filter(username=user)
    return render(re,'job-details.html',{'r':d,'r1':x})

def gallery(re,user):
    g = emp_gallery.objects.filter(username=user)
    return render(re, 'gallery.html',{'r': g})

def book_photo(re,user):
    if 'u_id' in re.session:
        y = re.session['u_id']
        g= user_registration.objects.filter(username=y)
        d = employee_registration.objects.filter(username=user)
        if re.method=='POST':
            a = re.POST['NAME']
            b = re.POST['PHONE']
            c = re.POST['ADDRESS']
            d = re.POST['EMAIL']
            f = re.POST['DATE']
            s3=re.POST['DAY']
            # g=re.POST['PHOTO']
            x=booking.objects.create(username=y,day=s3,name=a,phone_no=b,address=c,email=d,date=f,action='pending',employee_name=user, payment='pending')
            return HttpResponse("<script>alert('booking is processing.confirmation will be updated');window.location='../index1'</script>")
        return render(re,'book_photo.html',{'r':d,'r1':g})
    # else:
    #     return render(re, 'book_photo.html')



def book(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        d=booking.objects.filter(employee_name=z,action='pending')
        return render(re,'book_req.html',{'r':d})
    else:
        return render(re, 'book_req.html')
def book_accept(re):
    if re.method == "POST":
        if 'e_id' in re.session:
            r = re.POST['n1']
            d = booking.objects.filter(id=r)
            print(d)
            d.update(action="Confirm")
            return HttpResponse("<script>alert('Accepted');window.location='book'</script>")
        else:
            return render(re, 'emp_req.html')
    else:
        return render(re, 'emp_req.html')

def book_reject(request):      # rejecting book
    if request.method == "POST":
        r = request.POST['n1']
        d = employee_registration.objects.filter(id=r)
        d.delete()
        return HttpResponse("<script>alert('Rejected');window.location='booking_list'</script>")
    else:
        return render(request, 'book_req.html')

def booking_list(re):
    if 'e_id' in re.session:
        z=re.session['e_id']
        x=booking.objects.filter(employee_name=z,action='Confirm')
        return render(re,'bookings.html',{'r':x})

def bookkings(re):
    d=booking.objects.all()
    return render(re,'newadmn_booking.html',{'r':d})

def search(request):     #searching author
    if request.method == "POST":
        r = request.POST['n1']
        d = employee_registration.objects.filter(location=r)
        if list (d) == []:
            print(d)
            return HttpResponse("<script>alert('Not found check another location');window.location='photographer'</script>")
        else:
            return render(request,'search_result.html',{'r':d})
    else:
        return HttpResponse("<script>alert('No results found');window.location='photographer'</script>")


# def final_pay(request, id):
#     amount = 5000
#     order_currency = 'INR'
#     client = razorpay.Client(
#         auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
#     cursor = connection.cursor()
#     cursor.execute(
#         "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(id) + "' ")
#
#     payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
#     return render(request, "final_payment.html")


def user_inbox(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=booking.objects.filter(name=y,action='Confirm',payment='pending')
        if list (d) == []:
            return HttpResponse("<script>alert('Message is empty');window.location='index1'</script>")
        else:
            return HttpResponse("<script> alert ('Your booking is confirmed. Make your payment') ; window.location='your_booking' </script>")
    else:
        return HttpResponse("<script>alert('No results found');window.location='index1'</script>")

def book_confirm(re):
    if 'u_id' in re.session:
        z=re.session['u_id']
        d=booking.objects.filter(name=z,payment='pending')
        return render(re,'book_confirm.html',{'r':d})
    else:
        return HttpResponse('ERROR')

def reviewlist(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=feedback1.objects.filter(username=y)
        return render(re,'reviewlist.html',{'r':d})
    else:
        return render(re,'index1.html')
def remove_review(request):
    if request.method == "POST":
        r = request.POST['n1']
        d = feedback1.objects.filter(review=r)
        d.delete()
        return HttpResponse("<script>alert('review deleted');window.location='index1'</script>")
    else:
        return HttpResponse('not okay')

def your_booking(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=booking.objects.filter(username=y,action='Confirm')
        return render(re,'your_booking.html',{'r':d})
    else:
        return HttpResponse('NO BOOKING')

def your_cancelledbooking(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=booking.objects.filter(username=y,action='cancelled')
        return render(re,'cancelled_booking.html',{'r1':d})
    else:
        return HttpResponse('NO BOOKING')

def your_pendingbooking(re):
    if 'u_id' in re.session:
        y=re.session ['u_id']
        d=booking.objects.filter(username=y,action='pending')
        return render(re,'pending_booking.html',{'r1':d})
    else:
        return HttpResponse('NO BOOKING')

# def payy(re):
#     if re.method=='POST':
#         try:
#             x=int(re.POST['n1'])
#             re.session['pending']=re.POST['n2']
#             k=re.session['pending']
#             print(k)
#             s=x*500
#             order_currency='INR'
#             client=razorpay.Client(
#                 auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
#             return render(re,'final_payment.html',{'n':s,'l':k})
#         except Exception:
#             return HttpResponse("<script>alert('Thank you for payment');window.location='index1'</script>")
    # ------------sample----------
# from django.contrib.auth.decorators import login_required
# from .models import Profile
#
# @login_required
# def profile(request):
#     profile = Profile.objects.get_or_create(user=request.user)[0]
#     return render(request, 'sample checking.html', {'profile': profile})

def emp_addphoto(re):
    if 'e_id' in re.session:
        z = re.session['e_id']
        if re.method=='POST':
            a = re.POST['A']
            # b = re.POST['B']
            c = re.POST['C']
            # d = re.POST['D']
            e = re.POST['E']
            # f = re.POST['F']
            x = emp_gallery.objects.create(work1=a, work2=c,work3=e, username=z)
            print(x)
            x.save()
            return render(re, 'emp_addphoto.html')
        else:
            return render(re, 'emp_addphoto.html')



def gallery_emp(re):
    if 'e_id' in re.session:
        z = re.session['e_id']
        x=emp_gallery.filter(username=z)
        return render(re,"emp_galleryview.html")

#------forgot password-------
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = user_registration.objects.get(email=email)
            print(user)
        except:
            # return HttpResponse("<script>alert('Email is not registered');windows.location='login' </script>")
            messages.info(request, "Network connection failed")
            return redirect(forgot_password)

        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user_registration=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            print("sending..")
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            print("hai")
            # return render(request, 'emailsent.html')
            print("sended")
        except:
            print("network error")
            # return HttpResponse("<script>alert('Network connection failed');windows.location='login' </script>")
            messages.error(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'forget.html')

def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    # usr = user_registration.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            a=password_reset.user_registration.username
            print(a)
            log_in.objects.filter(username=a).update(password=new_password)
            # password_reset.user.set_password(new_password)
            # password_reset.user.save()
            # password_reset.delete()
            return redirect(login)
    return render(request, 'reset.html',{'token':token})


def user_message(req):
    if req.method=='POST':
        nm=req.POST['name']
        email=req.POST['email']
        sub=req.POST['subject']
        msg=req.POST['message']
        send_mail(f'{sub} from user {req.user.email}', f'{msg}','settings.EMAIL_HOST_USER', [email], fail_silently=False)

    return render(req,'user_message.html')


#cancel booking
def cancel(re):
    if re.method=='POST':
        x=re.POST['n2']
        d=booking.objects.filter(email=x,payment='pending')
        if list(d) == []:
            return HttpResponse("<script>alert('not allowed.. no refund after payment');window.location='../index1 '</script>")
        else:
            # return render(re, 'employee_reviews.html', {'r': d})
            d.update(action="cancelled")
            return HttpResponse("<script>alert('your booking is cancelled');window.location='../index1 '</script>")
    else:
        return HttpResponse("error")

def employeeee_review(re,user):
    print(user)
    d = feedback1.objects.filter(employee_name=user)
    x=employee_registration.objects.filter(username=user)
    if list(d) == []:
        return HttpResponse("<script>alert('No Reviews.....');window.location='../photographer '</script>")
    else:
        return render(re, 'employee_reviews.html', {'r': d,'r1':x})

def payment1(request):
    if request.method == 'POST':
            y = request.POST['b2']
            z = request.POST['b3']
            a = request.POST['b4']
            request.session['p_name'] = a
            request.session['l_name'] = y

            d = booking.objects.filter(employee_name=a,name=y,action='Confirm',payment='pending')
            if list(d) ==[]:
                url='your_booking'
                msge='''<script>alert('payment not allowed.. your in processing')
                window.location='%s'</script>'''%(url)
                return HttpResponse(msge)
            else:
                data=amountdetails.objects.filter(username=a)
                for i in data:
                    k=i.advAmound
                return render(request,'payment.html',{'r':d,'r1':k})
    else:
        return render(request, 'payment.html')




#user-paying payment
def pay(request, id):
        advAmound = (id)*100
        request.session['advAmound']=id
        order_currency = 'INR'
        client = razorpay.Client(
            auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
        # cursor = connection.cursor()
        # cursor.execute(
        #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(
        #         id) + "' ")

        # payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        return render(request, "pay.html",{'r':advAmound})


def success(re):
    if 'u_id' in re.session:
        z = re.session['u_id']
        d = booking.objects.filter(username=z)
        e_name=re.session['p_name']
    #     x=d.email
        print(d)
        # y = d.room_category
        # d1=payment.objects.create(name=a,employee_name=b,advAmound=c,email=x)
        # d1.save()
        # print(d1)
        # d2 = Booking.objects.get(name=a,hotel_name=b)
        # y=d2.username
        # # d3=adpay.objects.create(username=y,price=10,hotel_name=b)
        # d3 = adpay.objects.create(username=y, hotel_name=b)
        # d3.save()
        d4=booking.objects.filter(username=z,employee_name=e_name)
        print(d4)
        d4.update(payment='paid')
        return HttpResponse("<script>alert('Your payment succeeded');window.location='your_booking'</script>")
    # return render(request, 'user.html')

def empview_galley(re):
    if 'e_id' in re.session:
        z = re.session['e_id']
        d = emp_gallery.objects.filter(username=z)
        return render(re,'emp_viewgallery.html',{'r':d})

# def emp_addpayment(re):
#     # if re.method=='POST':
#     #     a = re.POST['USERNAME']
#     #     m = re.POST['AMOUNT1']
#     #     n = re.POST['AMOUNT2']
#     #     p = amountdetails.objects.create(fullamount=m, advAmound=n, username=j)
#     #     p.save()
#     #     return render(re,'addpaymnt.html')
#     if 'e_id' in re.session:
#         z = re.session['e_id']
#         if re.method=='POST':
#             m = re.POST['advance_amount']
#             n = re.POST['full_amount']
#             x = amountdetails.objects.create(fullamount=m, advAmound=n, username=z)
#             x.save()
#     return render(re, 'addpaymt.html')

def user(request):
    if 'u_id' in request.session:
        a = request.session['u_id']
        d = user_registration.objects.filter(username=a)
        data = employee_registration.objects.filter(action='Confirm')
        print(data)
        s = set()
        print(s)
        for i in data:
            s.add(i.location)
        l = list(s)
        print(l)
        return render(request, 'Photographers.html', {'r1': l})
    else:
        return render(request, 'login.html')


def locationfilter(re):
    if 'u_id' in re.session:
        x=re.session['u_id']
        z=employee_registration.objects.filter(action='Confirm')
        s = set()
        print(s)
        for i in z:
            s.add(i.location)
        l = list(s)
        return render(re,'photographers.html',{'r':z})
    else:
        return render(re,'photographers.html')
def location(request):
    if request.method == 'POST':
        x = request.POST['n1']
        d = employee_registration.objects.filter(location=x)
        print(d)
        return render(request, 'search_result.html', {'d1': d})
    else:
        return HttpResponse("failed")
