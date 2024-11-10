import os
import time
from datetime import datetime, timezone

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from myproject import settings
from myproject.utlis import check_database
from .collectors import register_model_rows_collector
from .models import MyModel
from .forms import MyModelForm


def home(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MyModelForm()

    items = MyModel.objects.all()
    return render(request, 'home.html', {'form': form, 'items': items,
                                         'env_value': os.environ.get('NODE_NAME', 'Default Node')})


def get_data_inserted(request):
    if request.method == 'GET':
        row_count = MyModel.objects.count()
        return HttpResponse(row_count)


# Added for debugging purposes
def debug_view(request):
    return JsonResponse({
        'allowed_hosts': settings.ALLOWED_HOSTS,
        'debug_mode': settings.DEBUG,
        'host_header': request.META.get('HTTP_HOST'),
        'remote_addr': request.META.get('REMOTE_ADDR'),
        'x_forwarded_for': request.META.get('HTTP_X_FORWARDED_FOR'),
    })


def get_metrics(request):
    register_model_rows_collector()
    # Generate and return metrics in Prometheus format
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)


@require_GET
def health_check(request):
    # Check database health
    db_healthy, db_error = check_database()

    # Prepare response data
    health_status = {
        "status": "healthy" if db_healthy else "unhealthy",
        "timestamp": datetime.now(timezone.utc),
        "version": "1.0.0",  # Your app version
        "checks": {
            "database": {
                "status": "healthy" if db_healthy else "unhealthy",
                "error": db_error
            }
        }
    }

    # Return 503 if any critical component is unhealthy
    status_code = 200 if db_healthy else 503

    return JsonResponse(health_status, status=status_code)
