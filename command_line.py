#this script required os with Python 3.10.1 installed
#this script uses PyPDF2, globm, natsort and os library
import PyPDF2
import glob
from natsort import natsorted
import os

#create blank list variables for date and wo folders list
all_folders_by_date = []
all_folders_by_wo = []



#set master directory
master_folder = os.listdir('E:/py made by imam/pdf merger/scan_pa_budi/pdf scan')

#import PyPDF2 lib
merge_pdfs = PyPDF2.PdfFileMerger()



#the playground
#get a list of all master folders
for i in master_folder:
    #put all the folder by date in a list
    all_folders_by_date.insert(1,i)
    wo_folder = os.listdir(f'scan_pa_budi/pdf scan/{i}')
    #put all wo folder to the list
    all_folders_by_wo.insert(1,wo_folder)
    print(i) #this to check the folders available in the list
    #create new folder to the new directory
    os.makedirs(f'scan_pa_budi/new pdf scan/{i}')
    for files in wo_folder:
        print(f'wo .................{i}')
        print(files)
        # take all pdf in every folder we have
        all_pdf = glob.glob(f'scan_pa_budi/pdf scan/{i}/{files}/*.pdf') #take all pdf inside each folders directory
        print(all_pdf)
        merge_pdfs = PyPDF2.PdfFileMerger() #put the blank list for pdf to be merged 
        for pdf in all_pdf: #natsorted each pdf because the folders named consecutively
            merge_pdfs.append(open(pdf,'rb')) #to put the pdfs in each wo folders in list
            print(pdf)
            new_pdf_files = (f'E:/py made by imam/pdf merger/scan_pa_budi/new pdf scan/{i}/{files}.pdf') # this to rename the merged file name in the new directory with the previous container folders name
            merge_pdfs.write(open(new_pdf_files,'wb')) #this to create new file containing the merged pdf, with the formated name, and new directory.
