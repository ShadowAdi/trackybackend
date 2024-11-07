from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Account
from .serializer import AccountSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
def Login(request):
    user = get_object_or_404(Account, email=request.data["email"])
    if not user.check_password(request.data["password"]):
        return Response(
            {"detail": "Password Not Match"}, status=status.HTTP_404_NOT_FOUND
        )
    token, created = Token.objects.get_or_create(user=user)
    serializer = AccountSerializer(instance=user)
    return Response(
        {"token": token.key, "data": serializer.data, "message": "LoggedIn"}
    )


@api_view(["POST"])
def Register(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = Account.objects.get(email=request.data["email"])
        user.set_password(request.data["password"])
        user.save()
        return Response({"message": "User Created", "data": serializer.data})
    else:
        print("Validation errors:", serializer.errors)  # Log validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def GetToken(request):
    serializer = AccountSerializer(instance=request.user)
    return Response({"user": serializer.data})


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        # Get the token from the request user
        request.user.auth_token.delete()
        return Response(
            {"message": "Logged out successfully"}, status=status.HTTP_200_OK
        )
    except AttributeError:
        return Response(
            {"error": "User is not logged in"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def create(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_users(request):

    users = Account.objects.all()
    serializers = AccountSerializer(users, many=True)
    return Response(serializers.data)


@api_view(["GET", "PUT", "DELETE"])
def get_user(request, pk):
    try:
        user = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AccountSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = AccountSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def UpdateUser(request, pk):
    try:
        user = Account.objects.get(pk=pk)
        if request.method == "PUT":
            serializer = AccountSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
