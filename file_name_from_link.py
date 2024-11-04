def extract_file_name(url: str) -> str:
    return url.split('/')[-1].split('.')[0]
