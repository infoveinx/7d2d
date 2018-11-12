package main

import (
  "fmt"
  "flag"
)

const regionSize int = 512

// south or west map coordinate
func swPoint(mapCoord *int) int8 {
    coord := float32(*mapCoord / regionSize)
    coord += 1.0
    return int8(coord * -1.0)
}

// north or east map coordinate
func nePoint(mapCoord *int) int8 {
    coord := float32(*mapCoord / regionSize)
    return int8(coord)
}

func main() {
    // command line arguments
    northPtr := flag.Int("n", 0, "north")
    southPtr := flag.Int("s", 0, "south")
    eastPtr := flag.Int("e", 0, "east")
    westPtr := flag.Int("w", 0, "west")
    flag.Parse()

    var (
        xCoord int8 = 0
        yCoord int8 = 0
    )

    if *northPtr != 0 {
        yCoord = nePoint(northPtr)
    } else if *southPtr != 0 {
        yCoord = swPoint(southPtr)
    }

    if *eastPtr != 0 {
        xCoord = nePoint(eastPtr)
    } else if *westPtr != 0 {
        xCoord = swPoint(westPtr)
    }

    fmt.Printf("Region file is: r.%d.%d.7rg\n", xCoord, yCoord)
}
