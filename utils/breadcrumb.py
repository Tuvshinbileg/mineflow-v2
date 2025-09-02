from django.views import View


class HamView(View):
    def get_breadcrumb(self):
        return []
