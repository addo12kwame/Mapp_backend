from django.db import models

class CSStandard(models.Model):
    standard_id = models.AutoField(primary_key=True)
    standard = models.CharField(max_length=255)  # Description of the standard
    grade = models.CharField(max_length=50)  # Grade level
    strand = models.TextField()  # Educational strand/category

    def __str__(self):
        return "standard: "+ self.standard + "; grade: " + self.grade + "; strand: " + self.strand




class LessonPlan(models.Model):
    title = models.CharField(max_length=255)  # Title of the lesson plan
    description = models.TextField(blank=True, null=True) # Short description of the lesson plan
    objectives = models.TextField(blank=True, null=True) # Objectives for the lesson
    materials = models.TextField(blank=True, null=True)  # Materials required for the lesson plan
    links = models.TextField(blank=True, null=True)  # Links to external resources
    assessment = models.TextField(blank=True, null=True)  # Assessment methods
    curricular_barriers = models.TextField(blank=True, null=True)  # Challenges in the curriculum
    environmental_barriers = models.TextField(blank=True, null=True)  # Environmental challenges
    options_for_engagement = models.TextField(blank=True, null=True)  # Strategies for engaging students
    options_for_representation = models.TextField(blank=True, null=True)  # Representation strategies
    options_for_action_and_expression = models.TextField(blank=True, null=True)  # Ways for action and expression
    iep_goals = models.TextField(blank=True, null=True)  # Goals for Individualized Education Programs
    scripting_of_lesson = models.TextField(blank=True, null=True)  # Detailed lesson script
    notes = models.TextField(blank=True, null=True)  # Additional notes
    suggested_format = models.CharField(max_length=255, blank=True, null=True)  # Suggested format (e.g., "Hybrid In-Class")
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates

    def __str__(self):
        return self.title

class Lesson(models.Model):
    lesson_plan = models.ForeignKey(
        LessonPlan, on_delete=models.CASCADE, related_name='lessons'
    )  # Link lessons to a specific lesson plan
    lesson_number = models.CharField(max_length=20)  # "Lesson 1", "Lesson 2", etc.
    title = models.CharField(max_length=255)  # Title of the lesson
    description = models.TextField(blank=True, null=True)  # Description of the lesson
    link = models.URLField(blank=True, null=True)  # Link to lesson resources
    suggested_format = models.CharField(max_length=255, blank=True, null=True)  # Suggested format
    notes = models.TextField(blank=True, null=True)  # Additional notes

    def __str__(self):
        return f"{self.lesson_number}: {self.title}"


class LessonPlanStandard(models.Model):
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE, related_name="lesson_standards")
    cs_standard = models.ForeignKey(CSStandard, on_delete=models.CASCADE, related_name="lesson_standards")
    additional_info = models.TextField(blank=True, null=True)  # Optional metadata for the association

    class Meta:
        unique_together = ('lesson_plan', 'cs_standard')  # Ensure unique associations

    def __str__(self):
        return f"{self.lesson_plan.title} - {self.cs_standard.standard}"

class User(models.Model):
    pass
