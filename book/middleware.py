class FirstMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f" resuest is : {self.get_response}")
        response = self.get_response(request)
        return response
