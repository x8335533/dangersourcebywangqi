from django.shortcuts import render
from checksource.models import Checkproblem,ImgProblem
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CheckproblemForm,InquireForm,ImgProblemForm

# Create your views here.
def index(request):
	"""主页"""
	return render(request, 'checksource/index.html')
	
def	allproblems(request):
	"""列出所有检查的问题"""
	problems = Checkproblem.objects.order_by('-checkwhen')
	i = set()
	for pp in problems:
		for imgs in pp.imgproblem_set.all():
			i.add(imgs)
	context = {'problems': problems,'imgproblem':i}
	return render(request, 'checksource/allproblems.html', context)
	
def newproblem(request):
	"""添加一个新问题"""
	if request.method != 'POST':
		# 未提交数据：创建一个新表单
		form = CheckproblemForm()
		context = {'form': form}
		return render(request, 'checksource/newproblem.html', context)
	else:
		# POST提交的数据,对数据进行处理
		form = CheckproblemForm(request.POST)
		if form.is_valid():
			p = Checkproblem()
			for key,value in request.POST.items():
				if key =='checkwhen':
					p.checkwhen = value
				elif key =='checkdepartment':
					p.checkdepartment = value	
				elif key =='checkway':
					p.checkway = value
				elif key =='checkwho':
					p.checkwho = value
				elif key =='problemdetail':
					p.problemdetail = value
				elif key =='problemtype':
					p.problemtype = value
				elif key =='problemsolve':
					p.problemsolve = value
				elif key =='whoresponsible':
					p.whoresponsible = value
				elif key =='problemdepartment':
					p.problemdepartment = value
				elif key =='departmentwho':
					p.departmentwho = value
				elif key =='problemteam':
					p.problemteam = value
				elif key =='problemwho':
					p.problemwho = value
				elif key =='problemreason':
					p.problemreason = value
				elif key =='closedate':
					p.closedatet = value
				elif key =='ifdone':
					p.ifdone = value
				elif key =='projecttype':
					p.projecttype = value
				elif key =='closewho':
					p.closewho = value
				elif key =='somethingelse':
					p.somethingelse = value
				elif key =='checkdepartment':
					p.checkdepartment = value
			p.save()
			return HttpResponseRedirect(reverse('checksource:upload',args=[p.id]))
			
def editproblem(request,problem_id):
	"""编辑问题的内容"""
	next = request.GET.get('next', '')
	problem = Checkproblem.objects.get(id=problem_id)
	if request.method != 'POST':
		form = CheckproblemForm(instance=problem)
		context = {'problem':problem,'form': form}
		return render(request, 'checksource/editproblem.html', context)
	else:
		form = CheckproblemForm(instance=problem, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('checksource:problemid',args=[problem_id]))
			#return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
			
	

def inquireinput(request):
	"""查询具体条件的检查"""
	pdic = ['checkwhenstart','checkwhenend','checkdepartment','checkway','checkwho','problemdetail','problemtype','problemsolve','whoresponsible','departmentincharge','problemdepartment','departmentwho','problemteam','problemwho','problemreason','projecttype','closewho','ifdone']
	paramdic = {}
	if request.method!='POST':
		form = InquireForm()
		return render(request,'checksource/inquireinput.html',{'form':form})
	else:
		form = InquireForm(data=request.POST)
		if form.is_valid():
			for key,value in request.POST.items():
				if key in pdic:
					if not value:
						if key == 'checkwhenstart':
							paramdic[key] = '2019-01-01'
						elif key == 'checkwhenend':
							paramdic[key] = '2119-12-31'
						else:
							paramdic[key]='all'				
					else:
						paramdic[key]= value			
				else:
					continue		
			
			return HttpResponseRedirect(reverse('checksource:inquireresult',kwargs=paramdic))
					
def inquireresult(request,**kwargs):
	
	"""查询具体条件的检查"""
	i = set()
	problemwithpicid = set()
	problems = Checkproblem.objects.all()
	for key,value in kwargs.items():
		if key!='checkwhenstart' and key!='checkwhenend':
			if value == 'all':
				continue
			elif key == 'problemdetail':
				problems = problems.filter(problemdetail__icontains=value)
			elif key == 'problemsolve':
				problems = problems.filter(problemsolve__icontains=value)
			elif key == 'problemreason':
				problems = problems.filter(problemreason__icontains=value)		
			else:
				condition = {key:value}
				problems = problems.filter(**condition).order_by('checkwhen')
		else:
			continue		
	problems = problems.filter(checkwhen__range=(kwargs['checkwhenstart'],kwargs['checkwhenend'])).order_by('-checkwhen')				
	for pp in problems:
		if pp.imgproblem_set.all():
			problemwithpicid.add(pp.id)
		for imgs in pp.imgproblem_set.all():
			i.add(imgs)
	 
	
	context = {'problems':problems,'imgproblem':i,'paramdic':kwargs,'problemwithpicid':problemwithpicid}	
	return render(request, 'checksource/inquireresult.html', context)		
		
		
		


	
def upload(request,problem_id):
	"""上传问题的图片"""
	next=request.GET.get('next','/')
	problem = Checkproblem.objects.get(id=problem_id)
	if request.method != 'POST':
		#form = ImgProblemForm()
		#context = {'form':form,'problem':problem}
		return render(request,'checksource/upload.html')
	else:
		files = request.FILES.getlist('img',None)
		for f in files:
			form = ImgProblem(img = f)
			form.Checkproblem = problem
			form.save()
		#return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))	
		return HttpResponseRedirect(reverse('checksource:problemid',args=[problem_id]))	
		"""
		form = ImgProblemForm(request.POST,request.FILES)
		new_img = form.save(commit=False)
		new_img.Checkproblem = problem
		new_img.save()
		return HttpResponseRedirect(reverse('checksource:problemid',args=[problem_id]))
		"""
		
def deleteimg(request,img_id):
	next=request.GET.get('next','/')
	imgproblem = ImgProblem.objects.get(id = img_id)
	imgproblem.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	#return HttpResponseRedirect(reverse('checksource:allproblems'))	
	
def problemid(request,p_id):
	problem = Checkproblem.objects.get(id = p_id)
	i = set()
	for imgs in problem.imgproblem_set.all():
		i.add(imgs)
	context = {'pblm':problem,'imgproblem':i}
	return render(request, 'checksource/problemid.html', context)
	
def problemidcheck(request,p_id,checkwhenstart,checkwhenend,checkdepartment,checkway,checkwho,problemdetail,problemtype,problemsolve,whoresponsible,departmentincharge,problemdepartment,departmentwho,problemteam,problemwho,problemreason,projecttype,closewho,ifdone):
	pdic = ['p_id','checkwhenstart','checkwhenend','checkdepartment','checkway','checkwho','problemdetail','problemtype','problemsolve','whoresponsible','departmentincharge','problemdepartment','departmentwho','problemteam','problemwho','problemreason','projecttype','closewho']
	paramdic={}
	paramdic['checkwhenstart']= checkwhenstart
	paramdic['checkwhenend']=checkwhenend
	paramdic['checkdepartment']=checkdepartment
	paramdic['checkway']=checkway
	paramdic['checkwho']=checkwho
	paramdic['problemdetail']=problemdetail
	paramdic['problemtype']=problemtype
	paramdic['problemsolve']=problemsolve
	paramdic['whoresponsible']=whoresponsible
	paramdic['departmentincharge']=departmentincharge
	paramdic['problemdepartment']=problemdepartment
	paramdic['departmentwho']=departmentwho
	paramdic['problemteam']=problemteam
	paramdic['problemwho']=problemwho
	paramdic['problemreason']=problemreason
	paramdic['projecttype']=projecttype
	paramdic['closewho']=closewho
	paramdic['ifdone']=ifdone
	problem = Checkproblem.objects.get(id = p_id)
	
				
	i = set()
	for imgs in problem.imgproblem_set.all():
		i.add(imgs)
	context = {'pblm':problem,'imgproblem':i,'paramdic':paramdic}
	return render(request, 'checksource/problemidcheck.html', context)
	
	
def editproblemcheck(request,p_id,checkwhenstart,checkwhenend,checkdepartment,checkway,checkwho,problemdetail,problemtype,problemsolve,whoresponsible,departmentincharge,problemdepartment,departmentwho,problemteam,problemwho,problemreason,projecttype,closewho,ifdone):
	problem = Checkproblem.objects.get(id=p_id)
	paramdic={}
	paramdic['p_id']= p_id
	paramdic['checkwhenstart']= checkwhenstart
	paramdic['checkwhenend']=checkwhenend
	paramdic['checkdepartment']=checkdepartment
	paramdic['checkway']=checkway
	paramdic['checkwho']=checkwho
	paramdic['problemdetail']=problemdetail
	paramdic['problemtype']=problemtype
	paramdic['problemsolve']=problemsolve
	paramdic['whoresponsible']=whoresponsible
	paramdic['departmentincharge']=departmentincharge
	paramdic['problemdepartment']=problemdepartment
	paramdic['departmentwho']=departmentwho
	paramdic['problemteam']=problemteam
	paramdic['problemwho']=problemwho
	paramdic['problemreason']=problemreason
	paramdic['projecttype']=projecttype
	paramdic['closewho']=closewho
	paramdic['ifdone']=ifdone
	if request.method != 'POST':
		form = CheckproblemForm(instance=problem)
		context = {'pblm':problem,'form': form,'paramdic':paramdic}
		return render(request, 'checksource/editproblemcheck.html', context)
	else:
		form = CheckproblemForm(instance=problem, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('checksource:problemidcheck',kwargs=paramdic))
			
def uploadcheck(request,p_id,checkwhenstart,checkwhenend,checkdepartment,checkway,checkwho,problemdetail,problemtype,problemsolve,whoresponsible,departmentincharge,problemdepartment,departmentwho,problemteam,problemwho,problemreason,projecttype,closewho,ifdone):
	
	problem = Checkproblem.objects.get(id=p_id)
	paramdic={}
	paramdic['p_id']= p_id
	paramdic['checkwhenstart']= checkwhenstart
	paramdic['checkwhenend']=checkwhenend
	paramdic['checkdepartment']=checkdepartment
	paramdic['checkway']=checkway
	paramdic['checkwho']=checkwho
	paramdic['problemdetail']=problemdetail
	paramdic['problemtype']=problemtype
	paramdic['problemsolve']=problemsolve
	paramdic['whoresponsible']=whoresponsible
	paramdic['departmentincharge']=departmentincharge
	paramdic['problemdepartment']=problemdepartment
	paramdic['departmentwho']=departmentwho
	paramdic['problemteam']=problemteam
	paramdic['problemwho']=problemwho
	paramdic['problemreason']=problemreason
	paramdic['projecttype']=projecttype
	paramdic['closewho']=closewho
	paramdic['ifdone']=ifdone
	if request.method != 'POST':
		#form = ImgProblemForm()
		#context = {'form':form,'problem':problem}
		return render(request,'checksource/uploadcheck.html')
	else:
		files = request.FILES.getlist('img',None)
		for f in files:
			form = ImgProblem(img = f)
			form.Checkproblem = problem
			form.save()
		return HttpResponseRedirect(reverse('checksource:problemidcheck',kwargs=paramdic))
		
def problemdoneconfirm(request,p_id,checkwhenstart,checkwhenend,checkdepartment,checkway,checkwho,problemdetail,problemtype,problemsolve,whoresponsible,departmentincharge,problemdepartment,departmentwho,problemteam,problemwho,problemreason,projecttype,closewho,ifdone):
	problem = Checkproblem.objects.get(id=p_id)
	problem.ifdone = True
	problem.save()
	problem = Checkproblem.objects.get(id=p_id)
	paramdic={}
	paramdic['p_id']= p_id
	paramdic['checkwhenstart']= checkwhenstart
	paramdic['checkwhenend']=checkwhenend
	paramdic['checkdepartment']=checkdepartment
	paramdic['checkway']=checkway
	paramdic['checkwho']=checkwho
	paramdic['problemdetail']=problemdetail
	paramdic['problemtype']=problemtype
	paramdic['problemsolve']=problemsolve
	paramdic['whoresponsible']=whoresponsible
	paramdic['departmentincharge']=departmentincharge
	paramdic['problemdepartment']=problemdepartment
	paramdic['departmentwho']=departmentwho
	paramdic['problemteam']=problemteam
	paramdic['problemwho']=problemwho
	paramdic['problemreason']=problemreason
	paramdic['projecttype']=projecttype
	paramdic['closewho']=closewho
	paramdic['ifdone']=ifdone
	return HttpResponseRedirect(reverse('checksource:problemidcheck',kwargs=paramdic))
	
def problemdoneconfirmnew(request,p_id):
	problem = Checkproblem.objects.get(id=p_id)
	problem.ifdone = True
	problem.save()
	return HttpResponseRedirect(reverse('checksource:problemid',args=[p_id]))
	
def deleteproblemcheck(request,p_id,checkwhenstart,checkwhenend,checkdepartment,checkway,checkwho,problemdetail,problemtype,problemsolve,whoresponsible,departmentincharge,problemdepartment,departmentwho,problemteam,problemwho,problemreason,projecttype,closewho,ifdone):
	problem = Checkproblem.objects.get(id=p_id)
	problem.delete()
	paramdic={}
	paramdic['checkwhenstart']= checkwhenstart
	paramdic['checkwhenend']=checkwhenend
	paramdic['checkdepartment']=checkdepartment
	paramdic['checkway']=checkway
	paramdic['checkwho']=checkwho
	paramdic['problemdetail']=problemdetail
	paramdic['problemtype']=problemtype
	paramdic['problemsolve']=problemsolve
	paramdic['whoresponsible']=whoresponsible
	paramdic['departmentincharge']=departmentincharge
	paramdic['problemdepartment']=problemdepartment
	paramdic['departmentwho']=departmentwho
	paramdic['problemteam']=problemteam
	paramdic['problemwho']=problemwho
	paramdic['problemreason']=problemreason
	paramdic['projecttype']=projecttype
	paramdic['closewho']=closewho
	paramdic['ifdone']=ifdone
	return HttpResponseRedirect(reverse('checksource:inquireresult',kwargs=paramdic))

def deleteproblem(request,p_id):
	problem = Checkproblem.objects.get(id=p_id)
	problem.delete()
	return HttpResponseRedirect(reverse('checksource:index')) 
