from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.db.models import F
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


def redirect_to_api(request):
    return redirect('api/')


@api_view(['GET'])
def api_list(request):
    """
    View for /api/ urls.
    It is used to handle GET requests for listing all objects.
    Requires no authorisation to handle requests.
    :param request: GET request
    :return: JsonResponse - contains all objects
    """
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_retrieve(request, pk):
    """
    Public view requiring no authentication, used for /api/id/ urls, where id is specific id number.
    It is used to handle GET requests for retrieving specific object.
    POST, PUT and DELETE requests are possible to be sent trough this api, altough
    user will receive text response directing them to correct api for authorised requests.
    :param request: GET, POST, PUT or DELETE request
    :param pk: ID number of specific Note
    :return: JsonResponse in response to GET request
    """
    if request.method == 'GET':
        try:
            Note.objects.filter(pk=pk).update(views_count=F('views_count') + 1)
            note = Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            Note.objects.filter(pk=pk).update(views_count=F('views_count') - 1)
            return Response(status=404)

        serializer = NoteSerializer(note)
        return JsonResponse(serializer.data, safe=False)
    else:
        return Response('Use /auth/ api for requests that modify data data', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def auth_api_list(request):
    """
    View for users authorised with token, used for /auth/ url.
    It is used to handle GET and POST requests.
    :param request: GET or POST request
    :return:
    """
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        if len(request.data['content']) == 0:
            return Response("Message cannot be empty", status=status.HTTP_400_BAD_REQUEST)
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def auth_api_detail(request, pk):
    """
    View for users authorised with token, used for /auth/id/ urls, where id is specific id number.
    It is used to handle GET, PUT, DELETE requests related to specific notes.
    :param request: GET, POST or DELETE request
    :param pk: ID number of specific note
    :return:
    """
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        # Get current views count and increment by one
        note.views_count = F('views_count') + 1
        note.save()

        note = Note.objects.get(pk=pk)  # Display note with updated views_count
        serializer = NoteSerializer(note)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data=request.data)
        if len(request.data['content']) == 0:
            return Response("Message cannot be empty", status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            note.views_count = 0  # Updated note will have its views count reset to 0
            note.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
