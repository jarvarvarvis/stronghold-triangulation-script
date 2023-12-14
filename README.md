# stronghold-triangulation-script

Python script to triangulate the position of a stronghold from just two eyes of ender.

## Usage instructions

First of all, run the script.

### First eye

You are prompted to enter 4 values in total:
- The X component of the player's position when the eye is thrown
- The Z component of the player's position when the eye is thrown
- The X component of the eye's position after is has stopped moving
- The Z component of the eye's position after is has stopped moving

### Move between eye throws

After entering the values for the first eye throw, you have to move somewhere else to get
data for the second eye throw.

Rotate ~90° left or right and start moving forward.
Around >150 blocks should be enough distance to move, but you may travel a further distance
to improve the accuracy.

Be careful that the eye doesn't start tracking another stronghold, since that will mess up the 
results!

### Second eye

When you've reached a good location to throw the second eye, you are again prompted to enter
the following 4 values:
- The X component of the player's position when the eye is thrown
- The Z component of the player's position when the eye is thrown
- The X component of the eye's position after is has stopped moving
- The Z component of the eye's position after is has stopped moving

### Output

The program will produce the following output:
```
Triangulation data:
============================================================
First eye position:         (<X>, <Z>)
First eye target position:  (<X>, <Z>)
Second eye position:        (<X>, <Z>)
Second eye target position: (<X>, <Z>)
Distance between throws: <distance>

 => Triangulated stronghold location: (X, Z)
```

The relevant output (the triangulated stronghold location) is in the last line.


## Usage recommendations

Triangulation is prone to small errors in the input values, so maybe run the script two or three
times to get accurate results.
