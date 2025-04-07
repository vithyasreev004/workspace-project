from django.shortcuts import render
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def simple_view(request):
    logger.debug('Rendering template: blog/simple.html')
    return render(request, 'blog/simple.html')

