import rest_framework.response


class Response(rest_framework.response.Response):
    """Base Response"""

    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
    ) -> None:
        super().__init__(data, status, template_name, headers, exception, content_type)


class Ok(Response):
    """200 OK"""

    status_code = 200


class Created(Response):
    """201 Created"""

    status_code = 201


class Accepted(Response):
    """202 Accepted"""

    status_code = 202


class NoContent(Response):
    """204 No Content"""

    status_code = 204


class BadRequest(Response):
    """400 Bad Request"""

    status_code = 400


class Unauthorized(Response):
    """401 Unauthorized"""

    status_code = 401


class Forbidden(Response):
    """403 Forbidden"""

    status_code = 403


class NotFound(Response):
    """404 Not Found"""

    status_code = 404


class MethodNotAllowed(Response):
    """404 Not Found"""

    status_code = 404


class InternalServerError(Response):
    """500 Internal Server Error"""

    status_code = 500


class RequestTimeout(Response):
    """408 Request Timeout"""

    status_code = 408


class Conflict(Response):
    """408 Conflict (Resource trying to be created already exists)"""

    status_code = 409
