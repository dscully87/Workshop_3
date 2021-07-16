from django.urls import path
from roughwork.views import WorkshopCreateView, WorkshopDetailView, WorkshopListView, WorkshopUpdateView, WorkshopDeleteView

app_name = 'workshops'

urlpatterns = [
    path('', WorkshopListView.as_view(), name='workshop-list'),
    path('create/', WorkshopCreateView.as_view(), name='workshop-create'),
    path('<int:pk>/', WorkshopDetailView.as_view(), name='workshop-detail'),
    path('<int:pk>/update/', WorkshopUpdateView.as_view(), name='workshop-update'),
    path('<int:pk>/delete/', WorkshopDeleteView.as_view(), name='workshop-delete'),
]
