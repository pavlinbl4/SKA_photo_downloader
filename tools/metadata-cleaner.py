import subprocess
import os
from pathlib import Path

def clean_metadata(image_path):
    """
    Remove all metadata from an image file using exiftool.
    
    Args:
        image_path (str): Path to the image file or directory
        
    Returns:
        bool: True if successful, False if failed
        str: Status message or error details
    """
    try:
        # Convert to Path object for better path handling
        path = Path(image_path)
        
        if not path.exists():
            return False, f"Path does not exist: {image_path}"
            
        # Construct the exiftool command
        # -all= removes all metadata
        # -overwrite_original prevents creating backup files
        cmd = ['exiftool', '-all=', '-overwrite_original']
        
        # Add recursive flag if it's a directory
        if path.is_dir():
            cmd.append('-r')
        
        cmd.append(str(path))
        
        # Run exiftool command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            return False, f"Error: {result.stderr}"
            
        return True, f"Successfully cleaned metadata from {image_path}"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def main(path_to_image):
    """
    Example usage of the clean_metadata function.
    """
    # Example with single file
    success, message = clean_metadata(path_to_image)
    print(message)
    
    # Example with directory
    # success, message = clean_metadata("path/to/image/directory")
    # print(message)

if __name__ == "__main__":
    main('../tests/test_images/20010402_pavl_18_up.jpeg')
