#
# 请输入这个程序的功能  视频 转mp3



import os
import sys
from moviepy.editor import VideoFileClip

def video_to_audio(input_video, output_audio):
    # 加载视频文件
    video_clip = VideoFileClip(input_video)

    # 提取音频
    audio_clip = video_clip.audio

    # 获取输入视频文件的文件名和扩展名
    file_name, _ = os.path.splitext(os.path.basename(input_video))

    # 构建输出音频文件路径
    output_audio_path = os.path.join(os.path.dirname(input_video), file_name + ".mp3")

    # 保存为 MP3 文件
    audio_clip.write_audiofile(output_audio_path)

    # 关闭视频和音频文件的连接
    video_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("请拖动视频文件到脚本上。")
    else:
        # 输入视频文件路径（从命令行参数获取）
        input_video_path = sys.argv[1]

        # 调用函数进行转换
        video_to_audio(input_video_path, None)

        print("转换完成！")
