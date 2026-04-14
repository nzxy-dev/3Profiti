>3Profti is a lightweight, reliable, and highly customizable screen recorder for Windows.

# Advanced operation
---
Its operation is simple but practical 3Profiti uses the GDI api to obtain screenshots every so many frames specified by the user in the FPS "edit" 
configuration section and automatically compressed as JPEG format in the .dat file you can use the dat extractor to extract the frames 
from the dat file or using a hexadecimal editor

>To use the dat extractor you need to install Python on your Windows computer.

1. You must open CMD
2. Direct to the installation path in the datextractor folder or simply wherever you have your datextractor, using the "cd" command
3. Execute the code of the function that requires

>Extract Frames
```
python extract_jpgs.py [videoName.dat] [outputfolder] [100"Number of frames to extract"]
```
>Get the maximum number of frames
```
python framecounter.py [videoName.dat]
```
#### without the brackets"[]"
---

# Usage and settings
---
### Using 3Profiti is quite simple, to start recording the screen just open the application and press the "Rec" button and 
### to end the video just press the "Stop" button. You can change the theme in the "Theme Dark" or "Theme Default" 
### button located just above the edit of the file destination selection.
## (Configs)
### For more advanced settings just tap the "Config" button to open the settings window once there you have multiple options such as: 
---
### (Keep . dat File) Which allows you to decide whether or not you want to keep the . dat file that contains all the compressed frames in jpg format or if you want 
### to delete it when you finish assembling your MP4 file
---
### (Assemble MP4vid) This function allows you to decide whether or not you want to generate the final "Video" MP4 file or not 
---
### (Time Lapse Mode) With this function you can record faster and smoother videos designed for timelapse starts recording without a specific
### frame limit or a completely linear or constant timeline perfect for modest PCs with not much space resources (Show cursor) Do you want the 
### mouse to be recorded in your video yes or no
---
### (FPS) Edit specifies the amount of FPS you want to record
---
### (Width) the width of the outgoing video / "Resolution"
---
### (Height) The height of the outgoing video / "Resolution"
---
>*Warning* (When recording in timelapse mode, although fluid, there is a significantly lower number of recorded frames depending on your GPU.
> By increasing the amount of FPS Profiti uses much more GPU so it is more likely to reach even less.
---
