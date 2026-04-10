from .models import VisitorCounter

class VisitorCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/' and not request.session.get('visited'):
            counter, created = VisitorCounter.objects.get_or_create(id=1)
            counter.count += 1
            counter.save()
            request.session['visited'] = True

        response = self.get_response(request)
        return response