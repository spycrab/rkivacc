import rkivacc

import os
import tempfile
import email.utils

import requests
import openpyxl

class RKIReport:

    def extract_row(row, state = True):
        
        data = {}
        
        if state:
            data["state"] = row[0].value
        
        data.update({
                "vaccinations": row[1].value,
                "delta": row[2].value,
                "vaccinations_per_capita": row[3].value,
                "reasons": {
                    "age": row[4].value,
                    "profession": row[5].value,
                    "medical": row[6].value,
                    "nursing_home": row[7].value
                },
                "hint": row[8].value
        })
                    
        return data
        

    def __init__(self, report_xlsx_path, modified = None):
        workbook = openpyxl.load_workbook(filename = report_xlsx_path)
        sheet = workbook.worksheets[rkivacc.WORKSHEET_INDEX]
        
        self._states = {}
        self._modified = modified
        
        table_rows = sheet.iter_rows(min_row=rkivacc.TABLE_FIRST_ROW, 
                                     max_row=rkivacc.TABLE_FIRST_ROW + rkivacc.TABLE_LENGTH - 1,
                                     max_col=9)
        total_row = next(sheet.iter_rows(min_row=rkivacc.TABLE_FIRST_ROW + rkivacc.TABLE_LENGTH,
                                         max_row=rkivacc.TABLE_FIRST_ROW + rkivacc.TABLE_LENGTH,
                                         max_col=9))
        
        for row in table_rows:
            self._states[row[0].value] = RKIReport.extract_row(row)  

        self._total = RKIReport.extract_row(total_row, state = False)
    
    def states(self):
        return list(self._states.keys())
        
    def state(self, name):
        return self._states[name]
        
    def all_states(self):
        return self._states.values()
    
    def total(self):
        return self._total

    def modified(self):
        return self._modified
           
    def download(target_path):
        try:
            response = requests.get(rkivacc.URL)
        except RequestException:
            raise RuntimeError("Failed to obtain statistics from server")
        
        if not response.ok:
            raise RuntimeError("Unexpected status code from server: {}".format(response.status_code))
        
        with open(target_path, "wb") as file:
            file.write(response.content)
        return email.utils.parsedate_to_datetime(response.headers['Last-Modified'])

    def obtain():
        temp_dir = tempfile.TemporaryDirectory()
        temp_file = os.path.join(temp_dir.name, "rkiReport.xlsx")
        last_modified = RKIReport.download(temp_file)
        report = RKIReport(temp_file, last_modified)
        temp_dir.cleanup()
        return report
