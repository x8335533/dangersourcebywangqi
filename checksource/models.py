from django.db import models

# Create your models here.

class Checkproblem(models.Model):
	"""检查的问题"""
	checkwhen = models.DateField() #DATE,
	checkdepartment = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	checkway = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	checkwho = models.CharField(max_length=30,default='') #varchar(30),
	problemdetail = models.CharField(max_length=3000,default='',null=True,blank=True) #text(3000),
	problemtype = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemsolve = models.CharField(max_length=3000,default='',null=True,blank=True) #text(3000),
	whoresponsible = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	departmentincharge = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemdepartment = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	departmentwho = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemteam = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemwho = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemreason = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	closedate = models.DateField(null=True,blank=True)  #DATE,
	ifdone =models.BooleanField(default=False,null=True,blank=True) #varchar(10),
	projecttype = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	closewho = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	somethingelse = models.CharField(max_length=3000,default='',null=True,blank=True) #text(3000)
	
	"""def __init__(self,form):
		self.checkwhen = form.checkwhen
		self.checkdepartment = form.checkdepartment
		self.checkway = form.checkway
		self.checkwho = form.checkwho
		self.problemdetail = form.problemdetail
		self.problemtype = form.problemtype
		self.problemsolve = form.problemsolve
		self.whoresponsible = form.whoresponsible
		self.departmentincharge = form.departmentincharge
		self.problemdepartment = form.problemdepartment
		self.departmentwho = form.departmentwho
		self.problemteam = form.problemteam
		self.problemwho = form.problemwho
		self.problemreason = form.problemreason
		self.closedate = form.closedate
		self.ifdone = form.ifdone
		self.projecttype = form.projecttype
		self.closewho = form.closewho
		self.somethingelse = form.somethingelse"""

"""以上分别对应：
检查日期---检查部门---检查方式---检查者---问题描述---问题分类---整改措施---部分管责任人---主控部门---责任部门---"部门负责人"---责任班组---"具体责任人"---本部门原因分析---"预计关闭日期"---是否落实---项目分类---关闭批准人---备注；
注：
检查方式：分为现场检查、录像筛查、记录及印证式提问等；
问题分类：违章、违规、作风；
项目分类：在岗履职、监装监卸、车辆运行、搬运、库区管理、现场调度、货运安检。
"""

class Inquireproblem(models.Model):
	"""根据具体条件查询问题"""
	checkwhenstart = models.DateField(null=True,blank=True) #DATE,
	checkwhenend = models.DateField(null=True,blank=True) #DATE,
	checkdepartment = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	checkway = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	checkwho = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemdetail = models.CharField(max_length=3000,default='',null=True,blank=True) #text(3000),
	problemtype = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemsolve = models.CharField(max_length=3000,default='',null=True,blank=True) #text(3000),
	whoresponsible = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	departmentincharge = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemdepartment = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	departmentwho = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemteam = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemwho = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	problemreason = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	closedate = models.DateField(null=True,blank=True)  #DATE,
	ifdone =models.BooleanField(default=None,null=True,blank=True) #varchar(10),
	projecttype = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	closewho = models.CharField(max_length=30,default='',null=True,blank=True) #varchar(30),
	somethingelse = models.CharField(max_length=3000,default='',null=True,blank=True) #text(3000)
	
class ImgProblem(models.Model):
	"""检查出问题的图片"""
	Checkproblem = models.ForeignKey(Checkproblem,on_delete=models.CASCADE)
	img = models.ImageField(upload_to = 'media')
