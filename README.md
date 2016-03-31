HTTP Redirector
===============

Simple HTTP server that always redirects to another location. Useful for reverse proxies that can't do it themselves.

Environment variables:

- PORT -- Port number for the server to listen on. Defaults to 8080.
- REDIRECT -- URL to redirect to. Mandatory
- APPENDPATH -- If set then the path of the request including query string is appended to the redirect url.


