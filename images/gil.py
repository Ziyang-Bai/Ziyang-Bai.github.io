import os

def generate_image_links_from_directory(directory, output_file, columns=1):
    # 定义常见图片格式的扩展名
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')

    # 获取目录下所有符合扩展名的图片文件
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(valid_extensions)]

    # 按照文件名排序
    image_files.sort()

    with open(output_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="en">\n')
        f.write('<head>\n')
        f.write('<meta charset="UTF-8">\n')
        f.write('<title>Image Gallery</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<h1>Image Gallery</h1>\n')
        f.write('<div id="gallery">\n')

        # 循环生成链接
        for filename in image_files:
            filepath = os.path.join(directory, filename)
            f.write(f'<a href="{filepath}" target="_blank">{filename}</a><br>\n')

        f.write('</div>\n')
        f.write('</body>\n')
        f.write('</html>\n')

# 使用函数，假设图片在"images"目录中
generate_image_links_from_directory('images', 'gallery.html')
