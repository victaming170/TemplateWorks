from pathlib import Path

d_root = Path.cwd()  # 返回当前运行目录
fP = Path(d_root, 'dir0_0/t1_0.txt')    # 可以在Path的同时将几个字符串连接
print(fP.resolve())     # resolve()方法返回绝对路径
fP2 = Path(d_root, 'dir0_0/t1_1.txt')
if Path(d_root / 'rnm-t0_0.bin').exists():
    Path(d_root / 'rnm-t0_0.bin').unlink()
fP3 = Path(d_root, 't0_0.txt')

print('----------- path property -----------')
print('name:', fP.name)     # 从路径中获取文件名，其实是获取路径元组中的最后一项
print('stem:', fP.stem)     # 从路径中获取不含后缀的纯文件名，其实就是获取路径元组最后一项的点之前的部分
print('suffix:', fP.suffix) # 从路径中获取后缀，其实就是获取路径元组最后一项的点之后的部分; 还有suffixs
print('parent:', fP.parent) # 获取文件所在目录名；还有parents，包含每一级父目录
print('parts:', fP.parts)   # 通过'\'将路径分割为一个元组

print('----------- exist -------------')
# Path.exists(), .is_file(), .is_dir()
if fP.exists():
    if fP.is_file():
        print('fP is file.')
    elif fP.is_dir():
        print('fP is dir.')
else:
    print('fP not exists.')

print('------------ read/write ----------------')
# with fP.open('r') as ffx:     # fP.open('r')等价于open(fP, 'r')
#     print(ffx.readline())
#     print(ffx.readline())
# lines = fP.read_text()          # 以字符串形式读取fP中的全部内容
fP2.write_text('hello1')         # write_text()则是以字符串形式覆写
# bs = fP.read_bytes()            # 以二进制形式读取fP中的全部内容
fP3.write_bytes(bytes([65, 66, 67])) # write_bytes()则是二进制覆写
print('create fP3, write ABC')

print('------------ create/delete/move -----------')
new_dir_Path = Path(d_root, 'dir0_1/dir1_1')
tgt_path = new_dir_Path / 'tgt-t1_1.txt'
if new_dir_Path.is_dir():
    print('new dir already existed. Delete')
    if tgt_path.exists():
        tgt_path.unlink()           # 删除文件
    new_dir_Path.rmdir()            # 删除空目录
new_dir_Path.mkdir(parents=True)    # 创建文件夹，打开parents可以多级新建
print('new dir created.')
fP2.replace(tgt_path.with_name('tgt-t1_1.txt'))               # source.replace(destination)
print('move file from source to destination')
fP3.rename(d_root / 'rnm-t0_0.bin')     # 重命名，会把整个路径重命名, 所以注意把目录名也加上

print('------------- file information -----------')
info_f = fP.stat()
print('file size:', info_f.st_size)
print('create time:', info_f.st_ctime)  # 文件创建时间戳
print('modify time:', info_f.st_mtime)  # 文件修改时间戳
print(type(info_f.st_mtime))

print('------------- browse ----------------')
for i in d_root.iterdir():  # 遍历目录下属各项
    print(i.name)
for i in d_root.rglob('*.txt'):     # 遍历目录下各特定项，rglob()可同时遍历子目录，glob()仅遍历本目录
    print(i)
