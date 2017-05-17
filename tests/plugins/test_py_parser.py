import os
import sys
import pytest
import context

from context import devspell
from context import get_path
PyParser = devspell.plugins.PyParser

def test_python_basic():
  """Test the basic operation of the Python parser"""
  parser = PyParser(None)
  assert not parser.path
  assert not parser.content

  parser = PyParser("does.not.exist")
  assert not parser.content

  path = get_path("parsers/python/basic.py")
  parser = PyParser(path)
  assert not parser.sections.has_section("!/usr/bin/python")
  assert parser.sections.has_section("This is a single comment")
  assert parser.sections.has_section("Information about test")
  assert parser.sections.has_section("This is my life")
  assert parser.sections.has_section("Comment about")
  assert parser.sections.has_section("Bob's life")
  assert parser.sections.has_section("Bob's fun life")
