#!/usr/bin/env python
import os
import sys

os.environ["PYTHONPATH"] = "/home/rajesh/env1/bin/pdfconverter/SaasposeApp"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pdfconverter.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
