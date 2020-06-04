"""
** HTTP Introduction**
-describe what happens when you type a url in the url bar 
-describe the requests/response cycle
-explain what a requests or response header is , and give examples
-explain the different categories of response codes 
-compare GET and POST requests 

**the internet**

when using the search bar 
first - DNS lookUp
second - computer makes a REQUEST to a server
third - Server processes that REQUEST 
fourth - sever issues a RESPONSE
[this is a Request/Response cycle]


**http headers **

- sent with both requests and responses
-provide additional information about the request of response
**request Headers **
~ACCEPT - acceptable contents-type for respone (e.g. html,json,xml)
~cache-control - specify cashing behavior 
~user-agent- information about the software used to make the request
**response headers **
~access-control-allow-origin: specify domains that can make requests
~allowed - http verbs that are allowed in requests

**response status codes **
~2xx- success
~3xx - redirect
~4xx - client error(your fault)
~5xx - server error(not your fault)


"""
