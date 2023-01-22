from blog.models import Category


def get_context_data(request):
    cat_menu = Category.objects.all()
    return {'cat_menu': cat_menu}
