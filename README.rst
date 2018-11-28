========
Services
========

Services is a simple Django app to consume simple json services in a simple way. 
You can make requests directly, async or recursive using failover services 
automatically while the services return errors.
Example:

```
import services

service_example = Service(name='registration_precheck', method='get', url='http://example.com/?query_param=<data>')
url_data = {'<data>': 'example_data'}
service_response = service_example.request_recursive(get_data=get_data)

if service_response['success']:
    respose_content = service_response['content'] # content is a dict
    print (response_content)

```

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

       INSTALLED_APPS = [
               ...
               'services',
       ]

2. Run `python manage.py migrate` to create the services models.

3. Start the development server and visit http://127.0.0.1:8000/admin/services
   to create a services (you'll need the Admin app enabled).

