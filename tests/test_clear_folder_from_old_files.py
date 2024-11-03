import os
import unittest
from datetime import datetime, timedelta
from unittest.mock import patch

from clear_folder_from_old_files import delete_old_files


# Assuming delete_old_files is imported from the script


class TestDeleteOldFiles(unittest.TestCase):

    # test 1

    @patch("os.listdir")
    @patch("os.path.isfile")
    @patch("os.remove")
    @patch("os.path.getmtime")
    def test_delete_old_files(self, mock_getmtime, mock_remove, mock_isfile, mock_listdir):
        # Setup test directory and file properties
        test_directory = "test_directory"
        extensions = [".tmp", ".log"]
        minutes = 30
        cutoff_date = datetime.now() - timedelta(minutes=minutes)

        # Mock the list of files in the directory
        mock_listdir.return_value = ["old_file.tmp", "new_file.tmp", "other.log"]

        # Mock file modification times
        old_file_time = (cutoff_date - timedelta(minutes=10)).timestamp()
        new_file_time = (cutoff_date + timedelta(minutes=10)).timestamp()
        mock_getmtime.side_effect = lambda file: old_file_time if "old_file" in file else new_file_time

        # Mock os.path.isfile to return True for all files
        mock_isfile.return_value = True

        # Run the function
        delete_old_files(test_directory, extensions, minutes)

        # Assertions
        mock_remove.assert_called_once_with(os.path.join(test_directory, "old_file.tmp"))
        self.assertEqual(mock_remove.call_count, 1, "Should delete only one old file")


    # test 2

    @patch("os.listdir")
    @patch("os.remove")
    def test_no_files_to_delete(self, mock_remove, mock_listdir):
        # Test with no matching extensions
        test_directory = "test_directory"
        extensions = [".jpg"]
        minutes = 30
        mock_listdir.return_value = ["file.tmp"]

        # Run the function
        delete_old_files(test_directory, extensions, minutes)

        # Assert that no files were deleted
        mock_remove.assert_not_called()


    #test 3

    @patch("os.path.isfile")    # добавил из первого теста
    @patch("os.listdir")
    @patch("os.path.getmtime")
    @patch("os.remove")

    def test_all_files_deleted(self, mock_remove, mock_getmtime, mock_listdir , mock_isfile):  # добавил mock_isfile

        # Test where all files should be deleted
        test_directory = "test_directory"
        extensions = [".tmp", ".log"]
        minutes = 30
        cutoff_date = datetime.now() - timedelta(minutes=minutes)


        # Mock the list of files and modification times
        mock_listdir.return_value = ["old_file1.tmp", "old_file2.log"]
        old_file_time = (cutoff_date - timedelta(minutes=10)).timestamp()
        mock_getmtime.side_effect = lambda file: old_file_time

        # Mock os.path.isfile to return True for all files
        mock_isfile.return_value = True

        # Run the function
        delete_old_files(test_directory, extensions, minutes)


        # Assert that both files were deleted
        self.assertEqual(mock_remove.call_count, 2, "Should delete both old files")





if __name__ == "__main__":
    unittest.main()
