# Importing the required modules
import logging

import azure.functions as func


# Defining the function
def main(req: func.HttpRequest) -> func.HttpResponse:
    # Logging a message
    logging.info('Python HTTP trigger function processed a request.')

    # Getting the value of the 'name' parameter from the request
    name = req.params.get('name')
    # If the 'name' parameter is not present in the request URL, trying to get it from the request body
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    # If 'name' is present, returning a personalized response with the value of 'name' in the message
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # If 'name' is not present, returning a generic response with a message asking for the 'name' parameter
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
