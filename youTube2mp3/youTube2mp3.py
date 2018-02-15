import pafy
import audiotranscode
import os


class YouTube2mp3:

    def __init__(self):

        self.audio_transcode = audiotranscode.AudioTranscode()
        self.tmp_file = "tmp."

    def download(self, url, destination_path, bitrate, callback, end_flag):

        video = pafy.new(url)
        best_audio = video.getbestaudio(preftype="m4a")
        best_extension = best_audio.extension

        best_audio.download(filepath=self.tmp_file + best_extension, quiet=True, meta=False, remux_audio=True,
                            callback=callback)
        try:
            self.audio_transcode.transcode(self.tmp_file + best_extension, destination_path, bitrate=bitrate)
        except:
            print('Unsupported audio format')
            os.remove(destination_path + self.mp3)
        os.remove(self.tmp_file + best_extension)
        end_flag[0] = True
