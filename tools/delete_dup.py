import hashlib
import os
import time
import sys, getopt



from conf import config





def getmd5(filename):
    """
    获取文件 md5 码
    :param filename: 文件路径
    :return: 文件 md5 码
    """
    file_txt = open(filename, 'rb').read()
    # 调用一个md5对象
    m = hashlib.md5(file_txt)
    # hexdigest()方法来获取摘要（加密结果）
    return m.hexdigest()


def main(argv):
    path = ''
    # 文件夹路径
    try:
        opts, args = getopt.getopt(argv, "hi:a", ["help","ifile=","aauto="])

    except getopt.GetoptError:
        print('test.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <input dirs>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            path = arg
        elif opt in ("-a", "--aauto"):

            t_dir = time.strftime("%Y-%m-%d", time.localtime())
            path = "{}/{}".format(config.getpath(),t_dir);
    # 键为文件大小, 值为列表（文件路径、md5）
    all_size = {}
    total_file = 0
    total_delete = 0
    # 开始时间
    start = time.time()
    # 遍历文件夹下的所有文件
    for file in os.listdir(path):
        # 文件数量加 1
        total_file += 1
        # 文件的路径
        real_path = os.path.join(path, file)
        # 判断文件是否是文件
        if os.path.isfile(real_path) == True:
            # 获取文件大小
            size = os.stat(real_path).st_size
            # md5(默认为空)
            size_and_md5 = [""]
            # 如果文件大小已存在
            if size in all_size.keys():
                # 获取文件的md5码
                new_md5 = getmd5(real_path)
                # 大小相同，md5 为空，添加md5
                if all_size[size][0] == "":
                    all_size[size][0] = new_md5
                # md5 已存在，删除
                if new_md5 in all_size[size]:
                    print('删除', real_path)
                    os.remove(real_path)
                    total_delete += 1
                else:
                    # md5 不存在，进行添加
                    all_size[size].append(new_md5)
            else:
                # 如果文件大小不存在，则将此文件大小添加到 all_size 字典中
                all_size[size] = size_and_md5
    # 结束时间
    end = time.time()
    time_last = end - start
    print('文件总数：', total_file)
    print('删除个数：', total_delete)
    print('耗时：', time_last, '秒')


if __name__ == '__main__':
    main(sys.argv[1:])