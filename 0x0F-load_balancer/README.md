# Load Balancer

I was given a second server to setup a nginx web server on top. and an additional server to set up an HAproxy load balancer to manage traffic connection between both web servers.

# Tasks

1. ["0-custom_http_response_header](./0-custom_http_response_header)

> * This bash script configures a new server with nginx and it sets the HTTP response to contain a custom header


2. ["1-install_load_balancer](./1-install_load_balancer)

> * This bash script setups up HAproxy load balancer on a new machine

e. ["2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp)

> * using puppet to add custom header to http response
