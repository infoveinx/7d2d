#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-04 20:50:06
# @Author  : Scott Farrell
# @Requires: Python 3.6+
import argparse
import sys

def sw_point(map_coord):
    coord = map_coord / 512
    coord += 1
    return int(coord * -1)

def ne_point(map_coord):
    coord = map_coord / 512
    return int(coord)

def usage():
    print(f"Invalid map coordinates.  Usage: {sys.argv[0]} -n 1434 -w 5097")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--north", type=int,
        help="North map coordinate")
    parser.add_argument("-s", "--south", type=int,
        help="South map coordinate")
    parser.add_argument("-e", "--east", type=int,
        help="East map coordinate")
    parser.add_argument("-w", "--west", type=int,
        help="West map coordinate")
    args = parser.parse_args()

    # check the map coordinates and generate the region coordinates
    if args.north:
        y_coord = ne_point(args.north)
    elif args.south:
        y_coord = sw_point(args.south)
    else:
        usage()

    if args.east:
        x_coord = ne_point(args.east)
    elif args.west:
        x_coord = sw_point(args.west)
    else:
        usage()

    print(f"Region file is : r.{x_coord}.{y_coord}.7rg")

if __name__ == "__main__":
    main()
