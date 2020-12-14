import tarfile
import xml.etree.ElementTree as ET
import traceback
import pandas as pd
import glob
import sys


def go(old, new, record_type, resultfoldername):
    if record_type == 'spm':
        c_name = ["OCLC_Num", "MMS_ID", "Holding_Status", "Condition", "Gov_ind"]
        rtn_name = 'uiu_spm_with_past_records.txt'

        return
    elif record_type == 'mpm':
        c_name = ["OCLC_Num", "MMS_ID", "Holding_Status", "Condition", " Item_Description", "Gov_ind"]
        rtn_name = 'uiu_mpm_with_past_records.txt'

    else:
        c_name = ["OCLC_Num", "MMS_ID", "ISSN", "Gov_ind"]
        rtn_name = 'uiu_serials_with_past_records.txt'

    df_past = pd.read_csv(old, sep='\t', names=c_name)
    df_current = pd.read_csv(new, sep='\t', names=c_name)
    mms_df_current = list(df_current["MMS_ID"])
    mms_df_past = list(df_past["MMS_ID"])
    mms_in_new = list(set(mms_df_current) - set(mms_df_past))
    df_dif = df_current.loc[df_current["MMS_ID"].isin(mms_in_new)]
    df_new = df_past.append(df_dif)
    df_new.to_csv(resultfoldername + "/" + rtn_name, sep='\t',
                  index=False, header=False)
    return


if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args < 5:
        print("Error: please read ReadMe file carefully about how to run the script.")
    else:
        go(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])