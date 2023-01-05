from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        print('GET()으로 호출!!!')
        return render(request, 'clarustagram/main.html')

    def post(self, request):
        print('POST()로 호출!!!')
        render(request, 'clarustagram/main.html')