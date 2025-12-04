# LibraryProject/middleware.py

class ContentSecurityPolicyMiddleware:
    """
    Adds a secure Content Security Policy header to every response.
    Helps prevent XSS attacks by limiting where scripts, styles,
    and other resources can load from.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Restrictive CSP configuration – expand if using CDNs
        response.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self'; "
            "img-src 'self' data:; "
            "font-src 'self'; "
            "connect-src 'self'"
        )
        return response
