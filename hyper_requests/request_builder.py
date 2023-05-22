import inspect

from requests.models import Request


def check_request_params(
    request_parameters: list[dict[str, str]]
) -> list[dict[str, str]]:
    """
    Checks the validity of request parameters and ensures they match the attributes of the Request class.

    :param request_parameters: List of dictionaries containing request parameters.
    :return: Validated list of request parameters.
    :raises ValueError: If the request parameters are invalid.
    """

    # Get the attribute names of the Request class
    request_attributes = inspect.getfullargspec(Request.__init__).args

    # Iterate over each dictionary in the request_parameters list
    for request_dict in request_parameters:
        # Get the keys of the dictionary
        request_keys = request_dict.keys()

        # Check if any key in the dictionary is also a valid attribute name of the Request class
        if not any(key in request_attributes for key in request_keys):
            raise ValueError(
                "Invalid request parameters. No matching keys found in Request class attributes."
            )

        # Check if a URL request string is present in the dictionary
        if "url" not in request_keys:
            raise ValueError("Invalid request parameters. No url key present")

    # If all dictionaries have at least one matching key, return the request_parameters list
    return request_parameters
