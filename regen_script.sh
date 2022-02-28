#!/bin/bash

rm freecad_saves/*
python3 src/csv_rail_generate.py
# freecad freecad_saves/python_generated_post.FCStd
