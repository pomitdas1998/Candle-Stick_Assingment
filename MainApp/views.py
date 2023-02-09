from django.shortcuts import render,HttpResponse
from .models import*
import pandas as pd


# Create your views here.

#Store the data present in the file in the python list of candle objects.
def create_db(file_path,time_intervals):
    df = pd.read_csv(file_path , delimiter=",")
    list_of_csv = [list(row) for row in df.values]

    for l in list_of_csv:
        Candle.objects.create(
            Index_name = l[0],
            date = l[1],
            time = l[2],
            open = l[3],
            high = l[4],
            low = l[5],
            close = l[6],
            volume = l[7],        
        )

#view data function
# def View_all_data(request):
#     candle = Candle.objects.all().values()
#     context = {
#          'candle' : candle
#             }

#     return render(request,'View.html',context)

#get timeInterval and converting list of candles that will be one minute into a given timeframe
def get_timeinterval(request):
    if request.method == "POST":
        intervals = request.POST['timeInterval']

    candle = Candle.objects.all().values()

    context = {
         'candle' : candle
            }
        
#logic for convertng the list of candles that will be one minute into a given timeframe
    df = pd.DataFrame(candle)[["time","open","high","low", "close", "volume"]]

    df["Dates"] = pd.to_datetime(df["time"])

    df.set_index("Dates",inplace =True)

    df = df.resample(intervals+'min').agg({
    "time":"last",
    "open":"first",
    "high":"max",
    "low":"min",
    "close":"last",
    "volume":"sum"
    })

#upload data in json format
    json = df.to_json('json_file.json',indent =1,orient="records")
    print(df,'__________________________json_____________________')

    return render( request,'index.html')

#get file and upload in Files folder
def index(request):
    if request.method =="POST":
        file =request.FILES['file']
        # time_intervals = request.POST.get('time_interval')
        time_intervals = request.POST.get("time_intervals")

        obj = File.objects.create(file = file)

        create_db(obj.file,time_intervals)

    return render(request,'index.html')
