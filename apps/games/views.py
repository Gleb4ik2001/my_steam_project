# Python
import uuid

# Django
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
from django.db.models.functions import Lower
from django.views.generic import View
from django.core.files.uploadedfile import InMemoryUploadedFile

# Local
from .models import Game, Genre, Company ,AdditionalGamesPhotos


class AddScreenshotsToGameView(View):
    def get(self,request):
        template_name = 'games/add_scrinshots_to_game.html'
        return render(
            request=request,
            template_name=template_name,
            context={}
        )
    def post(self,request:HttpRequest):
        game_id:int = request.POST.get('game_id')
        try:   
            game :Game = Game.objects.get(pk = game_id)
        except Game.DoesNotExist:
            return HttpResponse('<h1>Игры с указанным ID не существует в БД')
        image :InMemoryUploadedFile = None
        if request.FILES !={}:
            image = request.FILES.get('image')
            image.name = f'{uuid.uuid1()}.png'
        additional_img:AdditionalGamesPhotos = AdditionalGamesPhotos(
            game= game,
            img= image
        )
        additional_img.save()
        return HttpResponse('<h1>Загрузка дополнительного фото прошла успешно')
    
        
    
class MainView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'games/index.html'
        return render(
            request=request,
            template_name=template_name,
            context={}
        )
    

class CompanyView(View):
    
        def get(self, request: HttpRequest, company_id: int) -> HttpResponse:
            try:
                company: Company = Company.objects.get(id=company_id)
            except Company.DoesNotExist as e:
                return HttpResponse(
                    f'<h1>Компании с id {company_id} не существует!</h1>'
                )
            return render(
                request=request,
                template_name='games/company.html',
                context={
                    'company': company
                }
            )
class CompanyListView(View):
    def get(self,request):
        companys :QuerySet[Company] = Company.objects.all().order_by('name')
        template_name = 'games/companys.html'
        return render(
            request=request,
            template_name=template_name,
            context={
                'companys':companys
            }
        )



class GameListView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'games/game_list.html'
        queryset: QuerySet[Game] = Game.objects.all().order_by('-id')
        genres: QuerySet[Genre] = Genre.objects.all()
        return render(
            request=request,
            template_name=template_name,
            context={
                'games': queryset,
                'genres': genres
            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        data: dict = request.POST
        files: dict = request.FILES
        # breakpoint()

        image: InMemoryUploadedFile = None
        if files != {}:
            image = files.get('img_input')
            image.name = f'{uuid.uuid1()}.png'

        try:
            company: Company = Company.objects.annotate(lower_igor=Lower('name')).get(lower_igor=str(data.get('company_input')).lower())
        except Company.DoesNotExist:
            return HttpResponse(
                f"Компании {data.get('company_input')} не существует"
            )
        
        game: Game = Game.objects.create(
            name=data.get('game_input'),
            price=float(data.get('price_input')),
            datetime_created=data.get('date_input'),
            company=company,
            main_img=image
        )

        key: str
        for key in data:
            if 'genre_' in key:
                genre: Genre = Genre.objects.get(
                    id=int(key.strip('genre_'))
                )
                game.genres.add(genre)

        game.save()
        return HttpResponse("Hello")

class GameView(View):

    def get(self, request: HttpRequest, game_id: int) -> HttpResponse:
        try:
            game: Game = Game.objects.get(id=game_id)
            additional_photos :AdditionalGamesPhotos = AdditionalGamesPhotos.objects.filter(game=game_id)

        except Game.DoesNotExist as e:
            return HttpResponse(
                f'<h1>Игры с id {game_id} не существует!</h1>'
            )
        except AdditionalGamesPhotos.DoesNotExist as e:
            pass
        return render(
            request=request,
            template_name='games/store-product.html',
            context={
                'game': game ,
                'additional_images':additional_photos
            }
        )
    
def about(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/about.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )

