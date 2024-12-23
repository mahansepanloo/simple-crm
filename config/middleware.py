from logger_app.models import Loggers
import json


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        data_request = self._get_request_body(request)

        response = self.get_response(request)

        data = { 
            "user": request.user if request.user.is_authenticated else 'Anonymous',
            "user_ip": self._get_ip(request),
            "view_method": request.method.lower(),
            "view": self._get_view_name(request),
            "request": data_request,
            "response": self._get_response_body(response),
            "status_code": response.status_code,
            "query_params": request.GET.dict() if request.method == 'GET' else None,
        }

        self.create_log_entry(data)
        return response
    
    def create_log_entry(self, data):
        try:
            log_entry = Loggers(**data)
            log_entry.save()
            print("=" * 200)
        except Exception as e:
            print(f"Error saving log: {e}")

    def _get_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR', '')
        return ip

    def _get_view_name(self, request):
        try:
            if request.resolver_match:
                view_func = request.resolver_match.func
                return f"{view_func.__module__}.{view_func.__name__}"
        except AttributeError:
            return "Unknown"

    def _get_request_body(self, request):
        try:
            if request.body:
                return json.loads(request.body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            return "Invalid or non-JSON body"

    def _get_response_body(self, response):
        try:
            if hasattr(response, 'content') and response.content:
                return json.loads(response.content.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            return "Invalid or non-JSON response"
        return None
