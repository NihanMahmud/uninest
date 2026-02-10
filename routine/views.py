# routine/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from auth_management.models import Student
from .models import Class, Lab

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_schedule(request):
    try:
        # Decode JWT manually to get student info
        auth_header = request.headers.get('Authorization', None)
        if not auth_header:
            return Response({"error": "Authorization header missing"}, status=401)

        token_str = auth_header.split()[1]  # 'Bearer <token>'
        auth = JWTAuthentication()
        validated_token = auth.get_validated_token(token_str)

        roll_number = validated_token['roll_number']
        name = validated_token['name']
        section = validated_token['section']

        # Fetch classes and labs
        classes = list(Class.objects.filter(section=section['main']).values(
            'date', 'time', 'teacher', 'course', 'credit', 'assignment'
        ))
        labs = list(Lab.objects.filter(lab_group=section['sub']).values(
            'date', 'time', 'teacher', 'course', 'credit'
        ))

        return Response({
            "student": name,
            "roll_number": roll_number,
            "section": section,
            "classes": classes,
            "labs": labs
        })

    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
