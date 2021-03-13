## Manipulating Images
### Course 6, Week 1

This is my own implementation of the solution and is **overkill** for the
purpose of finishing the assignment. I wanted this script to stand on
its own and be able to be used in other situations. Therefore, this
script **has no dependencies** but does **require certain command-line
arguments** to work correctly.

I intend to modify this script to be even more interactable, but for
now, it does the following:

- Converts to 3-channel RGB
- Rotates images 90 degrees clockwise
- Resizes images to 128 x 128 pixels
- Saves images as JPEG

#### Required commandline arguments, in order:
    1. Source Directory - path to directory containing source images
    2. Source Extension - extension of the images to be converted
    3. Destination Directory - path to directory to save converted images in

**Example:**
> `user@pc:~$ python3 convert-images.py ~/images .png ~/converted`
