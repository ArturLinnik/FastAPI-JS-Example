# Description

This is a simple example of an API written in FastAPI separate from the front-end and using jinja2 templating. 

Here a username and a password are sent to the route /api/v1/login where the API receives them and returns a json with a success message. The javascript gets this message from the API and if it's sucessful then it posts the form and the username is rendered.
