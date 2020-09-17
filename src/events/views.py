from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.utils import timezone #추가
from datetime import datetime #추가

#from django.contrib.auth.models import User
from django.contrib.auth import (
	login as django_login,
	logout as django_logout,
	authenticate,
	)
from django.template import RequestContext


# Create your views here.
def main(request):
	# if not request.user.is_authenticated:
	# 	data = {"name":request.user, "is_authenticated":request.user.is_authenticated}
	# else:
	# 	data = {"last_login":request.user.last_login, "name":request.user.username,
	# 	"password":request.user.password, "is_authenticated":request.user.is_authenticated}
	# return render(request, 'main2.html', context={"data":data})
	if request.method == 'GET':
		if not request.session.get('login_complete',False):
			unknown_user = User(email='unknown')
			context = { 'member' : unknown_user}
		else:
			email = request.session.get('email', 'unknown')
			user = User(email = email)
			context = {'user' : user}
			return render(request, 'main.html', context)

	#
	# if request.GET.get('search_key'):
	# 	search_key = request.GET['search_key']
	# 	# con_list = Concert.objects.filter(name__in=search_key).order_by('name')
	# 	return render(request, 'searchcon.html',{'search_key':search_key})


	# elif request.method == 'POST':
	# 	search_key = request.POST['search_key']
	# 	con_list = Concert.objects.filter(name__in=search_key)
	# 	return render(request, 'searchcon.html', {'conlist': con_list})

	return render(request, 'main.html')


def searchcon(request):
	search = request.POST['search_key']
	concerts = list(Concert.objects.filter(name__icontains = search))

	tmp = []
	for i in concerts:
		group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').get(concert = i.code)
		tmp.append(group)


	return render(request, 'searchcon.html', {'tmp':tmp, 'search':search})


# def searchcon(request,search_key):
# 	con_list = list(Concert.objects.filter(name__icontains=search_key))
#
# 	gg = []
# 	for i in len(con_list):
# 		group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').get(code = con_list[i].code)
# 		gg.append(group)
# 	return render(request, 'searchcon.html', {'con_list': gg})
#

def info(request):
   return render(request, 'info.html')

def concert(request):
   return render(request, 'concert.html')

def menuticket(request):
	if request.method == 'GET':
		group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').all()[9163:9200]

		return render(request,'menu_ticketing.html',{'group':group})

def conall(request, code):
	if request.method == 'GET':
		if code == 'now':
			group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').filter(date__year='2019',date__month = '6', date__day__gt ='13')
			return render(request,'concert_all.html',{'group':group, 'code':code})
		elif code == 'plan':
			group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').filter(date__year='2019',date__month__gt = '6')
			return render(request,'concert_all.html',{'group':group, 'code':code})
		elif code == 'exit':
			group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').filter(date__year__lt='2019',date__month__lt = '6')[:200]
			return render(request,'concert_all.html',{'group':group, 'code':code})
		else:
			group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').all()[8000:8200]
			return render(request,'concert_all.html',{'group':group, 'code':code})


def condate(request, code):
	if request.method == 'GET':
		if code == 'year':
			dates = []
			date1 = Schedule.objects.prefetch_related('concert').select_related('concert__hall').filter(date__year='2015')[:20]
			date2 = Schedule.objects.prefetch_related('concert').select_related('concert__hall').filter(date__year='2016')[:20]
			date3 = Schedule.objects.prefetch_related('concert').select_related('concert__hall').filter(date__year='2017')[:20]
			date4 = Schedule.objects.prefetch_related('concert').select_related('concert__hall').filter(date__year='2019')[:20]
			dates.append(date1)
			dates.append(date2)
			dates.append(date3)
			dates.append(date4)
			return render(request, 'concert_date.html', {'dates': dates, 'code':code})
		if code == 'month':
			dates = []
			for i in range(1, 13):
				dates.append(Schedule.objects.prefetch_related('concert').select_related('concert__hall').filter(date__month=str(i))[:10])
			return render(request, 'concert_date.html', {'dates': dates, 'code':code})




def conart(request):
	if request.method == 'GET':
		# artist = Artist.objects.all()
		# # g = Perform.objects.prefetch_related('concert').prefetch_related('concert__artist').
		# if code == 'kor':
		#
		# 	group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').filter(date__year='2019',date__month = '6', date__day__gt ='13')
		# 	return render(request,'concert_all.html',{'group':group, 'code':code})
		# else:
		# 	group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').all()[8000:8200]
		# 	return render(request,'concert_all.html',{'group':group, 'code':code})
		artists = []
		arti = Artist.objects.all()[:6]

		for i in range(6):
			artists.append(arti[i].code)

		art = []
		for i in range(6):
			# b = Schedule.objects.prefetch_related('concert').select_related('concert__perform')
			a = Perform.objects.prefetch_related('concert').select_related('concert__hall').filter(artist = artists[i])
			art.append(a)

		return render(request, 'concert_artist.html', {'artists':art})

def conrank(request):
	return render(request, 'concert_ticket.html')

def fuelcharge(request):
	if request.method == "GET":
		if request.session.keys():
			e = request.session['email']
			u = User.objects.get(email=e)
			return render(request, 'fuel.html',{'fuel':u.coin})
		else:
			return render(request, 'main.html')
	if request.method == "POST":
		if request.session.keys():
			e = request.session['email']
			u = User.objects.get(email=e)
			fuel = request.POST['fuel']
			u.coin = int(u.coin) + int(fuel)
			u.save()
			content = {'username': u.name, 'email': u.email, 'coin': u.coin}
			return render(request, 'mypage.html', content)

def detailedsearch(request):
	concertname = request.POST['concertname']
	artistname = request.POST['artistname']
	startdate = request.POST['startdate']
	enddate = request.POST['enddate']
	location = request.POST['location']

	all = Schedule.objects.select_related('concert').select_related('concert__hall')

	return render(request,'detail_searchcon.html',{'tmp':tmp})

	#
	# if len(concertname) > 0:



		# if len(artistname) > 0:
		# 	artists = Artist.objects.filter(name__icontains = artistname)
		# 	concerts = Concert.objects.filter(name__icontains = concertname)
		# 	tmp = []
		# 	for i in concerts:
		# 		artist = Perform.objects.filter(concert = i.code)
		# 		for j in artist:
		# 			return
		#
		# 	return render(request, 'detail_searchcon.html', {'tmp': tmp})

	# 	concerts = Concert.objects.filter(name__icontains = concertname)
	# 	tmp = []
	# 	for i in concerts:
	# 		group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').get(concert=i.code)
	# 		tmp.append(group)
	# 	return render(request, 'detail_searchcon.html', {'tmp': tmp})
	# if len(artistname) > 0:
	# 	artists = Artist.objects.filter(name__icontains = artistname)
	# 	tmp = []
	# 	for i in artists:
	# 		perform = Perform.objects.filter(artist = i.code)
	# 		for j in perform:
	# 			group = Schedule.objects.prefetch_related('concert').select_related('concert__hall').get(concert=j.concert)
	# 			tmp.append(group)
	# 			print(group)
	# 	return render(request, 'detail_searchcon.html', {'tmp': tmp})
	#
	# return render(request, 'detail_searchcon.html')


# @login_required
def mypage(request):
	if request.method == 'GET':
		if request.session.keys():
			e = request.session['email']
			u = User.objects.get(email = e)
			b = Book.objects.select_related('concert').filter(email = e)
			fc = Fconcert.objects.filter(email = u)
			fa = Fartist.objects.filter(email = u)

			temp = []
			for i in fc:
				con = Concert.objects.get(code = i.concert.code)
				temp.append(con)

			temp2 = []
			for i in fa:
				art = Artist.objects.get(code = i.artist.code)
				temp2.append(art)

			content = {'username':u.name, 'email':u.email, 'coin':u.coin, 'book':b, 'fc': fc, 'temp': temp, 'fa':fa, 'temp2':temp2}

			return render(request, 'mypage.html', content)
		else:
			# 팝업 창 띄울 수 있도록
			return render(request,'main.html')



def posdetail(request,code):
	if request.method == 'GET':
		posu = Concert.objects.select_related('hall').get(code = code)
		sche = Schedule.objects.filter(concert = code)
		# qqq = Perform.objects.prefetch_related('concert').select_related('artist')
		artist = list(Perform.objects.filter(concert = code))
		poscontent = {'con_name':posu.name, 'con_hall':posu.hall.name,'con_poster':posu.poster, 'artist':artist, 'sche':sche, 'ccode':code}
		return render(request, 'concert_detail.html', poscontent)

	if request.method == "POST":
		if request.session.keys():
			e = request.session['email']
			u = User.objects.get(email = e)
			c = Concert.objects.get(code = code)
			fav = Fconcert(concert = c,email = u)
			fav.save()
			return redirect('mypage')
		else:
			return render(request, 'main.html')

def ticketing(request,code):
	if request.method == 'GET':
		if request.session.keys():
			e = request.session['email']
			u = User.objects.get(email = e)

			# book미리 예약된 거 있는지 확인



			ticket = Ticket.objects.select_related('concert').select_related('concert__seat').filter(concert = code)[0]

			# if len(ticket) == 0:
			# 	return render(request,'main.html') #에러메시지

			acode = Perform.objects.prefetch_related('concert')
			book = Book.objects.filter(email = e)
			# endbook = list(Book.objects.filter(concert=code))
			endbook = Schedule.objects.select_related('concert').select_related('concert__seat').filter(concert= code)

			# poar = Artist.objects.get(code = acode)
			sche = Schedule.objects.filter(concert = code)
			posu = Concert.objects.select_related('hall').get(code = code)
			artist = list(Perform.objects.filter(concert = code))



			section = list(Seat.objects.filter(concert = code).values_list('section',flat=True).distinct())

			seat = {}
			for i in section:
				tp = list(Seat.objects.filter(concert = code).filter(section = i).values_list('number',flat= True))
				seat[i] = tp

			# seat = list(Seat.objects.filter(concert = code).values_list('number',flat=True).distinct())
			# seat.sort()

			prebook = list(Book.objects.filter(concert = code))

			for i in range(len(prebook)):
				tss = prebook[i].section
				tnn = prebook[i].number
				if tss in section and tnn in seat[tss]:
					seat[tss].remove(tnn)


			# ticket = Ticket.objects.select_related('concert').select_related('concert__seat').filter(concert = code)


			return render(request, 'ticketing.html',{'posu':posu, 'artist':artist,'coin':u.coin, 'ticket':ticket.price, 'sche':sche, 'section':section,'seat':seat,'book':book, 'endbook':endbook})
		else:
			# 팝업 창 띄울 수 있도록
			return render(request,'main.html')


	if request.method == 'POST':
		if request.session.keys():

			e = request.session['email']
			# 예약목록 가져오기
			bef = Book.objects.filter(email = e)
			con_list = []
			for i in bef:
				con_list.append(i.concert.code)

			if code in con_list: # 에러 보내야 할 듯
				return HttpResponse("이미 예매된 공연입니다")
				# return render(request, "ticketing.html")

			con = Concert.objects.get(code= code)

			# price = request.POST['price']
			sec = request.POST['section']

			price = Ticket.objects.filter(concert = code).get(rating = sec)
			sea = request.POST['seatno']
			booked = request.POST['booked']
			u = User.objects.get(email = e)
			# concert, email, coin, booked_at

			book = Book.objects.create(
				concert = con,
				email = u,
				booked_at = booked,
				coin = price.price, #임시가격
				section = sec,
				number=  sea
			)

			u.coin = int(u.coin) - int(price.price)
			u.save()


			return redirect('mypage')
			# return render(request,'mypage.html')
		else:
			# 팝업 창 띄울 수 있도록
			return render(request,'main.html')



def artpop(request,code):
	if request.method == 'GET':
		a = Artist.objects.get(code = code)
		m = list(Member.objects.filter(artist= code))
		con = Perform.objects.select_related('concert').filter(artist = code)
		return render(request,'artist_info.html',{'a': a,'m':m, 'con':con})

	if request.method == "POST":
		if request.session.keys():
			e = request.session['email']
			u = User.objects.get(email = e)
			c = Artist.objects.get(code = code)
			fav = Fartist(artist = c,email = u)
			fav.save()
			return HttpResponse('관심가수로 등록되었습니다.')
		else:
			return render(request, 'main.html')



def register(request):
	if request.method == 'POST':
		name = request.POST['name']
		birth = request.POST['birth']
		sex = request.POST['sex']
		email = request.POST['email']
		password = request.POST['password1']
		passworda = request.POST['password2']
		phone= request.POST['phone']

		e = User.objects.filter(email=email)
		if len(e) > 0:
			return render(request,'join.html', {'error':'중복된 이메일이 존재합니다'})

		if password == passworda:

				user = User.objects.create(
					name = name,
					birth = birth,
					sex = sex,
					email = email,
					password = password,
					contact = phone,
				)
				return redirect('/')
		else:
			# messages.error(request, "비밀번호가 일치하지 않습니다")
			return render(request,'join.html', {'error':'비밀번호가 일치하지 않습니다'})
	else:
		return render(request, 'join.html')

def login(request):
	if request.method == "POST":

		email = request.POST['email']
		password = request.POST['password']


		try:
			u = User.objects.get(email = email)
		except:
			return render(request,'login.html', {'error':'이메일이 존재하지 않습니다'})


		if u.password == password:
			request.session['email'] = u.email

			return render(request,"main.html")
		else:
			return render(request,'login.html', {'error':'비밀번호가 일치하지 않습니다'})

	else:
		return render(request, "login.html")


def logout(request):
	del request.session['email']
	return render(request,"main.html")
