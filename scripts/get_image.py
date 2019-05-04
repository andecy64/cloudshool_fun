from cloudscool_fun.apiflash_utils import ApiflashMicroClient

def get_image(url, dir_path):
    client = ApiflashMicroClient(screenshot_dir=dir_path)
    client.get_image(url)

def main():
    pass
