from django.core.paginator import Paginator


def prepare_pagination(list_of_object, per_page, request):
    paginator = Paginator(list_of_object, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    page_range = [i for i in range(max(1, page_obj.number - 1), min(page_obj.number + 1, paginator.num_pages) + 1)]
    if paginator.num_pages == 1:
        page_range = None
    elif paginator.num_pages == 2:
        page_range = range(1, 3)
    elif len(page_range) < 3:
        page_range = page_range + [3] if page_obj.number == 1 else [page_range[-1] - 2] + page_range
    return page_range, page_obj, paginator.num_pages