#!/usr/bin/python3

# Develop

"""Definition of sqlite"""

DEFINITION = """
CREATE TABLE IF NOT EXISTS measureFive(
  min            REAL NOT NULL,
  max            REAL NOT NULL,
  counter        INT NOT NULL,
  gr1 REAL       NOT NULL,
  gr2 REAL       NOT NULL,
  gr3 REAL       NOT NULL,
  gr4 REAL       NOT NULL,
  idReader       INT NOT NULL,
  nameReader     TEXT NOT NULL,
  idController   INT NOT NULL,
  nameController TEXT NOT NULL,
  typeMeasure    TEXT NOT NULL
);
"""


def get_definition():
    """Return Definition"""
    return DEFINITION
