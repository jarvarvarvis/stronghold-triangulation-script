# stronghold-triangulation-script

Python script to triangulate the position of a stronghold from just two eyes of ender.

## Usage instructions

First of all, run the script.

### First eye

You are prompted to enter 3 values in total:
- Your camera's yaw when looking in the direction of flight of the eye
- The X component of the player's position when the eye is thrown
- The Z component of the player's position when the eye is thrown

### Move between eye throws

After entering the values for the first eye throw, you are prompted to rotate left/right
by 90°. The program will also print the optimal yaw values for a 90°-left/-right rotation
respectively.
After you've made a decision in which direction to move, enter your new yaw value.

Note that the 90° are not a requirement, just a good choice. Anything around that value probably
works fine as well.

You may now move forwards. Try to keep the camera steady while doing so, the results are the best
if you move in a straight line from the first position.

Around ~100 blocks should be enough distance to move, but you may travel a further distance. 
Just remember to keep the camera steady.

### Second eye

When you've reached a good location to throw the second eye, you are again prompted to enter
the following 3 values:
- Your camera's yaw when looking in the direction of flight of the eye
- The X component of the player's position when the eye is thrown
- The Z component of the player's position when the eye is thrown

### Output

The program will produce the following output:
```
Triangulation data:
============================================================
Alpha: <angle>°
Beta: <angle>°
Moved distance between throws: <distance>
Length of d (height of triangle): <length of side d>
Distance from first point to stronghold: <distance stronghold <-> first eye throw>
Forward direction from first point: <direction first point -> stronghold>

 -> Triangulated stronghold location: <stronghold (X, Z) coordinates>
```

The relevant output (the triangulated stronghold location) is in the last line.


## Usage recommendations

Triangulation is prone to small errors in the input values, so maybe run the script two or three
times to get accurate results.
