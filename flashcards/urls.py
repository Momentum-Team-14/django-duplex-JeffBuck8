from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_subject, name='list_subject'),
    path('subject/new/', views.subject_new, name='subject_new'),
    path('subject/edit/<int:pk>', views.subject_edit, name='subject_edit'),
    path('delete_subject/<int:pk>', views.delete_subject, name='delete_subject'),
    path('card_questions/<int:pk>', views.card_questions, name='card_questions'),
    path('card_answer/<int:pk1>', views.card_answer, name='card_answer'),
    path('flashcard/new/<int:pk>', views.card_new, name='card_new'),
    path('flashcard/edit/<int:pk1>/<int:pk2>', views.card_edit, name='card_edit'),
    path('delete_card/<int:pk1>/<int:pk2>', views.delete_card, name='delete_card'),
]