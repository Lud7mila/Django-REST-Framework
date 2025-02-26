from http.client import HTTPResponse

from django.shortcuts import render

from rest_framework_simplejwt.tokens import RefreshToken

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user) # Создание Refesh и Access
            refresh.payload.update({    # Полезная информация в самом токене
                'user_id': user.id,
                'username': user.username
            })
            return HTTPResponse({
                            'refresh': str(refresh),
                            'access': str(refresh.access_token), # Отправка на клиент
                            }, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        if username is None or password is None:
            return HTTPResponse({'error': 'Нужен и логин, и пароль'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is None:

            return Response({'error': 'Неверные данные'},

                            status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)

        refresh.payload.update({

            'user_id': user.id,

            'username': user.username

        })

        return Response({

            'refresh': str(refresh),

            'access': str(refresh.access_token),

        }, status=status.HTTP_200_OK)