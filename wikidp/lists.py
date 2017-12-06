#!/usr/bin/python
# coding=UTF-8
#
# WikiDP Wikidata Portal
# Copyright (C) 2017
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.
#
"""Pre-populated constant lists."""
def properties():
    """Calls the list of default properties the user will be prompted to fill out"""
    software_list = [("P275", "item"),
                     ("P348", "string"),
                     ("P856", "url"),
                     ("P1547", "item"),
                     ("P178", "item"),
                     ("P1072", "item"),
                     ("P1073", "item"),
                     ("P1195", "string"),
                     ("P400", "item"),
                     ("P277", "item"),
                     ("P306", "item"),
                     ("P2749", "ex-id"),
                     ("P2078", "string"),
                     ("P1401", "string")
                    ]
    # property_values = ["P31", "P361", "P144", "P1365", "P178"]
    return software_list
    # file formats**, software, refs, quals


    # sitelinks
    # aliases
    # claims
    # descriptions


# # TO DO:

# Categories of alternates
# Collapsable [Item Preview]
# Home/Unsearched output
# Better parsing of refs
# Refs of external links
# details
# Does not work on: Q1324793
