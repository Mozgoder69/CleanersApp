#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Can't import Django. Check it's installed "
        "and available on your PythonPath env var? "
        "If there any active virtual environments? "
    ) from exc


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "general.settings")
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
