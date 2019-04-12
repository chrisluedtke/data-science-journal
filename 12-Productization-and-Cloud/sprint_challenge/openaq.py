"""Simple openaq to only depend on json, math, and requests (no dfs/plots)."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import math


class ApiError(Exception):
    pass

class API(object):
    """Generic API wrapper object.
    """
    def __init__(self, **kwargs):
        self._key       = kwargs.pop('key', '')
        self._pswd      = kwargs.pop('pswd', '')
        self._version   = kwargs.pop('version', None)
        self._baseurl   = kwargs.pop('baseurl', None)
        self._headers   = {'content-type': 'application/json'}

    def _make_url(self, endpoint, **kwargs):
        """Internal method to create a url from an endpoint.
        :param endpoint: Endpoint for an API call
        :type endpoint: string
        :returns: url
        """
        endpoint = "{}/{}/{}".format(self._baseurl, self._version, endpoint)

        extra = []
        for key, value in kwargs.items():
            if isinstance(value, list) or isinstance(value, tuple):
                #value = ','.join(value)
                for v in value:
                    extra.append("{}={}".format(key, v))
            else:
                extra.append("{}={}".format(key, value))

        if len(extra) > 0:
            endpoint = '?'.join([endpoint, '&'.join(extra)])

        return endpoint

    def _send(self, endpoint, method='GET', **kwargs):
        """Make an API call of any method

        :param endpoint: API endpoint
        :param method: API call type. Options are PUT, POST, GET, DELETE

        :type endpoint: string
        :type method: string

        :returns: (status_code, json_response)

        :raises ApiError: raises an exception
        """
        auth = (self._key, self._pswd)
        url  = self._make_url(endpoint, **kwargs)

        if method == 'GET':
            resp = requests.get(url, auth=auth, headers=self._headers)
        else:
            raise ApiError("Invalid Method")

        if resp.status_code != 200:
            raise ApiError("A bad request was made: {}".format(resp.status_code))

        res = resp.json()

        # Add a 'pages' attribute to the meta data
        try:
            res['meta']['pages'] = math.ceil(res['meta']['found'] / res['meta']['limit'])
        except:
            pass

        return resp.status_code, res

    def _get(self, url, **kwargs):
        return self._send(url, 'GET', **kwargs)

class OpenAQ(API):
    """Create an instance of the OpenAQ API

    """
    def __init__(self, version='v1', **kwargs):
        """Initialize the OpenAQ instance.

        :param version: API version.
        :param kwargs: API options.

        :type version: string
        :type kwargs: dictionary

        """
        self._baseurl = 'https://api.openaq.org'

        super(OpenAQ, self).__init__(version=version, baseurl=self._baseurl)

    def cities(self, **kwargs):
        """Returns a listing of cities within the platform.

        :param country: limit results by a certain country
        :param limit: limit results in the query. Default is 100. Max is 10000.
        :param page: paginate through the results. Default is 1.
        :param order_by: order by one or more fields (ex. order_by=['country', 'locations']). Default value is 'country'
        :param sort: define the sort order for one or more fields (ex. sort='desc')

        :return: dictionary containing the *city*, *country*, *count*, and number of *locations*

        :type country: 2-digit ISO code
        :type limit: number
        :type order_by: string or list of strings
        :type sort: string
        :type page: number
        :type country: string or array of strings
        :type df: bool
        :type index: string

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.cities()
        >>> resp['results']
        [
            {
                "city": "Amsterdam",
                "country": "NL",
                "count": 21301,
                "locations": 14
            },
            {
                "city": "Badhoevedorp",
                "country": "NL",
                "count": 2326,
                "locations": 1
            },
            ...
        ]
        """
        return self._get('cities', **kwargs)

    def countries(self, **kwargs):
        """Returns a listing of all countries within the platform

        :param order_by: order by one or more fields (ex. order_by=['cities', 'locations']). Default value is 'country'
        :param sort: define the sort order for one or more fields (ex. sort='desc')
        :param limit: change the number of results returned. Max is 10000. Default is 100.
        :param page: paginate through results. Default is 1.

        :type order_by: string or list
        :type sort: string
        :type limit: int
        :type page: int
        :type df: bool
        :type index: string

        :return: dictionary containing the *code*, *name*, *count*, *cities*, and number of *locations*.

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.countries()
        >>> resp['results']
        [
            {
                "cities": 174,
                "code": "AT",
                "count": 121987,
                "locations": 174,
                "name": "Austria"
            },
            {
                "cities": 28,
                "code": "AU",
                "count": 1066179,
                "locations": 28,
                "name": "Australia",
            },
            ...
        ]
        """
        return self._get('countries', **kwargs)

    def latest(self, **kwargs):
        """Provides the latest value of each parameter for each location

        :param city: limit results by a certain city. Defaults to ``None``.
        :param country: limit results by a certain country. Should be a 2-digit
                        ISO country code. Defaults to ``None``.
        :param location: limit results by a city. Defaults to ``None``.
        :param parameter: limit results by a specific parameter. Options include [
                            pm25, pm10, so2, co, no2, o3, bc]
        :param has_geo: filter items that do or do not have geographic information.
        :param coordinates: center point (`lat`, `long`) used to get measurements within a
                                certain area. (Ex: coordinates=40.23,34.17)
        :param radius: radius (in meters) used to get measurements. Must be used with coordinates.
                        Default value is 2500.
        :param limit: change the number of results returned. Max is 10000. Default is 100.
        :param page: paginate through the results.

        :type city: string
        :type country: string
        :type location: string
        :type parameter: string
        :type has_geo: bool
        :type coordinates: string
        :type radius: int
        :type limit: int
        :type page: int
        :type df: bool
        :type index: string

        :return: dictionary containing the *location*, *country*, *city*, and number of *measurements*

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.latest()
        >>> resp['results']
        [
            {
                "location": "Punjabi Bagh",
                "city": "Delhi",
                "country": "IN",
                "measurements": [
                    {
                        "parameter": "so2",
                        "value": 7.8,
                        "unit": "ug/m3",
                        "lastUpdated": "2015-07-24T11:30:00.000Z"
                    },
                    {
                        "parameter": "co",
                        "value": 1.3,
                        "unit": "mg/m3",
                        "lastUpdated": "2015-07-24T11:30:00.000Z"
                    },
                    ...
                ]
                ...
            }
        ]
        """
        return self._get('latest', **kwargs)

    def locations(self, **kwargs):
        """Provides metadata about distinct measurement locations

        :param city: Limit results by one or more cities. Defaults to ``None``. Can define as a single city
                        (ex. city='Delhi'), a list of cities (ex. city=['Delhi', 'Mumbai']), or as a tuple
                        (ex. city=('Delhi', 'Mumbai')).
        :param country: Limit results by one or more countries. Should be a 2-digit
                        ISO country code as a string, a list, or a tuple. See `city` for details.
        :param location: Limit results by one or more locations.
        :param parameter: Limit results by one or more parameters. Options include [
                            pm25, pm10, so2, co, no2, o3, bc]
        :param has_geo: Filter items that do or do not have geographic information.
        :param coordinates: center point (`lat`, `long`) used to get measurements within a
                                certain area. (Ex: coordinates=40.23,34.17)
        :param nearest: get the X nearest number of locations to `coordinates`. Must be used
                        with coordinates. Wins over `radius` if both are present. Will add the
                        `distance` property to locations.
        :param radius: radius (in meters) used to get measurements. Must be used with coordinates.
                        Default value is 2500.
        :param order_by: order by one or more fields (ex. order_by=['country', 'count']). Default value is 'location'
        :param sort: define the sort order for one or more fields (ex. sort='desc')
        :param limit: change the number of results returned. Max is 10000. Default is 100.
        :param page: paginate through the results.

        :type city: string, array, or tuple
        :type country: string, array, or tuple
        :type location: string, array, or tuple
        :type parameter: string, array, or tuple
        :type has_geo: bool
        :type coordinates: string
        :type nearest: int
        :type radius: int
        :type order_by: string or list
        :type sort: string
        :type limit: int
        :type page: int
        :type df: bool
        :type index: string

        :return: a dictionary containing the *location*, *country*, *city*, *count*, *distance*,
                    *sourceName*, *sourceNames*, *firstUpdated*, *lastUpdated*, *parameters*, and *coordinates*

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.locations()
        >>> resp['results']
        [
            {
                "count": 4242,
                "sourceName": "Australia - New South Wales",
                "firstUpdated": "2015-07-24T11:30:00.000Z",
                "lastUpdated": "2015-07-24T11:30:00.000Z",
                "parameters": [
                    "pm25",
                    "pm10",
                    "so2",
                    "co",
                    "no2",
                    "o3"
                ],
                "country": "AU",
                "city": "Central Coast",
                "location": "wyong"
            },
            ...
        ]
        """
        return self._get('locations', **kwargs)

    def measurements(self, **kwargs):
        """Provides data about individual measurements

        :param city: Limit results by a certain city. Defaults to ``None``.
        :param country: Limit results by a certain country. Should be a 2-digit
                        ISO country code. Defaults to ``None``.
        :param location: Limit results by a city. Defaults to ``None``.
        :param parameter: Limit results by one or more parameters. Options include [
                            pm25, pm10, so2, co, no2, o3, bc]
        :param has_geo: Filter items that do or do not have geographic information.
        :param coordinates: center point (`lat`, `long`) used to get measurements within a
                        certain area. (Ex: coordinates=40.23,34.17)
        :param radius: radius (in meters) used to get measurements. Must be used with `coordinates`.
                        Default value is 2500.
        :param value_from: Show results above a value threshold. Must be used with `parameter`.
        :param value_to: Show results below a value threshold. Must be used with `parameter`.
        :param date_from: Show results after a certain date. Format should be ``Y-M-D``.
        :param date_to: Show results before a certain date. Format should be ``Y-M-D``.
        :param sort: The sort order (``asc`` or ``desc``). Must be used with `order_by`.
        :param order_by: Field to sort by. Must be used with **sort**.
        :param include_fields: Include additional fields in the output. Allowed values are: *attribution*,
                            *averagingPeriod*, and *sourceName*.
        :param limit: Change the number of results returned. Max is 10000 and default is 100.
        :param page: Paginate through the results

        :type city: string
        :type country: string
        :type location: string
        :type parameter: string, array, or tuple
        :type has_geo: bool
        :type coordinates: string
        :type radius: int
        :type value_from: number
        :type value_to: number
        :type date_from: date
        :type date_to: date
        :type sort: string
        :type order_by: string
        :type include_fields: array
        :type limit: number
        :type page: number
        :type df: bool
        :type index: string

        :return: a dictionary containing the *date*, *parameter*, *value*, *unit*,
            *location*, *country*, *city*, *coordinates*, and *sourceName*.

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.measurements(city = 'Delhi')
        >>> resp['results']
        {
            "parameter": "Ammonia",
            "date": {
                "utc": "2015-07-16T20:30:00.000Z",
                'local': "2015-07-16T18:30:00.000-02:00"
            },
            "value": "72.9",
            "unit": "ug/m3",
            "location": "Anand Vihar",
            "country": "IN",
            "city": "Delhi",
            "coordinates": {
                "latitude": 43.34,
                "longitude": 23.04
            },
            "attribution": {
                "name": "SINCA",
                "url": "http://sinca.mma.gob.cl/"
            },
            {
                "name": "Ministerio del Medio Ambiente"
            }
            ...
        }
        """
        return self._get('measurements', **kwargs)

    def fetches(self, **kwargs):
        """Provides data about individual fetch operations that are used to populate
        data in the platform.

        :param order_by: order by one or more fields (ex. order_by=['timeEnded', 'count']). Default value is 'country'
        :param sort: define the sort order for one or more fields (ex. sort='desc')
        :param limit: change the number of results returned. Max is 10000. Default is 100.
        :param page: paginate through the results. Default is 1.

        :type order_by: string or list
        :type sort: string
        :type limit: int
        :type page: int

        :return: dictionary containing the *timeStarted*, *timeEnded*, *count*, and *results*

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.fetches()
        >>> resp
        {
            "meta": {
                "name": "openaq-api",
                "license":
                "website":
                "page": 1,
                "limit": 100,
                "found": 3,
                "pages": 1
            },
            "results": [
                {
                    "count": 0,
                    "results": [
                        {
                            "message": "New measurements inserted for Mandir Marg: 1",
                            "failures": {},
                            "count": 0,
                            "duration": 0.153,
                            "sourceName": "Mandir Marg"
                        },
                        {
                            "message": "New measurements inserted for Sao Paulo: 1898",
                            "failures": {},
                            "count": 1898,
                            "duration": 16.918,
                            "sourceName": "Sao Paulo"
                        },
                        ...
                    ],
                    "timeStarted": "2016-02-07T15:25:04.603Z",
                    "timeEnded": "2016-02-07T15:25:04.793Z",
                }
            ]
        }
        """
        return self._get('fetches', **kwargs)

    def parameters(self, **kwargs):
        """
        Provides a simple listing of parameters within the platform.

        :param order_by: order by one or more fields (ex. order_by=['preferredUnit', 'id']). Default value is 'country'
        :param sort: define the sort order for one or more fields (ex. sort='desc')

        :type order_by: string or list
        :type sort: string

        :return: a dictionary containing the *id*, *name*, *description*, and
            *preferredUnit*.

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.parameters()
        >>> resp['results']
        [
            {
                "id": "pm25",
               "name": "PM2.5",
               "description": "Particulate matter less than 2.5 micrometers in diameter",
               "preferredUnit": "ug/m3"
            }
            ...
        ]
        """
        return self._get('parameters', **kwargs)

    def sources(self, **kwargs):
        """
        Provides a list of data sources.

        :param order_by: order by one or more fields (ex. order_by=['active', 'country']). Default value is 'country'
        :param sort: define the sort order for one or more fields (ex. sort='desc')
        :param limit: Change the number of results returned.
        :param page: Paginate through the results

        :type limit: number
        :type page: number
        :type df: bool
        :type index: string
        :type order_by: string or list
        :type sort: string

        :return: a dictionary containing the *url*, *adapter*, *name*, *city*,
            *country*, *description*, *resolution*, *sourceURL*, *contacts*, and *active*.

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.sources()
        >>> resp['results']
        [
            {
                "url": "http://airquality.environment.nsw.gov.au/aquisnetnswphp/getPage.php?reportid=2",
                "adapter": "nsw",
                "name": "Australia - New South Wales",
                "city": "",
                "country": "AU",
                "description": "Measurements from the Office of Environment & Heritage of the New South Wales government.",
                "resolution": "1 hr",
                "sourceURL": "http://www.environment.nsw.gov.au/AQMS/hourlydata.htm",
                "contacts": [
                    "olaf@developmentseed.org"
                ]
            }
            ...
        ]
        """

        return self._get('sources', **kwargs)

    def __repr__(self):
        return "OpenAQ API"
