from rest_framework import generics
from rest_framework.generics import ListAPIView

from .models import CSStandard, Lesson
from .serializer import CSStandardSerializer, LessonPlanSerializer, LessonSummarySerializer
from .models import LessonPlan,LessonPlanStandard
from .serializer import LessonPlanStandardSerializer


class CSStandardListCreateView(generics.ListCreateAPIView):
    queryset = CSStandard.objects.all()
    serializer_class = CSStandardSerializer


class CSStandardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CSStandard.objects.all()
    serializer_class = CSStandardSerializer


class LessonPlanListCreateView(generics.ListCreateAPIView):
    queryset = LessonPlan.objects.all()
    serializer_class = LessonPlanSerializer


class LessonPlanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LessonPlan.objects.all()
    serializer_class = LessonPlanSerializer

class LessonPlanStandardListCreateView(generics.ListCreateAPIView):
    queryset = LessonPlanStandard.objects.all()
    serializer_class = LessonPlanStandardSerializer


class LessonPlanStandardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LessonPlanStandard.objects.all()
    serializer_class = LessonPlanStandardSerializer

class ListOfLessonsView(ListAPIView):
    """
    API endpoint to show a summary of all lessons in the system.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSummarySerializer