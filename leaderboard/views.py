from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from sellbuy.models import ShareDetail,Share


def leaderboard(request):

	return render(request,'leaderboard/leaderboard.html')
def get_leaderboard(request):
	user = ShareDetail.objects.all()
	shares = Share.objects.exclude(name='none').all()
	#print "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMatrixc="+str(Matrixc)

	tuple_list1=[]
	tuple_list2=[]
	tuple_list3=[]
	count=0
	for o in user:
		shareworth = float(0)
		for sh in shares:
			shareworth += float(getattr(o,str(sh.name))) * float(sh.currentprice)
		UserNetWorth = float(o.money_in_hand) + shareworth
		#print o.username,UserNetWorth
		#tuple_list.append(tuple({int(UserNetWorth),str(o.username)}))
		tuple_list1.append(UserNetWorth)
		print UserNetWorth
		tuple_list2.append(str(o.username))
		print o.username
		tuple_list3.append(count)
		print count
		#tuple_list[count][1]=int(UserNetWorth)
		#print tuple_list
		print count
		count=count+1
	high_i=0
	high=0
	ans=''
	n=len(tuple_list1)
	print n
	for i in range(0,n-1):
		print ",,,,,,,,,,,,i=",i
		high=tuple_list1[i]
		for j in range(i+1,n):
			print ",,,,,,,,,,,j=",j
			if(tuple_list1[j]>high):
				high=tuple_list1[j]
				high_i=jq
		tmp_val=tuple_list1[i]
		tuple_list1[i]=high
		tuple_list1[high_i]=tmp_val
		tmp_val=tuple_list3[i]
		tuple_list3[i]=tuple_list3[high_i]
		tuple_list3[high_i]=tmp_val
	ans="<table border=3>"
	for i in range(2):
		print "tuple_list3[i]=",tuple_list3[i]
		print "tuple_list2[0]=",tuple_list2[0]
		print "tuple_list2[1]=",tuple_list2[1]

		ans+="<tr><td>"+str(tuple_list2[int(tuple_list3[i])])+'</td><td>'+str(tuple_list1[i])+"</td></tr>"
		#ans+=str(tuple_list3[i])+' '+str(tuple_list1[i])
	ans+='</table>'
	return HttpResponse(ans)