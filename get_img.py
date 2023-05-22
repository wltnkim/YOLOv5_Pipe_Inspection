import ftplib
import os
import shutil

# ftp 정보
host = 'rovitek.inosf.net'
user = 'givet'
passwd = 'Givet23'

# host = 'localhost'
# user = 'test'
# passwd = 'test108'

folder_tree = 0


try:
    # ftp 연결
    with ftplib.FTP() as ftp:
        ftp.connect(host=host,port=21)
        ftp.encoding = 'utf-8'
        #ftp.set_pasv(False)
        ftp.set_pasv(True)
        s = ftp.login(user=user,passwd=passwd)
        print("Connect success!")

        ftp.cwd("/home/rovitek/4inch/public/data")
        
        # List up files
        list = ftp.nlst()
        ftp.dir()
        #print(list)
 
        
        
        if not os.path.exists("get_imgs"):
            os.makedirs("get_imgs")

        # 파일다운로드
        
        for file in list :
            filename = file.split(sep='.')
            if not len(filename) >= 2:
                #print("Directory : " + file)

                while (folder_tree > 0):
                    folder_tree = folder_tree - 1
                    ftp.cwd('..')

                ftp.cwd(file)
                ftp.dir()
                folder_tree = folder_tree + 1

                file_list = ftp.nlst()
                for folder_tree_file in file_list:
                    #print("File : " + file + "/" + folder_tree_file)
                    fd = open(folder_tree_file, 'wb')
                    ftp.retrbinary("RETR " + folder_tree_file, fd.write)

            else:
                while (folder_tree > 0):
                    folder_tree = folder_tree - 1
                    ftp.cwd('..')

                #print("File : " + file)
                fd = open(file, 'wb')
                ftp.retrbinary("RETR " + file, fd.write)
                
        fd.close()
        ftp.close()
        
                
except Exception as e:
    print(e)



try:
    get_files = os.listdir(os.getcwd())
    for get_file in get_files:
        if '.png' in get_file or '.jpg' in get_file:
            #print(get_file)
            if os.path.exists("get_imgs/" + get_file):
                print(get_file + " exists")
                os.remove(get_file)
            else:
                shutil.move(get_file, "get_imgs/" + get_file)
                


except Exception as e:
    print(e)