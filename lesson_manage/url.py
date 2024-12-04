from django.urls import path
from .views import (
    CSStandardListCreateView, CSStandardRetrieveUpdateDestroyView,
    LessonPlanListCreateView, LessonPlanRetrieveUpdateDestroyView,
    LessonPlanStandardListCreateView, LessonPlanStandardRetrieveUpdateDestroyView, ListOfLessonsView
)

urlpatterns = [
    # CSStandard endpoints
    path('cs-standards/', CSStandardListCreateView.as_view(), name='csstandard-list-create'),
    path('cs-standards/<int:pk>/', CSStandardRetrieveUpdateDestroyView.as_view(), name='csstandard-detail'),

    # LessonPlan endpoints
    path('lesson-plans/', LessonPlanListCreateView.as_view(), name='lessonplan-list-create'),
    path('lesson-plans/<int:pk>/', LessonPlanRetrieveUpdateDestroyView.as_view(), name='lessonplan-detail'),

    # LessonPlanStandard endpoints
    path('lesson-plan-standards/', LessonPlanStandardListCreateView.as_view(), name='lessonplanstandard-list-create'),
    path('lesson-plan-standards/<int:pk>/', LessonPlanStandardRetrieveUpdateDestroyView.as_view(), name='lessonplanstandard-detail'),
    path('list-of-lessons/', ListOfLessonsView.as_view(), name='list-of-lessons'),
]
