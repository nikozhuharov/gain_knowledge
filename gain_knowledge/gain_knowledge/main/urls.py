from django.urls import path

from gain_knowledge.main.views import show_home, show_profile, create_profile, edit_profile, \
    delete_profile, CategoryListView, CourseDetailView, list_courses, list_tests, display_question, final_score

urlpatterns = [
    path('', show_home, name='index'),
    path('categories/', CategoryListView.as_view(), name='list categories'),
    path('categories/<int:pk>', list_courses, name='list courses'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='courses details'),
    path('tests/<int:pk>', list_tests, name='list tests'),
    path('question/<int:pk>', display_question, name='display question'),
    path('final_score/', final_score, name='final score'),


    path('profile/', show_profile, name='profile details'),
    path('profile/create', create_profile, name='create profile'),
    path('profile/edit', edit_profile, name='edit profile'),
    path('profile/delete', delete_profile, name='delete profile'),
]