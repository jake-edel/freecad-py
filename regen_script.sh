#!/bin/bash

rm freecad_saves/python_generated_post.FCStd
python3 src/angle_rail_generate.py 
freecad freecad_saves/python_generated_post.FCStd
