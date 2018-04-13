from django.shortcuts import render
from .models import Earthquake
import json
import datetime
from django.db.models import Sum, Avg, Min, Max

# Create your views here.
def index(request):
	context = {}
	if request.GET:
		context["quakes"] = Earthquake.objects.filter(date__range=[request.GET.get("begin"), request.GET.get("end")])
		context["begin"] = request.GET.get("begin")
		context["end"] = request.GET.get("end")
	else:
		context["quakes"] = Earthquake.objects.all()
		context["begin"] = Earthquake.objects.all().order_by("date")[0].date.strftime("%Y-%m-%d")
		context["end"] = Earthquake.objects.all().order_by("-date")[0].date.strftime("%Y-%m-%d")

	# with open('static/query.json') as data_file:    
	#     data = json.load(data_file)

	# parsed_data = []
	# parsed_data_time = []
	# for i in data["features"]:
	# 	if "kazakhstan" in i["properties"]["place"].lower():
			# parsed_data.append(i)
			# parsed_data_time.append()
			# print(i["geometry"]["coordinates"][0])
			# Earthquake.objects.create(
			# 	date=datetime.datetime.fromtimestamp(round(int(i["properties"]["time"])*0.001)),
			# 	latitude=i["geometry"]["coordinates"][1],
			# 	longitude=i["geometry"]["coordinates"][0],
			# 	depth=i["geometry"]["coordinates"][2],
			# 	magnitude=i["properties"]["mag"]
			# 	)
	# context["data"] = parsed_data_time
	# data = Earthquake.objects.all()

	return render(request, "map.html", context)

def magchart(request):
	context = {}
	years = []
	if request.GET:
		# context["quakes"] = Earthquake.objects.filter(date__range=[request.GET.get("begin")-1, request.GET.get("end")+1])
		for i in range(Earthquake.objects.filter(date__gte=request.GET.get("begin")).order_by("date")[0].date.year-1,Earthquake.objects.filter(date__lte=request.GET.get("end")).order_by("-date")[0].date.year+2):
			if Earthquake.objects.filter(date__year=i).exists():
				years.append({
					"count": Earthquake.objects.filter(date__year=i).count(),
					"mag": list(Earthquake.objects.filter(date__year=i).aggregate(Avg('magnitude')).values())[0],
					"min": list(Earthquake.objects.filter(date__year=i).aggregate(Min('magnitude')).values())[0],
					"max": list(Earthquake.objects.filter(date__year=i).aggregate(Max('magnitude')).values())[0],
					"year": i
				})

		context["data"]=years
		context["begin"] = request.GET.get("begin")
		context["end"] = request.GET.get("end")
	else:
		for i in range(Earthquake.objects.all().order_by("date")[0].date.year-1,Earthquake.objects.all().order_by("-date")[0].date.year+1):
			if Earthquake.objects.filter(date__year=i).exists():
				years.append({
					"count": Earthquake.objects.filter(date__year=i).count(),
					"mag": list(Earthquake.objects.filter(date__year=i).aggregate(Avg('magnitude')).values())[0],
					"min": list(Earthquake.objects.filter(date__year=i).aggregate(Min('magnitude')).values())[0],
					"max": list(Earthquake.objects.filter(date__year=i).aggregate(Max('magnitude')).values())[0],
					"year": i
				})

		context["data"]=years
		context["begin"] = Earthquake.objects.all().order_by("date")[0].date.strftime("%Y-%m-%d")
		context["end"] = Earthquake.objects.all().order_by("-date")[0].date.strftime("%Y-%m-%d")

	return render(request, "mag.html", context)

def freqchart(request):
	context = {}
	years = []
	if request.GET:
		# context["quakes"] = Earthquake.objects.filter(date__range=[request.GET.get("begin")-1, request.GET.get("end")+1])
		for i in range(Earthquake.objects.filter(date__gte=request.GET.get("begin")).order_by("date")[0].date.year-1,Earthquake.objects.filter(date__lte=request.GET.get("end")).order_by("-date")[0].date.year+2):
			if Earthquake.objects.filter(date__year=i).exists():
				years.append({
					"count": Earthquake.objects.filter(date__year=i).count(),
					"mag": list(Earthquake.objects.filter(date__year=i).aggregate(Avg('magnitude')).values())[0],
					"min": list(Earthquake.objects.filter(date__year=i).aggregate(Min('magnitude')).values())[0],
					"max": list(Earthquake.objects.filter(date__year=i).aggregate(Max('magnitude')).values())[0],
					"year": i
				})

		context["data"]=years
		context["begin"] = request.GET.get("begin")
		context["end"] = request.GET.get("end")
	else:
		for i in range(Earthquake.objects.all().order_by("date")[0].date.year-1,Earthquake.objects.all().order_by("-date")[0].date.year+1):
			if Earthquake.objects.filter(date__year=i).exists():
				years.append({
					"count": Earthquake.objects.filter(date__year=i).count(),
					"mag": list(Earthquake.objects.filter(date__year=i).aggregate(Avg('magnitude')).values())[0],
					"min": list(Earthquake.objects.filter(date__year=i).aggregate(Min('magnitude')).values())[0],
					"max": list(Earthquake.objects.filter(date__year=i).aggregate(Max('magnitude')).values())[0],
					"year": i
				})

		context["data"]=years
		context["begin"] = Earthquake.objects.all().order_by("date")[0].date.strftime("%Y-%m-%d")
		context["end"] = Earthquake.objects.all().order_by("-date")[0].date.strftime("%Y-%m-%d")

	return render(request, "freq.html", context)


