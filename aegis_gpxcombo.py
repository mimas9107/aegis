from bs4 import BeautifulSoup
import sys
import glob
import time

def about():
    ### 把神盾匯出的分段 gpx檔結合.
    print("＝＝＝＝＝把神盾匯出的　ｇｐｘ檔結合。　＝＝＝＝＝")
    print("＝　　會輸出合併結果於　ｏｕｔｐｕｔ. ｔｘｔ中　＝")
    print("＝　　　　　　　　　　　　　　　　　　　　　　　＝")
    print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
    return 0

def main():

    work_dir = sys.path[0]
    data_dir = work_dir+"/aegis"
    output_filename = "output.txt"
    print("目前工作目錄={}".format(work_dir))
    print("讀取資料目錄={}".format(data_dir))

    
    datafiles = glob.glob(data_dir+"/*.gpx")

    datafiles.sort()
    datafiles_sorted=datafiles.copy()
    n_datafiles_sorted = len(datafiles_sorted)

    read_progress=0
    data_soups = []
    for each_file in datafiles_sorted:
        with open(each_file) as fp:
            soup = BeautifulSoup(fp,"xml") 

        data_soups.append(soup)
        fp.close()
        read_progress+=1
        print("讀取中...{:.2f}%".format(100*read_progress/n_datafiles_sorted),end='\r',flush=False)
        

    with open(output_filename,"+w") as fout:
        
        gpxheader="<?xml version=\"1.0\" encoding=\"utf-8\"?> \r<gpx xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" version=\"1.0\" creator=\"RunningFree\" xmlns=\"http://www.topografix.com/GPX/1/0\">\r"
        fout.write(gpxheader)
        fout.write("<trk>\r")
        
        write_progress=0
        for ele in data_soups:
            fout.write(str(ele.select("trkseg")[0])+"\r")
            time.sleep(0.3)
            write_progress+=1
            print("寫入...{}中 {:.1f}%".format(output_filename,100*write_progress/n_datafiles_sorted),end='\r',flush=False)

        fout.write("</trk>\r")
        fout.write("</gpx>")
    fout.close()
    print('\n')        

    print(output_filename)
    return 0

if __name__ == "__main__":
    about()
    main()
