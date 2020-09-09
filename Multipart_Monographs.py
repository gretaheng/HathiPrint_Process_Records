import tarfile
import xml.etree.ElementTree as ET
import traceback
import pandas as pd
import glob
import sys

def unzip_tar(zipfoldername, newfoldername):
	temp = glob.glob(zipfoldername+ "/*.tar.gz")
	old_path = zipfoldername + "\\"
	new_path = zipfoldername + "/"
	all_zip = [i.replace(old_path, new_path) for i in temp]
	xml_name_list = []
	for i in range(len(all_zip)):
		name1 = all_zip[i]
		name2 = all_zip[i].lstrip(new_path).rstrip(".tar.gz") + ".xml"
		my_tar = tarfile.open(name1)
		my_tar.extract(name2, newfoldername + "/")
		my_tar.close()
		xml_name_list.append(newfoldername + "/" + name2)
	return xml_name_list

def read_one_xml(file_name):
	l = []
	root = ET.parse(file_name).getroot()
	for re in root.findall("./record"):
		if re.findall("./datafield[@tag='035'].subfield[@code='a']") is not None:
			for valid_re in re.findall("./datafield[@tag='035'].subfield[@code='a']"):
				if valid_re.text:
					if "(OCoLC)" in valid_re.text:
						oclc = valid_re.text
						mmsid = re.find("./controlfield[@tag='001']").text
						gov = re.find("./datafield[@tag='086']")
						if gov:
							gov_ind = 1
						else:
							gov_ind = 0

						if re.findall("./datafield[@tag='977']") is not None:
							for item in re.findall("./datafield[@tag='977']"):
								if item.find("./subfield[@code='f']") is not None:
									con_text = item.find("./subfield[@code='f']").text.lower()
									if con_text and "damage" in con_text:
										con = "BRT"
									else:
										con = ""
								else:
									con = ""
								if item.find("./subfield[@code='g']") is not None:
									sta_text = item.find("./subfield[@code='g']").text.lower()
									if sta_text and "withdrawn" in sta_text:
										sta = "WD"
									elif (sta_text) and ("missing" in sta_text or "lost" in sta_text):
										sta = "LM"
									else:
										sta = "CH"
								else:
									sta = "CH"
								l_re = [oclc,mmsid,sta,con,gov_ind]
								l.append(l_re)
	return l

def read_all_files(xml_name_list, resultfoldername):
	c_name = ["OCLC_Num","MMS_ID","Holding_Status", "Condition","Gov_ind"]
	df = pd.DataFrame(columns = c_name)
	for i in xml_name_list:
		print('Now processing ' + i)
		rv_d = read_one_xml(i)
		df = df.append(pd.DataFrame(rv_d, columns = c_name))
	df.to_csv(resultfoldername+ "/" + 'multipart_mono_results.txt', sep='\t', index=False, header=False)
	return

def go(zipfoldername, newfoldername, resultfoldername):
	xml_name_list = unzip_tar(zipfoldername, newfoldername)
	print("finish_upzip")
	print("start parsing .xml files")
	read_all_files(xml_name_list, resultfoldername)
	print("Finished!")

if __name__ == "__main__":
	num_args = len(sys.argv)
	if num_args < 4:
		print("Error: please read ReadMe file carefully about how to run the script.")
	else:
		go(sys.argv[1], sys.argv[2], sys.argv[3])