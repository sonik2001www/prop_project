from property.models import notUser


class CreateNotUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()  # Створюємо нову сесію, якщо вона ще не створена
                session_key = request.session.session_key
                not_user = notUser.objects.create(csrf=session_key)

        response = self.get_response(request)
        return response


