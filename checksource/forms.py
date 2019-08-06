from django import forms
from .models import Checkproblem,Inquireproblem,ImgProblem
from bootstrap_datepicker_plus import DateTimePickerInput

checkwaylist =(('', ''),('现场检查', '现场检查'),('录像筛查', '录像筛查'),('记录及印证式提问', '记录及印证式提问'))
protypelist = (('', ''),('违章', '违章'),('违规', '违规'),('作风', '作风'))
ifdonelist = ((None,'所有'),(True,'是' ),(False,'否' ))
class CheckproblemForm(forms.ModelForm):  #新增检查的表单
	class Meta:
		model = Checkproblem   #根据哪个模型创造的表单
		   #表单中包含的字段
		exclude = ['ifdone']
		labels = {'checkwhen':"检查日期",'checkdepartment': '检查部门','checkway':'检查方式','checkwho':'检查者','problemdetail':'问题描述','problemtype':'问题分类','problemsolve':'整改措施','whoresponsible':'部分管责任人','departmentincharge':'主控部门','problemdepartment':'责任部门','departmentwho':'部门负责人','problemteam':'责任班组','problemwho':'具体责任人','problemreason':'本部门原因分析','closedate':'预计关闭日期','projecttype':'项目分类','closewho':'关闭批准人','somethingelse':'备注',}
		widgets = {'checkwhen':DateTimePickerInput(
		options={"format": "YYYY-MM-DD","locale":"zh-cn",}),
		'checkway':forms.Select(choices=checkwaylist),
		'problemtype':forms.Select(choices=protypelist),
		'closedate':DateTimePickerInput(
		options={"format": "YYYY-MM-DD","locale":"zh-cn",}),
		'problemdetail': forms.Textarea(attrs={'cols': 40,'rows':3}),#
		'problemsolve': forms.Textarea(),#attrs={'cols': 40,'rows':3}
		'problemreason': forms.Textarea(),#attrs={'cols': 40,'rows':3}
		}
		
class InquireForm1(forms.Form):		  #查询具体条件的表单
	datestart = forms.DateField(widget=DateTimePickerInput(options={
	"format": "YYYY-MM-DD", # moment date-time format
	"showClose": False,
	"showClear": False,
	"showTodayButton": False,
	"locale":"zh-cn",
	}),label='检查起始日期')
	
	dateend = forms.DateField(widget=DateTimePickerInput(options={
	"format": "YYYY-MM-DD", # moment date-time format
	"showClose": False,
	"showClear": False,
	"showTodayButton": False,
	"locale":"zh-cn",
	}),label='检查终止日期')
	
	checkdepartment = forms.CharField(label='检查部门')
	checkway = forms.CharField(max_length=10,widget=forms.widgets.Select(choices=checkwaylist),label='检查方式')
	problemcontain = forms.CharField(label='问题包含')

class InquireForm(forms.ModelForm):  #新增检查的表单
	class Meta:
		model = Inquireproblem   #根据哪个模型创造的表单
		   #表单中包含的字段
		exclude = ['somethingelse','closedate']
		labels = {'checkwhenstart':"起始日期",'checkwhenend':"终止日期",'checkdepartment': '检查部门','checkway':'检查方式','checkwho':'检查者','problemdetail':'问题描述包含','problemtype':'问题分类','problemsolve':'整改措施包含','whoresponsible':'部分管责任人','departmentincharge':'主控部门','problemdepartment':'责任部门','departmentwho':'部门负责人','problemteam':'责任班组','problemwho':'具体责任人','problemreason':'本部门原因分析','closedate':'预计关闭日期','projecttype':'项目分类','closewho':'关闭批准人','ifdone':'是否已整改','somethingelse':'备注',}
		widgets = {'checkwhenstart':DateTimePickerInput(
		options={"format": "YYYY-MM-DD","locale":"zh-cn",}),
		'checkwhenend':DateTimePickerInput(
		options={"format": "YYYY-MM-DD","locale":"zh-cn",}),
		'checkway':forms.Select(choices=checkwaylist),
		'problemtype':forms.Select(choices=protypelist),
		'ifdone':forms.Select(choices=ifdonelist),
		'closedate':DateTimePickerInput(
		options={"format": "YYYY-MM-DD","locale":"zh-cn",}),
		}
		
class ImgProblemForm(forms.ModelForm):
	class Meta:
		model = ImgProblem
		fields = {'img'}		
