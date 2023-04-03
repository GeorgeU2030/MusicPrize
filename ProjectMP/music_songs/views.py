from django.shortcuts import render
from django.db.models import Max
from music_songs.models import Song
from music_songs.models import Singer
# Create your views here.

def showindex(request):

    max_number = Singer.objects.aggregate(Max('points'))['points__max']  # Returns the highest number.
    max_users = Singer.objects.filter(points=max_number)
    data = {'songs':max_users}
    return render(request,'index.html',data)
    
    

def showaddsong(request):
    return render(request, 'addsong.html' );

def showaddsing(request):
    return render(request, 'addsinger.html' );

def showadd(request):
    return render(request, 'addpoints.html' );

def registersong(request):
    if request.method == 'POST':
        name = request.POST['txtnom']
        try:
            sing1 = request.POST['txtsing1']
        except:
            sing1 = ""
        
        try:
            sing2 = request.POST['txtsing2']
        except:
            sing2=""

        sing3 = request.POST['txtsing3']
     

        typesong = request.POST['txttype']
        tweek1 = request.POST['txtweek1']

        tweek2 = request.POST['txtweek2']
        try:
            ppicture = request.FILES['txtfot']
        except:
            ppicture = "imagebd/whiteimage.png"

        song = Song(namesong = name,singer1=sing1,singer2=sing2,singer3=sing3,typeSong = typesong,week1=tweek1,week2=tweek2,picture=ppicture)
        song.save()

        singer1 = Singer.objects.get(name=sing1)
        cpoints =0
        if typesong == 'C':
            cpoints=55
        elif typesong == 'B':
            cpoints=60
        elif typesong == 'B+':
            cpoints=65
        elif typesong == 'A':
            cpoints=75
        elif typesong == 'A+':
            cpoints=90
        
        singer1.points = singer1.points+cpoints
        singer1.awards = singer1.awards+1
        singer1.save()

        if sing2 != '':
            singer2 = Singer.objects.get(name=sing2)
            cpoints =0
            if typesong == 'C':
                cpoints=55
            elif typesong == 'B':
                cpoints=60
            elif typesong == 'B+':
                cpoints=65
            elif typesong == 'A':
                cpoints=75
            elif typesong == 'A+':
                cpoints=90
        
            singer2.points = singer2.points+cpoints
            singer2.awards = singer2.awards+1
            singer2.save()

        if sing3 != '':
            singer3 = Singer.objects.get(name=sing3)
            cpoints =0
            if typesong == 'C':
                cpoints=55
            elif typesong == 'B':
                cpoints=60
            elif typesong == 'B+':
                cpoints=65
            elif typesong == 'A':
                cpoints=75
            elif typesong == 'A+':
                cpoints=90
        
            singer3.points = singer3.points+cpoints
            singer3.awards = singer3.awards+1
            singer3.save()

        data = {'r': 'Song has been registered succesfully'}
        return render(request, 'addsong.html', data)
    
    else:
        data = {'r2' : 'Request Failed'}
        return render(request, 'addsong.html', data)

def registerSinger(request):
    if request.method == 'POST':
        nam = request.POST['txtnom']
        countr = request.POST['txtcount']
        try:
            pphoto = request.FILES['txtfot']
        except:
            pphoto = "imagebd/whiteimage.png"

        try:
            ppflag = request.FILES['txtcountry']
        except:
            ppflag = "imagebd/whiteimage.png"

        singer = Singer(name=nam,country=countr,photo=pphoto,flag=ppflag,points=0,awards=0,position=0)
        singer.save()
        data = {'r': 'Singer has been registered succesfully'}
        return render(request, 'addsinger.html', data)
    else:
        data = {'r2' : 'Request Failed'}
        return render(request, 'addsinger.html', data)
            

def showlistsong(request):
    songs = Song.objects.all().values().order_by('-week2')
    data = {'songs': songs}
    return render(request, 'listsong.html',data );


def showranking(request):
    singerAr = Singer.objects.all().order_by('-points')
    i=1
    for x in singerAr:
        x.position = i
        x.save()
        i=i+1

    singers = Singer.objects.all().values().order_by('-points')
    data = {'singers': singers}
    return render(request, 'ranking.html',data );


def showawards(request):
    singerAr = Singer.objects.all().order_by('-awards')
    i=1
    for x in singerAr:
        x.position = i
        x.save()
        i=i+1

    singers = Singer.objects.all().values().order_by('-awards')
    data = {'singers': singers}
    return render(request, 'awards.html',data );
        
def pointadd(request):
    if request.method == 'POST':
        sing1 = request.POST['txtn']
        po = request.POST['txttype']
        try:
            if(po=='Singer Month'):
                p = 100
                singer1 = Singer.objects.get(name=sing1)
                singer1.points = singer1.points+p
                singer1.save()
                data = {'r': 'The points has been added succesfully'}
                return render(request, 'addpoints.html', data)
            elif po =='2nd Week':
                p = 20
                singer1 = Singer.objects.get(name=sing1)
                singer1.points = singer1.points+p
                singer1.save()
                data = {'r': 'The points has been added succesfully'}
                return render(request, 'addpoints.html', data)
            elif po =='3rd Week':
                p = 30
                singer1 = Singer.objects.get(name=sing1)
                singer1.points = singer1.points+p
                singer1.save()
                data = {'r': 'The points has been added succesfully'}
                return render(request, 'addpoints.html', data)
            elif po =='4th Week':
                p = 50
                singer1 = Singer.objects.get(name=sing1)
                singer1.points = singer1.points+p
                singer1.save()
                data = {'r': 'The points has been added succesfully'}
                return render(request, 'addpoints.html', data)
        except:
            data = {'r2' : 'Request Failed'}
            return render(request, 'addpoints.html', data)
    
    else:
        data = {'r2' : 'Request Failed'}
        return render(request, 'addpoints.html', data)

