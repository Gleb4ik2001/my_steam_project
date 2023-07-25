from django.urls import path

# Local
from .views import GameView, about, GameListView, MainView ,CompanyView,CompanyListView ,AddScreenshotsToGameView


urlpatterns = [
    path('<int:game_id>/', GameView.as_view(),name='game_id'),
    path('list/', GameListView.as_view(),name='game_list'),
    path('', MainView.as_view(),name='main'),
    path('about/', about , name='about'),
    path('company/<int:company_id>/', CompanyView.as_view(),name='company'),
    path('companys/',CompanyListView.as_view(),name='companys'),
    path('add_screenshots_to_game', AddScreenshotsToGameView.as_view(),name='add_screenshots')
]
