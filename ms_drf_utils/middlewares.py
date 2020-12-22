import jwt


class User:
    id = None
    email = None
    groups = []
    company = None


class RequestJwtMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def get_token_payload(self, request):
        payload = {}

        authorization = request.META.get("HTTP_AUTHORIZATION", "")
        try:
            token = authorization.split("Bearer ")[1]
        except IndexError:
            return {}

        payload = jwt.decode(token, verify=False)
        return payload

    def __call__(self, request):

        payload = self.get_token_payload(request)
        request.user_object = User

        if payload:
            request.user_object.id = payload["sub"]
            request.user_object.email = payload["email"]
            request.user_object.groups = [g for g in payload["scope"].split(" ")]
            request.user_object.company = payload["clt-ref"]

        response = self.get_response(request)

        return response