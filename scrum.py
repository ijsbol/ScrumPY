import sys
from scrumpy import handler
from scrumpy import errors

ACCEPTED_FILE_EXTENSION = ".sc"

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError as error:
        raise errors.error(f"No file was selected to run. | Try: 'scrum.py program{ACCEPTED_FILE_EXTENSION}'")
    file_extension = file_path[-len(ACCEPTED_FILE_EXTENSION)::]
    if file_extension != ACCEPTED_FILE_EXTENSION:
        raise errors.error(f"Unrecognised file extension '{file_extension}', only accepted type: `{ACCEPTED_FILE_EXTENSION}`")
    handler.run_file(file_path)
