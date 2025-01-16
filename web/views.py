from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Connect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# Create your views here.
def index(request):
    return render(request, "index.html", locals())



def connect(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # 儲存資料到模型
        connect_instance = Connect.objects.create(
            name=name,
            company_name=company_name,
            email=email,
            phone=phone,
            message=message,
        )

        # 發送郵件給 superuser
        superusers = User.objects.filter(is_superuser=True)
        superuser_emails = [user.email for user in superusers if user.email]

        if superuser_emails:
            send_mail(
                subject='新的聯絡表單提交',
                message=f'姓名: {name}\n公司: {company_name}\nEmail: {email}\n電話: {phone}\n訊息: {message}',
                from_email='kylelin.development@gmail.com',  # 您的郵件地址
                recipient_list=superuser_emails,
            )

        return redirect('connect_success')  # 表單提交成功後跳轉

    return render(request, 'connect.html')

def connect_success(request):
    return render(request, 'connect_success.html')