from .models import VisitorCounter

def visitor_counter(request):
    counter = VisitorCounter.objects.filter(id=1).first()
    return {'visitor_count': counter.count if counter else 0}