from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from bsapp.Classification import Classification 

def index(request):
	obj = Classification()
	ds, dsname, names,dt = obj.datasetDetails()
	nr = ds.shape[0]
	nc = ds.shape[1]
	return render(request,'index.html',\
		         {'dsname':dsname,'nc':nc, 'nr':nr,\
		         'names':names,'dt':dt,'nums':range(1,15)})

def dashboard(request):
	return render(request,'dashboard.html')	

def distanalysis(request):
	return render(request,'distanalysis.html')

def distanalysis1(request):
	return render(request,'distanalysis1.html')

def comparison(request):
	return render(request,'comparison.html')

def classification(request):
	obj = Classification()
	res, met = obj.classificationModels()
	return render(request,'classification.html',{'res':res,'met':met,'nums':range(1,7)})	

def dataexplore(request):
	return render(request,'dataexplore.html')			

def datasetOverview(request):
	obj = Classification()
	ds, dsname, names, dt = obj.datasetOverview()
	nr=ds.shape[0]
	nc=ds.shape[1]
	return render(request,'datasetoverview.html',\
		         {'dsname':dsname,'nc':nc,'nr':nr,\
		          'names':names,'dt':dt})

def datasamples(request):
	obj = Classification()
	ds, names = obj.getDatasetLess()
	
	return render(request,'datasamples.html',\
		         {'names':names,'ds':ds.head(20)})	

def datasetDetails(request):
	obj = Classification()
	values=['29 to 79','1, 0','1, 2, 3, 4','94 to 200',\
		'126 to 564','0, 1','0, 1, 2','71 to 202','0, 1','1 to 3','1, 2, 3',\
		'0 to 3','3, 6, 7','0 or 1']	
	desc=['Age of the person in years','Gender of the person [1: Male, 0: Female]\
         ','Chest pain Typical/Angina,Atypical/Angina\
		 Non-angina pain, Asymptomatic','Resting Blood Pressure in mm Hg',\
		 'Serum cholesterol in mg/dl','Fasting Blood Sugar in mg/dl',\
		 'Resting Electrocardiographic Results','Maximum Heart Rate Achieved',\
		 'Exercise Induced Angina','ST depression induced by exercise relative to rest',\
		 'Slope of the Peak Exercise ST segment','Number of major vessels colored by fluoroscopy','Normal, Fixed Defect, Reversible Defect',\
		 'class attribute']
	ds, dsname, names, dt = obj.datasetDetails()
	nr=ds.shape[0]
	nc=ds.shape[1]
	return render(request,'datasetdetails.html',\
		         {'dsname':dsname,'nc':nc,'nr':nr,\
		          'names':names,'dt':dt,'nums':range(1,15),'desc':desc,'values':values})

def statsanalysis(request):
	obj = Classification()
	
	ds, dsname, names, dt = obj.datasetDetails()
	return render(request,'statsanalysis.html',{'ds':ds})

def getpredictions(request):
	obj = Classification()
	results, methods, Y_pred_rf, Y_test,names = obj.getPredictions()
	return render(request, 'predictions.html', {'dp': Y_pred_rf, 'ds':Y_test,'len':len(Y_pred_rf),\
												'len1':len(Y_test),'names':names})