from django.contrib import admin
from .models import LessonPlan, CSStandard, LessonPlanStandard, Lesson


# Inline model for LessonPlanStandard
class LessonPlanStandardInline(admin.TabularInline):
    model = LessonPlanStandard
    extra = 1  # Number of empty forms to display for new entries
    autocomplete_fields = ('cs_standard',)  # Autocomplete for standards


# Register the CSStandard model
@admin.register(CSStandard)
class CSStandardAdmin(admin.ModelAdmin):
    list_display = ('standard_id', 'standard', 'grade', 'strand')
    search_fields = ('standard', 'grade', 'strand')


# Register the LessonPlan model with an inline for standards
@admin.register(LessonPlan)
class LessonPlanAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'objectives', 'materials', 'assessment')
    list_filter = ('curricular_barriers', 'environmental_barriers')
    inlines = [LessonPlanStandardInline]  # Use the inline for managing standards


# Register the LessonPlanStandard model
@admin.register(LessonPlanStandard)
class LessonPlanStandardAdmin(admin.ModelAdmin):
    list_display = ('lesson_plan', 'cs_standard', 'additional_info')
    search_fields = ('lesson_plan__title', 'cs_standard__standard', 'additional_info')
    autocomplete_fields = ('lesson_plan', 'cs_standard')  # Autocomplete for related fields

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_number', 'title', 'lesson_plan', 'suggested_format')  # Fields to display in the list view
    list_filter = ('suggested_format',)  # Add filters for better usability
    search_fields = ('lesson_number', 'title')  # Allow searching by lesson number or title
    ordering = ('lesson_number',)  # Order by lesson number