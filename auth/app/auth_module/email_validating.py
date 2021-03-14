import re
from typing import Optional
from auth_module.exceptions import ValidatingError


class Validating(object):
    def validating(email: str) -> Optional[str]:
        pattern: str = r'[^@]+@[^@]+\.[^@]+'
        if not re.match(pattern, email):
            raise ValidatingError(email)
        return email
