from django.http import JsonResponse
from django.shortcuts import render

from grpc_client.client import get_application_data, get_user_data


def application_data_view(request):
    application_id = 1  # Replace with actual logic to determine the application ID
    grpc_response = get_application_data(application_id)
    data = {"application_data": grpc_response.data}
    return JsonResponse(data)


def user_data_view(request):
    user_id = 1  # Replace with actual logic to determine the user ID
    grpc_response = get_user_data(user_id)
    return JsonResponse({"user_data": grpc_response})
