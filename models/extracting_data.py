import re

patterns = {
    "IMDBLink": r"IMDBLink:(.*?)\n",
    "IMDBScore": r"IMDBScore:(.*?)\n",
    "SubtitleLink": r"Link:(.*?)\n",
    "SubtitleDownload": r"Download:(.*?)\n",
    "SubtitleFilename": r"Filename:(.*?)\n",
    "SubtitleDownloads": r"Downloads:(.*?)times\n",
    "SubtitleLanguage": r"Language:(.*?)\n",
    "SubtitleFormat": r"Format:(.*?)\n",
    "SubtitleTotal": r"Total:(.*?)subtitlefile\n",
    "SubtitleUploaded": r"Uploaded:(.*?)\n",
    "SubtitleNFOCreated": r"nfocreated:(.*?)\n",
    "SubtitleReleaseName": r"ReleaseName:(.*?)\n",
    "SubtitleFPS": r"FPS:(.*?)\n",
    "CDFilename": r"Filename:(.*?)\n",
    "CDSize": r"Size:(.*?)bytes\n",
    "CDMD5": r"MD5:(.*?)\n"
}




class FilterInfo:
    def filter_text(self, text: str):
        pattern = re.compile(r'[^a-zA-Z0-9\n\/.:]')
        filtered_text = re.sub(pattern, '', text)
        return filtered_text

    def extract_info(self, txt: str) ->dict:
        info = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, txt)
            if match:
                value = match.group(1).strip()
                # Convert value to int if key expects an integer value
                if key in ['SubtitleDownloads', 'SubtitleTotal', 'CDSize']:
                    value = int(value)
                info[key] = value
            else:
                # Set value to 0 if key is missing and expects an integer value
                if key in ['SubtitleDownloads', 'SubtitleTotal', 'CDSize']:
                    info[key] = 0
                else:
                    info[key] = None

        return info

    def main_extracting_data(self, file_data: str):
        try:
            filtered = self.filter_text(file_data)
            return self.extract_info(filtered)
        except Exception as err:
            print(f'Error in filter info: {err}')

