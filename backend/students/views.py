from .models import Student
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer



class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    



    
        
    
