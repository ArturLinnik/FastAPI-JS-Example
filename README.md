# Description

This is a simple example of an API written in FastAPI separate from the front-end and using javascript templating. 

Here a username and a password are sent to the route /login where the API receives them and returns a json with a success message. The javascript gets this message from the API and if it's sucessful then it returns the username and the password to the html in order to them to be rendered.
