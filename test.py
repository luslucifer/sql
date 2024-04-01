# Sample dictionary data
data_dict = {
    "IMDBLink": "IMDBLink_value",
    "IMDBScore": 8.7,
    "SubtitleLink": "SubtitleLink_value",
    "SubtitleDownload": "SubtitleDownload_value",
    "SubtitleFilename": "SubtitleFilename_value",
    "SubtitleDownloads": 1000,
    "SubtitleLanguage": "English",
    "SubtitleFormat": "SRT",
    "SubtitleTotal": 10,
    "SubtitleUploaded": "2024-04-01 12:00:00",
    "SubtitleNFOCreated": "2024-04-01 12:00:00",
    "SubtitleReleaseName": "SubtitleReleaseName_value",
    "SubtitleFPS": 23.976,
    "CDFilename": "CDFilename_value",
    "CDSize": 1048576,
    "CDMD5": "CDMD5_value"
}

# Convert dictionary data to a list of tuples
# data_list = [(v for k, v in data_dict.items())]
data_list = [tuple(data_dict.values())]


# Insert data into the database
print(data_list)
