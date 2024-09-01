import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized


def access_nested_map(nested_map, path):
    """ Function to access the nested map using the given path. """
    for key in path:
        if key not in nested_map:
            raise KeyError(f"Key '{key}' not found")
        nested_map = nested_map[key]
    return nested_map


def memoize(fn):
    cache = {}

    def memoized_fn(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return memoized_fn


def get_json(url):
    import requests
    response = requests.get(url)
    return response.json()


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):

    @patch('requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        # Set up the mock to return the expected JSON payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function with the test URL
        result = get_json(test_url)

        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the result matches the expected payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    @patch('__main__.TestClass.a_method')
    def test_memoize(self, mock_a_method):
        # Define TestClass within the test method
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Set up the mock to return 42
        mock_a_method.return_value = 42

        # Create an instance of TestClass
        instance = TestClass()

        # Call a_property twice
        result1 = instance.a_property()
        result2 = instance.a_property()

        # Check that a_property returns the correct result
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        # Check that a_method is only called once
        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
