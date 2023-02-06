# HTTP Client Requests

|           |                                                                                                 |
| --------- | ----------------------------------------------------------------------------------------------- |
| Name      | HTTP Client Requests                                                                            |
| Version   | v1.0.1                                                                                          |
| DockerHub | [weevenetwork/http-client-requests](https://hub.docker.com/r/weevenetwork/http-client-requests) |
| Authors   | Marcus Jones                                                                                    |

## Table of Contents

- [HTTP Client Requests](#http-client-requests)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Input](#input)
  - [Output](#output)

## Description

This Module performs repeated HTTP requests (acting as a client) at a specified interval, to the given URL. The returned payload is forwarded to the next module. This module may be used to interact with a single REST API resource endpoint.

NOTE: Only one header is supported.

The Python class, HttpRequest, is an implementation of a simple HTTP client using the aiohttp library. It provides methods for sending a HTTP request and polling a URL at a specified interval. The class takes in a URL, method, authentication token, payload, and header as parameters. The class also contains some error handling, such as checking if the URL is valid and raising an error if the method is not one of the allowed values. The send_request method sends the HTTP request and returns the response. The poll method repeatedly sends the request and forwards the response.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Environment Variables | type   | Description                                            |
| --------------------- | ------ | ------------------------------------------------------ |
| URL                   | string | The full URL, including protocol and path              |
| METHOD                | string | HTTP request method; GET, POST, DELETE, PUT            |
| AUTH_TOKEN            | string | Will be passed as "{Authorization: Bearer AUTH_TOKEN}" |
| PAYLOAD               | string | Data for POST                                          |
| HEADER                | string | Additional HTTP header, as a JSON string               |
| POLL_INTERVAL         | string | Poll interval in seconds                               |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                                                                          |
| --------------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| MODULE_NAME           | string | Name of the module                                                                                   |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)                                                       |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module                                                               |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |

## Input

HTTP response body

## Output

Output of this module is a string or JSON, as specified by the user.
