## Install Python Packages
The following three Python 3 scripts utilized several packages:
  - tarfile
  - xml.etree.ElementTree as ET
  - pandas
  - glob
  - sys
  - traceback

All packages except pandas should be Python standard library. Use pip install [package_name] to install or pip install [package_name] --upgrade to upgrade a package.

<br/>

## HathiPrint_Process_Records_Single-part_Monographs

A Python script used for processing compressed single-part monographs Alma records. After the publication profiles job is done, download all .tar.gz files from FTP server and save them to a local folder (folder_path_1). Create a new folder (folder_path_2) for MARCXML files. Then create a new folder (folder_path_3) for the results generated by the script.

To run the script, download the Sinle-part_Monographs.py file (to file_path_4). We recommand you to save the python file and folders in the same folder so we could use relative path in the command line.
In the command line, 
### In the command line, run: python file_path_4/Single-part_Monographs.py folder_path_1 folder_path_2 folder_path_3
<br/>

## HathiPrint_Process_Records_Multipart_Monographs
A Python script used for processing compressed multipart monographs Alma records. After the publication profiles job is done, download all .tar.gz files from FTP server and save them to a local folder (folder_path_1). Create a new folder (folder_path_2) for MARCXML files. Then create a new folder (folder_path_3) for the results generated by the script.

To run the script, download the Multipart_Monographs.py file (to file_path_4). We recommand you to save the python file and folders in the same folder so we could use relative path in the command line.

In the command line, 
### In the command line, run: python file_path_4/Multipart_Monographs.py folder_path_1 folder_path_2 folder_path_3
                           
<br/>

## HathiPrint_Process_Records_Serials
A Python script used for processing serials Alma records. After the publication profiles job is done, download all .tar.gz files from FTP server and save them to a local folder (folder_path_1). Create a new folder (folder_path_2) for MARCXML files. Then create a new folder (folder_path_3) for the results generated by the script.

To run the script, download the Serials.py file (to file_path_4). We recommand you to save the python file and folders in the same folder so we could use relative path in the command line.

In the command line, 
### In the command line, run: python file_path_4/Serials.py folder_path_1 folder_path_2 folder_path_3
