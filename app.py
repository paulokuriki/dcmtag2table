from dcmtag2table import dcmtag2table

list_of_tags = [
    "AccessionNumber",
    "AcquisitionDate",
    "AcquisitionMatrix",
    "AcquisitionTime",
    "ConvolutionKernel",
    "ImageOrientationPatient",
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
    "SOPClassUID",
    "SOPInstanceUID",
    "SpacingBetweenSlices",
    "StationName",
    "StudyDescription",
    "StudyID",
    "StudyInstanceUID",
]

folder = "C:\\Users\\paulo\\Documents\\results\\"
export_csv = "C:\\Users\\paulo\\Documents\\results\\dicom_tags.csv"

df = dcmtag2table(folder, list_of_tags)

try:
    df.to_csv(export_csv)
    print(f'{export_csv} exported successfully.')
except:
    print(f'Error exporting {export_csv} file.')
