from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from models import Bug
from forms import BugForm
from datetime import datetime 


def home(request):
	print 'print some thing ', request.POST
	return render(request,'bugz/home.html')
# a summary of all the bugs to admin.
def bugsummary_admin(request):
	bugs = Bug.objects.filter(record_stat = 'O')
	return render(request, 'bugz/bugsummary_admin.html',{'bugs':bugs})

#details of a bug to admin
def bugdetails(request,bug_id):
	# if request.method == 'POST':
	# 	bugformreason = BugFormReason(request.POST)
	# 	if bugFormReason.is_valid():
	# 		bugreason = bugformreason.save(commit = False)
	# 		bugreason.save()
	# 	return render(request,'bugz/bugsummary_admin.html')
	# else:
	print 'show details ', request
	bug = Bug.objects.get(pk = bug_id)
	return render(request,'bugz/bugdetails.html',{'bug':bug});

#to save the bug 
def registerbug(request):
	
	if request.method == 'POST': # for a form with data in it
		bugform = BugForm(request.POST)
		if bugform.is_valid():
			bug = bugform.save(commit = False)
			bug.date_time = datetime.now()
			bug.save()
		return render(request,'bugz/thankyou.html')
	else: # for a new form
		bugform = BugForm()

	return render (request,'bugz/registerbug.html',{'bugform' : bugform})


#as a thankyou
def thankyou(request,bug_id):
	bug_id = Bug.objects.get(pk = bug_id)
	print request.POST
	return render (request,'bugz/thankyou.html',{'bug_id':bug_id});

