#!/usr/bin/env python3
from IO.chords import HarmReader

def main():
    filename = "funk.chords"
    reader = HarmReader(filename + ".pdf")
    reader.read(filename)

main()
