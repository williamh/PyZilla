=======
PyZilla
=======

PyZilla is a simple wrapper for the xmlrpclib package which
provides an object that can be used to make XML-RPC calls to a
Bugzilla installation.

It exposes the BugZilla object which you can instantiate with the uri
for the xmlrpc.cgi file on your bugzilla installation.

Here's a simple usage example:

    >>> from pyzilla import BugZilla
    >>> bzilla = BugZilla("http://bugzilla.example.com/xmlrpc.cgi")
    >>> bzilla.login("username", "password")
    >>> bzilla.Bugzilla.version()

For this example, the module will store the authentication cookies in
the current directory in a file named cookies.txt.

For details of the API, please refer to the Bugzilla webservice docs
<http://www.bugzilla.org/docs/3.0/html/api/Bugzilla/WebService.html>.

For a saner interface to bugzilla, please refer to the Bugzilla
REST API <https://wiki.mozilla.org/Bugzilla:REST_API>.
