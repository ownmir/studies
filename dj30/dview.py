from django.views.generic.dates import ArchiveIndexView
from models import MainDuty

class DutyIndexView(ArchiveIndexView):
    model = MainDuty
    date_field = "date_duty"
    date_list_period = "year"
    template_name = "main/index.html"
    # context_object_name = "duty"
    allow_empty = True
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['duties'] = MainDuty.objects.all()
        return context
