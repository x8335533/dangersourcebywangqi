from django.urls import path,re_path,include
from . import views

urlpatterns = [
    #主页
    path('', views.index, name='index'),
    #所有数据
    path('allproblems/', views.allproblems, name='allproblems'),
    #添加新数据
    path('newproblem/', views.newproblem, name='newproblem'),
    #编辑数据
    path('editproblem/(?P<problem_id>\d+)/', views.editproblem, name='editproblem'),
    #查询条件输入
    path('inquireinput/',views.inquireinput,name='inquireinput'),
    #查询条件输出
    path('inquireresult/&&(?P<checkwhenstart>\.*?)&&(?P<checkwhenend>\.*?)&&(?P<checkdepartment>\.*?)&&(?P<checkway>\.*?)&&(?P<checkwho>\.*?)&&(?P<problemdetail>\.*?)&&(?P<problemtype>\.*?)&&(?P<problemsolve>\.*?)&&(?P<whoresponsible>\.*?)&&(?P<departmentincharge>\.*?)&&(?P<problemdepartment>\.*?)&&(?P<departmentwho>\.*?)&&(?P<problemteam>\.*?)&&(?P<problemwho>\.*?)&&(?P<problemreason>\.*?)&&(?P<projecttype>\.*?)&&(?P<closewho>\.*?)&&(?P<ifdone>\.*?)&&/',views.inquireresult,name='inquireresult'),
    
    #上传图片
    path('upload/(?P<problem_id>\d+)/',views.upload,name='upload'),
    #删除图片
    path('/deleteimg/(?P<img_id>\d+)/',views.deleteimg,name= 'deleteimg'),
    #根据主键ID查询
    path('problemid/(?P<p_id>\d+)/', views.problemid, name='problemid'),
    #查询列表修改某条数据，与problemid基本一致，只是多了返回查询的列表
    path('problemidcheck/(?P<p_id>\d+)&&(?P<checkwhenstart>\.*?)&&(?P<checkwhenend>\.*?)&&(?P<checkdepartment>\.*?)&&(?P<checkway>\.*?)&&(?P<checkwho>\.*?)&&(?P<problemdetail>\.*?)&&(?P<problemtype>\.*?)&&(?P<problemsolve>\.*?)&&(?P<whoresponsible>\.*?)&&(?P<departmentincharge>\.*?)&&(?P<problemdepartment>\.*?)&&(?P<departmentwho>\.*?)&&(?P<problemteam>\.*?)&&(?P<problemwho>\.*?)&&(?P<problemreason>\.*?)&&(?P<projecttype>\.*?)&&(?P<closewho>\.*?)&&(?P<ifdone>\.*?)&&/', views.problemidcheck, name='problemidcheck'),
    #编辑数据,根据查询后点击的id和查询参数再返回
    path('editproblemcheck/(?P<p_id>\d+)&&(?P<checkwhenstart>\.*?)&&(?P<checkwhenend>\.*?)&&(?P<checkdepartment>\.*?)&&(?P<checkway>\.*?)&&(?P<checkwho>\.*?)&&(?P<problemdetail>\.*?)&&(?P<problemtype>\.*?)&&(?P<problemsolve>\.*?)&&(?P<whoresponsible>\.*?)&&(?P<departmentincharge>\.*?)&&(?P<problemdepartment>\.*?)&&(?P<departmentwho>\.*?)&&(?P<problemteam>\.*?)&&(?P<problemwho>\.*?)&&(?P<problemreason>\.*?)&&(?P<projecttype>\.*?)&&(?P<closewho>\.*?)&&(?P<ifdone>\.*?)&&/', views.editproblemcheck, name='editproblemcheck'),
    #上传图片,根据查询后点击的id和查询参数再返回
    path('uploadcheck/(?P<p_id>\d+)&&(?P<checkwhenstart>\.*?)&&(?P<checkwhenend>\.*?)&&(?P<checkdepartment>\.*?)&&(?P<checkway>\.*?)&&(?P<checkwho>\.*?)&&(?P<problemdetail>\.*?)&&(?P<problemtype>\.*?)&&(?P<problemsolve>\.*?)&&(?P<whoresponsible>\.*?)&&(?P<departmentincharge>\.*?)&&(?P<problemdepartment>\.*?)&&(?P<departmentwho>\.*?)&&(?P<problemteam>\.*?)&&(?P<problemwho>\.*?)&&(?P<problemreason>\.*?)&&(?P<projecttype>\.*?)&&(?P<closewho>\.*?)&&(?P<ifdone>\.*?)&&/', views.uploadcheck, name='uploadcheck'),
    #整改完毕确认返回查询列表
    path('problemdoneconfirm/(?P<p_id>\d+)&&(?P<checkwhenstart>\.*?)&&(?P<checkwhenend>\.*?)&&(?P<checkdepartment>\.*?)&&(?P<checkway>\.*?)&&(?P<checkwho>\.*?)&&(?P<problemdetail>\.*?)&&(?P<problemtype>\.*?)&&(?P<problemsolve>\.*?)&&(?P<whoresponsible>\.*?)&&(?P<departmentincharge>\.*?)&&(?P<problemdepartment>\.*?)&&(?P<departmentwho>\.*?)&&(?P<problemteam>\.*?)&&(?P<problemwho>\.*?)&&(?P<problemreason>\.*?)&&(?P<projecttype>\.*?)&&(?P<closewho>\.*?)&&(?P<ifdone>\.*?)&&/',views.problemdoneconfirm,name='problemdoneconfirm'),
    #整改完毕确认
    path('problemdoneconfirmnew/(?P<p_id>\d+)/',views.problemdoneconfirmnew,name='problemdoneconfirmnew'),
    #删除图片返回列表
    path('deleteproblemcheck/(?P<p_id>\d+)&&(?P<checkwhenstart>\.*?)&&(?P<checkwhenend>\.*?)&&(?P<checkdepartment>\.*?)&&(?P<checkway>\.*?)&&(?P<checkwho>\.*?)&&(?P<problemdetail>\.*?)&&(?P<problemtype>\.*?)&&(?P<problemsolve>\.*?)&&(?P<whoresponsible>\.*?)&&(?P<departmentincharge>\.*?)&&(?P<problemdepartment>\.*?)&&(?P<departmentwho>\.*?)&&(?P<problemteam>\.*?)&&(?P<problemwho>\.*?)&&(?P<problemreason>\.*?)&&(?P<projecttype>\.*?)&&(?P<closewho>\.*?)&&(?P<ifdone>\.*?)&&/',views.deleteproblemcheck,name='deleteproblemcheck'),
    #删除图片
    path('deleteproblem/(?P<p_id>\d+)/',views.deleteproblem,name='deleteproblem'),
    
    
    
]
