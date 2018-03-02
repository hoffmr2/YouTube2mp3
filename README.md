# YouTube2mp3

Small application for downloading audio from YouTube in mp3 320 kb/s format.
May be used as python app, or can be freezed with setup.py file. Tested and design for windows

## Prerequisites

Requires installing following packages:

- pafy https://github.com/mps-youtube/pafy

- audiotranscode https://github.com/devsnd/python-audiotranscode

  which requires additional for working on windows system:
  - lame mp3 [download](http://www.free-codecs.com/download_soft.php?d=6124be49faf6fa64474a329b31d6fef9&s=22&r=&f=lame_encoder.htm)
  - ffmpeg [download](https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20180227-fa0c9d6-win64-static.zip)
  - faad [download](http://www.rarewares.org/files/aac/faad2-20100614.zip) 
- cx_Freeze https://anthony-tuininga.github.io/cx_Freeze/

## Creating Windows *.exe

- open windows powershell in youTube2mp3 directory
- type  "python .\setup.py"
- output "YouTube2mp3.exe" will appear in build directory

## Usage

### Python script Windows

- copy lame.exe, lame_enc.dll, ffmpeg.exe and faad.exe to youTube2mp3 directory
- open windows powershell in youTube2mp3 directory
- type  "python .\mainWindow.py"

### Standalone Windows

- copy lame.exe, lame_enc.dll, ffmpeg.exe and faad.exe to build directory
- run YouTube2mp3.exe
