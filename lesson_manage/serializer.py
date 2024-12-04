from rest_framework import serializers
from .models import LessonPlan, CSStandard, LessonPlanStandard, Lesson


class CSStandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSStandard
        fields = ['standard_id', 'standard', 'grade', 'strand']


class LessonPlanStandardSerializer(serializers.ModelSerializer):
    cs_standard = CSStandardSerializer()

    class Meta:
        model = LessonPlanStandard
        fields = ['lesson_plan', 'cs_standard', 'additional_info']


class LessonPlanSerializer(serializers.ModelSerializer):
    standards = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )  # Allow linking standards via IDs
    associated_standards = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = LessonPlan
        fields = [
            'id', 'title', 'description', 'objectives', 'materials', 'links', 'assessment',
            'curricular_barriers', 'environmental_barriers',
            'options_for_engagement', 'options_for_representation',
            'options_for_action_and_expression', 'iep_goals',
            'scripting_of_lesson', 'notes', 'suggested_format', 'standards', 'associated_standards'
        ]

    def get_associated_standards(self, obj):
        lesson_plan_standards = LessonPlanStandard.objects.filter(lesson_plan=obj)
        return [
            {
                "standard_id": lps.cs_standard.standard_id,
                "standard": lps.cs_standard.standard,
                "grade": lps.cs_standard.grade,
                "strand": lps.cs_standard.strand,
            }
            for lps in lesson_plan_standards
        ]

    def create(self, validated_data):
        # Extract standards from validated data
        standards = validated_data.pop('standards', [])
        # Create the lesson plan
        lesson_plan = LessonPlan.objects.create(**validated_data)
        # Link standards to the lesson plan
        for standard_id in standards:
            cs_standard = CSStandard.objects.get(standard_id=standard_id)
            LessonPlanStandard.objects.create(lesson_plan=lesson_plan, cs_standard=cs_standard)

        # Dynamically generate lessons based on the lesson plan data
        Lesson.objects.create(
            lesson_plan=lesson_plan,
            lesson_number=f"Lesson-{lesson_plan.id}",  # Use the primary key as the lesson number
            title=lesson_plan.title,  # Use the title from the LessonPlan
            description=lesson_plan.description,  # Use the description from the LessonPlan
            link=lesson_plan.links,  # Use the links from the LessonPlan
            suggested_format=lesson_plan.suggested_format,  # Use the suggested format from the LessonPlan
            notes=lesson_plan.notes  # Use the notes from the LessonPlan
        )

        return lesson_plan



class LessonSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['lesson_number', 'title', 'description', 'link', 'suggested_format', 'notes']

