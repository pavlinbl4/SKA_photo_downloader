import unittest
from io import BytesIO
from unittest.mock import patch, Mock, MagicMock

import requests
from PIL import Image

from image_downloader import downloader


class TestDownloader(unittest.TestCase):
    def setUp(self):
        # Create a test image in memory
        self.test_image = Image.new('RGB', (100, 100), color='red')
        self.test_buffer = BytesIO()
        self.test_image.save(self.test_buffer, format='JPEG')
        self.test_buffer.seek(0)
        
        # Test parameters
        self.test_url = "https://example.com/image.png"
        self.test_album = "test_album"

    @patch('requests.get')
    @patch('PIL.Image.open')
    @patch('file_name_from_link.extract_file_name')  # Replace 'your_module' with actual module name
    def test_successful_download(self, mock_extract_filename, mock_image_open, mock_requests_get):
        # Setup mocks
        mock_response = Mock()
        mock_response.content = self.test_buffer.getvalue()
        mock_requests_get.return_value = mock_response

        # Setup mock image
        mock_pil_image = MagicMock()
        mock_rgb_image = MagicMock()
        mock_pil_image.convert.return_value = mock_rgb_image
        mock_image_open.return_value = mock_pil_image

        mock_extract_filename.return_value = "test_image"

        # Execute function
        downloader(self.test_url, self.test_album)

        # Assertions
        mock_requests_get.assert_called_once_with(self.test_url, stream=True, verify=False)
        mock_pil_image.convert.assert_called_once_with('RGB')
        mock_rgb_image.save.assert_called_once()

        # Verify the save call
        save_args = mock_rgb_image.save.call_args
        self.assertTrue(save_args is not None)
        args, kwargs = save_args
        self.assertEqual(kwargs.get('format', 'JPEG'), 'JPEG')
        self.assertTrue(args[0].endswith('.JPG'))

    @patch('requests.get')
    def test_network_error(self, mock_requests_get):
        # Setup mock to raise network error
        mock_requests_get.side_effect = requests.exceptions.RequestException("Network Error")

        # Execute and verify it handles the error
        downloader(self.test_url, self.test_album)  # Should print error but not raise exception

    @patch('requests.get')
    def test_invalid_image(self, mock_requests_get):
        # Setup mock with invalid image data
        mock_response = Mock()
        mock_response.content = b"invalid image data"
        mock_requests_get.return_value = mock_response

        # Execute and verify it handles the error
        downloader(self.test_url, self.test_album)  # Should print error but not raise exception

    @patch('requests.get')
    @patch('PIL.Image.open')
    @patch('file_name_from_link.extract_file_name')
    def test_save_error(self, mock_extract_filename, mock_image_open, mock_requests_get):
        # Setup mocks
        mock_response = Mock()
        mock_response.content = self.test_buffer.getvalue()
        mock_requests_get.return_value = mock_response

        mock_pil_image = MagicMock()
        mock_rgb_image = MagicMock()
        mock_rgb_image.save.side_effect = IOError("Save Error")
        mock_pil_image.convert.return_value = mock_rgb_image
        mock_image_open.return_value = mock_pil_image

        mock_extract_filename.return_value = "test_image"

        # Execute and verify it handles the error
        downloader(self.test_url, self.test_album)  # Should print error but not raise exception

    def test_invalid_url(self):
        # Test with invalid URL
        downloader("invalid_url", self.test_album)  # Should print error but not raise exception

if __name__ == '__main__':
    unittest.main()
