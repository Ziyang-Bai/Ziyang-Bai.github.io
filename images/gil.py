def generate_image_links(start, end, output_file):
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
        for n in range(start, end + 1):
            filename = f'image-{n}.jpg'
            f.write(f'<a href="{filename}" target="_blank">{filename}</a><br>\n')

        f.write('</div>\n')
        f.write('</body>\n')
        f.write('</html>\n')

# 使用函数，假设图片从image-1.jpg开始到image-100.jpg结束
generate_image_links(1, 100, 'gallery.html')