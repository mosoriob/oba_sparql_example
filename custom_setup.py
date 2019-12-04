from typing import Dict
from pprint import pprint

from obasparql.static import GET_ALL_USER_QUERY, GET_ONE_USER_QUERY
from settings import GRAPH_BASE, ENDPOINT
import unittest

from obasparql import QueryManager
from settings import QUERY_DIRECTORY, CONTEXT_DIRECTORY, QUERIES_TYPES


class TestSum():
    @staticmethod
    def generate_graph(username):
        return "{}{}".format(GRAPH_BASE, username)

    def setUp(self):
        self.query_manager = QueryManager(queries_dir=QUERY_DIRECTORY,
                                          context_dir=CONTEXT_DIRECTORY,
                                          queries_types=QUERIES_TYPES)
        username = "mint@isi.edu"
        self.username = self.generate_graph(username)

    def test_get_one_setup_custom(self):
        """
        Test to obtain one resource by the uri and a custon query
        """
        owl_class_name = "custom"
        resource_uri = "https://w3id.org/okn/i/mint/cycles-0.9.4-alpha-simple-pongo"
        resource_type_uri = "https://w3id.org/okn/o/sdm#ModelConfigurationSetup"
        query_type = "get_setup"

        #grlc args
        request_args: Dict[str, str] = {
            "resource": resource_uri,
            "g": self.username
        }

        resource = self.query_manager.obtain_query(query_directory=owl_class_name,
                                                   owl_class_uri=resource_type_uri,
                                                   query_type=query_type,
                                                   endpoint=ENDPOINT,
                                                   request_args=request_args)
        return resource
if __name__ == '__main__':
    example = TestSum()
    example.setUp()
    resource = example.test_get_one_setup_custom()
    pprint(resource)

