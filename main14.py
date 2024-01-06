#
# pyinstaller D:\pythonxiangmu\zidonghua\main14.py --onefile --icon=tubiao.ico



import imageio
from PIL import Image
import os

def resize_image(image, target_size):
    # 使用Pillow库调整图像大小
    return image.resize(target_size)

def video_to_gif(video_path, gif_path, fps=10, target_size=None, target_filesize_mb=5):
    # 使用imageio库读取视频
    video_reader = imageio.get_reader(video_path)
    
    # 获取视频的帧率和帧数
    video_fps = video_reader.get_meta_data()['fps']
    total_frames = video_reader.get_meta_data()['nframes']
    
    # 计算每隔多少帧采样一次，以实现指定的GIF帧率
    sample_every = max(1, int(video_fps / int(fps)))  # 将fps转换为整数，并确保不为零
    
    # 创建一个GIF写入器
    gif_writer = imageio.get_writer(gif_path, fps=int(fps))  # 将fps转换为整数

    try:
        # 逐帧读取视频并写入GIF
        for i in range(0, total_frames, sample_every):
            frame = video_reader.get_data(i)

            # 调整图像大小（如果指定了目标大小）
            if target_size:
                frame = resize_image(Image.fromarray(frame), target_size)

            gif_writer.append_data(frame)
            
            # 获取当前GIF文件大小
            current_filesize_mb = os.path.getsize(gif_path) / (1024 * 1024)
            
            # 如果当前文件大小超过目标大小，尝试降低质量
            if current_filesize_mb > target_filesize_mb:
                gif_writer.set_meta_data({'fps': int(fps), 'quality': 10})  # 将fps转换为整数
                gif_writer.close()
                gif_writer = imageio.get_writer(gif_path, fps=int(fps))  # 将fps转换为整数

                # 重新写入当前帧
                gif_writer.append_data(frame)
    except Exception as e:
        print(f"Error: An exception occurred - {e}")
    finally:
        gif_writer.close()

# 示例用法（限制GIF大小为5MB，同时设置目标大小为300x300像素）
video_path = r'C:\Users\22216\Desktop\fb00f6e89aa94dfddb255731f9e8de61.mp4'
gif_path = 'output_gif.gif'
target_size = (300, 300)
target_filesize_mb = 5
video_to_gif(video_path, gif_path, target_size=target_size, target_filesize_mb=target_filesize_mb)
