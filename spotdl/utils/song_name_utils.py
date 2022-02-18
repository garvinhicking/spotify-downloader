import re

def format_name(input_str: str) -> str:
    output = input_str

    # ! this is windows specific (disallowed chars)
    output = "".join(char for char in output if char not in "/?\\*|<>#")

    # ! double quotes (") and semi-colons (:) are also disallowed characters but we would
    # ! like to retain their equivalents, so they aren't removed in the prior loop
    output = output.replace('"', "'").replace(":", " - ")

    # Optional replacements of characters that cause trouble for i.e. Dropbox synchronization
    # TODO: How to check for arguments.safe_filenames at this point?!
    output = re.sub('[^A-Za-zÀ-ž\u0370-\u03FF\u0400-\u04FF 0-9\._,-]', '_', output)

    return output
