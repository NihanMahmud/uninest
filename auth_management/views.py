from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def login(request):
    roll_number = request.data.get('roll_number')
    password = request.data.get('password')

    try:
        student = Student.objects.get(roll_number=roll_number)

        if not student.check_password(password):
            return Response({"error": "Invalid credentials"}, status=401)

        # Create JWT tokens
        refresh = RefreshToken.for_user(student)
        access_token = str(refresh.access_token)

        refresh['roll_number'] = student.roll_number
        refresh['name'] = student.name

        tokens = get_tokens_for_student(student)

        return Response({
            "access": tokens['access'],
            "refresh": tokens['refresh'],
            "name": student.name
        }, status=200)

    except Student.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=401)

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_student(student):
    refresh = RefreshToken.for_user(student)

    # Add roll number, name, section into the token
    refresh['roll_number'] = student.roll_number
    refresh['name'] = student.name
    refresh['section']=student.get_section()

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }
