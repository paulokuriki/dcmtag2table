import pydicom
from tqdm import tqdm
import pandas as pd
import os
import time
import glob


def dcmtag2df(folder, list_of_tags):
    """
    # Create a Pandas DataFrame with the <list_of_tags> DICOM tags
    # from the DICOM files in <folder>

    # Parameters:
    #    folder (str): folder to be recursively walked looking for DICOM files.
    #    list_of_tags (list of strings): list of DICOM tags with no whitespaces.


    # Returns:
    #    df (DataFrame): table of DICOM tags from the files in folder.
    """
    list_of_tags = list_of_tags.copy()
    table = []
    start = time.time()

    # checks if folder exists
    if not os.path.isdir(folder):
        print(f'{folder} is not a valid folder.')
        return None

    # joins ** to the folder name for using at the glob function
    print("Searching files recursively...")
    search_folder = os.path.join(folder, '**')

    try:
        filelist = glob.glob(search_folder, recursive=True)
        print(f"{len(list(filelist))} files/folders found ")
    except Exception as e:
        print(e)
        return None
    time.time()
    print("Reading files...")

    for _f in tqdm(filelist):
        try:
            ds = pydicom.dcmread(_f, stop_before_pixels=True)
            items = []
            items.append(_f)

            for _tag in list_of_tags:
                if _tag in ds:
                    #items.append(ds.data_element(_tag).value)
                    items.append(str(ds.data_element(_tag).value))
                else:
                    items.append("Not found")

            table.append((items))
        except:
            pass
            # print("Skipping non-DICOM: " + _f)

    list_of_tags.insert(0, "Filename")
    test = list(map(list, zip(*table)))
    dictone = {}

    if len(table) == 0:
        print(f'0 DICOM files found at folder: {folder}')
        return None

    for i, _tag in enumerate(list_of_tags):
        dictone[_tag] = test[i]

    df = pd.DataFrame(dictone)
    time.sleep(2)
    print("Finished.")
    return df

list_of_tags = [
    "AccessionNumber",
    "AcquisitionDate",
    "AcquisitionMatrix",
    "AcquisitionTime",
    "ConvolutionKernel",
    "ImageOrientationPatient",
    "ImageTime",
    "InstitutionName",
    "Manufacturer",
    "ManufacturersModelName",
    "ModalitiesInStudy",
    "Modality",
    "NumberOfAverages",
    "PatientID",
    "ProtocolName",
    "SeriesDescription",
    "SeriesInstanceUID",
    "SeriesTime",
    "SOPClassUID",
    "SOPInstanceUID",
    "SpacingBetweenSlices",
    "StationName",
    "StudyDescription",
    "StudyID",
    "StudyInstanceUID",
    "StudyTime"
]

#folder = "C:\\Users\\paulo\\Desktop\\dicom\\"
#export_csv = "C:\\Users\\paulo\\Desktop\\dicom\\results.csv"

folder = os.getcwd()
export_csv = os.path.join(folder, 'export.csv')

df = dcmtag2df(folder, list_of_tags)

try:
    if len(df.index) > 0:
        df.to_csv(export_csv)
        print(f'{export_csv} exported successfully.')
    else:
        print(f'{export_csv} not modified.')
except Exception as e:
    print(f'Error exporting {export_csv} file.\n' + str(e))