import os

def generate_image_links_from_directory(directory, output_file, columns=4):
    # 获取目录下所有的jpg文件
    image_files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    
    # 按照文件名排序
    image_files.sort()

    with open(output_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html lang="en">\n')
        f.write('<head>\n')
        f.write('<meta charset="UTF-8">\n')
        f.write('<title>Image Gallery</title>\n')
        f.write('<style>\n')
        f.write('table { width: 80%; margin: 0 auto; border-collapse: collapse; }\n')
        f.write('td { padding: 10px; text-align: left; border: 1px solid #ccc; }\n')
        f.write('a { color: #0000ff; text-decoration: none; }\n')
        f.write('</style>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<h1>Image Gallery</h1>\n')
        f.write('<table>\n')

        # 循环生成表格行和链接
        for i, filename in enumerate(image_files):
            if i % columns == 0:
                f.write('<tr>\n')  # 每n列新建一行
            
            # 生成每个图片的链接
            f.write(f'<td><a href="{os.path.join(directory, filename)}" target="_blank">{filename}</a></td>\n')
            
            if (i + 1) % columns == 0:
                f.write('</tr>\n')  # 每n列结束一行

        # 如果最后一行不满列数，补上</tr>
        if len(image_files) % columns != 0:
            f.write('</tr>\n')

        f.write('</table>\n')
        f.write('</body>\n')
        f.write('</html>\n')

# 调用函数，假设图片都在"images"目录中
generate_image_links_from_directory('.', 'gallery.html')
