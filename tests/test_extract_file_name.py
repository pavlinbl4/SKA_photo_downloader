import unittest

from fille_name_from_link import extract_file_name


class TestExtractFileName(unittest.TestCase):
    def test_basic_url(self):
        url = "http://example.com/path/to/file.jpg"
        self.assertEqual(extract_file_name(url), "file")

    def test_url_without_extension(self):
        url = "http://example.com/path/to/file"
        self.assertEqual(extract_file_name(url), "file")

    def test_url_with_query_parameters(self):
        url = "http://example.com/path/to/file.jpg?query=123"
        self.assertEqual(extract_file_name(url), "file")

    def test_url_with_multiple_dots(self):
        url = "http://example.com/path.to/file.name.jpg"
        self.assertEqual(extract_file_name(url), "file")

    def test_trailing_slash(self):
        url = "http://example.com/path/to/file.jpg/"
        self.assertEqual(extract_file_name(url), "")

    def test_empty_url(self):
        url = ""
        self.assertEqual(extract_file_name(url), "")

    def test_url_with_no_filename(self):
        url = "http://example.com/path/to/"
        self.assertEqual(extract_file_name(url), "")

if __name__ == "__main__":
    unittest.main()