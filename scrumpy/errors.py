import traceback #traceback.print_exc()

class ScrumPYErrors(Exception):
    pass

def error(error_text):
    raise ScrumPYErrors(error_text) 