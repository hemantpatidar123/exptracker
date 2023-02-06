from django.shortcuts import render,redirect
from .models import User,Expence,Income

def renderPage(req):
	return render(req,"home.html")

def Deshboard(req):
	if 'uid' in req.session:
		uid=req.session['uid']
		expences=Expence.objects.filter(user_id_id=uid)
		incomes=Income.objects.filter(user_id_id=uid)
		TotalExpence=0
		TotalIncome=0
		for expence in expences:
			TotalExpence+=expence.amount
		for income in incomes:
			TotalIncome+=income.amount
		NetBalance=TotalIncome-TotalExpence 
		return render(req,"deshboard.html",{'NetBalance':NetBalance,'Total_Income':TotalIncome,"Total_Exp":TotalExpence})
	else:
		return redirect("/")

def signUp(req):
	return render(req,"signup.html")

def showExpPage(req):
	return render(req,"expence.html")
def ShowIncomePage(req):
	return render(req,"income.html")

def showExp(req):
	if 'uid' in req.session:
		uid=req.session['uid']
		record=Expence.objects.filter(user_id_id=uid)
		if record:
			list=record.values()
			return render(req,"showExp.html",{'list':list})
	else:
		return redirect("/")


def showIncome(req):
	if 'uid' in req.session:
		uid=req.session['uid']
		record=Income.objects.filter(user_id_id=uid)
		if record:
			list=record.values()
			return render(req,"showIncome.html",{'list':list})
	else:
		return redirect("/")

def signup_save(req):
	obj=User()
	obj.name=req.GET.get('name')
	obj.password=req.GET.get('password')
	obj.email=req.GET.get('email')
	obj.phone=req.GET.get('phone')
	obj.save()
	return redirect('/')

def login_Data(req):
	email=req.POST.get('email')
	password=req.POST.get('password')
	user=User.objects.filter(email=email,password=password)
	if(user):
		list=user.values()
		req.session['uid']=list[0]['id']
		req.session['email']=list[0]['email']
		return redirect("/Deshboard")
	else:
		return render(req,"home.html",{'message':"Invalid UserName & Password"})

def save_Expence(req):
	if 'uid' in req.session:
		uid=req.session['uid']
		obj=Expence()
		obj.time=req.GET.get('time')
		obj.date=req.GET.get('date')
		obj.remark=req.GET.get('remark')
		obj.amount=req.GET.get('amount')
		obj.category=req.GET.get('s1')
		obj.user_id_id=uid
		obj.save()
		return redirect("/Deshboard")
	else:
		return redirect("/")

def save_income(req):
	if 'uid' in req.session:
		uid=req.session['uid']
		obj=Income()
		obj.time=req.GET.get('time')
		obj.date=req.GET.get('date')
		obj.remark=req.GET.get('rem3ark')
		obj.amount=req.GET.get('amount')
		obj.category=req.GET.get('s1')
		obj.user_id_id=uid
		obj.save()
		return redirect("/Deshboard")
	else:
		return redirect("/")

def logout(req):
	del req.session['uid']
	return redirect("/")







