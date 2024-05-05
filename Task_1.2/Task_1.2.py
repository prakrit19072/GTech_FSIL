# first need to get all the URLs
# then we can do the query API
from sec_api import QueryApi
from sec_api import ExtractorApi
import json 
import os
import csv
queryApi = QueryApi(api_key="3a1d698ade390ad4c149f477b761eb2d1633849899ac24343c01956c1a046249")
extractorApi = ExtractorApi(api_key = "3a1d698ade390ad4c149f477b761eb2d1633849899ac24343c01956c1a046249")
import pandas as pd



query_ibm = {
  "query": { "query_string": { 
      "query": "formType:\"10-K\" AND ticker:IBM", # only 10-Ks
  }},
  "from": "0", # start returning matches from position null, i.e. the first matching filing 
  "size": "24"  # return just one filing
}

query_orcl = {
  "query": { "query_string": { 
      "query": "formType:\"10-K\" AND ticker:ORCL", # only 10-Ks
  }},
  "from": "0", # start returning matches from position null, i.e. the first matching filing 
  "size": "24"  # return just one filing
}



query_aapl = {
  "query": { "query_string": { 
      "query": "formType:\"10-K\" AND ticker:AAPL", # only 10-Ks
  }},
  "from": "0", # start returning matches from position null, i.e. the first matching filing 
  "size": "24"  # return just one filing
}



#21

response_aapl = queryApi.get_filings(query_aapl)
response_ibm = queryApi.get_filings(query_ibm)
response_orcl = queryApi.get_filings(query_orcl)


aapl= open(os.path.join(os.getcwd(),"Task_1.2\\Urls","AAPL_urls.txt"),"a")
for i in range(22):
    aapl.write(str(response_aapl["filings"][i]["linkToFilingDetails"])+"\n")


orcl= open(os.path.join(os.getcwd(),"Task_1.2\\Urls","ORCL_urls.txt"),"a")
for i in range(22):
    orcl.write(str(response_orcl["filings"][i]["linkToFilingDetails"])+"\n")


ibm= open(os.path.join(os.getcwd(),"Task_1.2\\Urls","IBM_urls.txt"),"a")
for i in range(22):
    ibm.write(str(response_ibm["filings"][i]["linkToFilingDetails"])+"\n")






path = os.path.join(os.getcwd(),"Task_1.2","Urls","ORCL_urls.txt")
with open(path, 'r') as file:
    num=0
    for line in file:
        year = 2023-num
        url = str(line.strip())
        section_1 = extractorApi.get_section(filing_url=url, 
                                            section="1", 
                                            return_type="text")
        section_1A = extractorApi.get_section(filing_url=url, 
                                            section="1A", 
                                            return_type="text")
        section_7A = extractorApi.get_section(filing_url=url, 
                                            section="7A", 
                                            return_type="text")
        section_8 = extractorApi.get_section(filing_url=url, 
                                            section="8", 
                                            return_type="text")
        filename  = f"ORCL_{year}.csv"
        with open(filename, 'w') as csvfile:
            row1 = ['1',section_1]
            row2 = ['1A', section_1A]
            row3 = ['7A', section_7A]
            row4 =  ['8', section_8]
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row1)
            csvwriter.writerow(row2)
            csvwriter.writerow(row3)
            csvwriter.writerow(row4)
        num = num+1




path = os.path.join(os.getcwd(),"Task_1.2","Urls","AAPL_urls.txt")
with open(path, 'r') as file:
    num=0
    for line in file:
        year = 2023-num
        url = str(line.strip())
        section_1 = extractorApi.get_section(filing_url=url, 
                                            section="1", 
                                            return_type="text")
        section_1A = extractorApi.get_section(filing_url=url, 
                                            section="1A", 
                                            return_type="text")
        section_7A = extractorApi.get_section(filing_url=url, 
                                            section="7A", 
                                            return_type="text")
        section_8 = extractorApi.get_section(filing_url=url, 
                                            section="8", 
                                            return_type="text")
        filename  = f"AAPL_{year}.csv"
        with open(filename, 'w') as csvfile:
            row1 = ['1',section_1]
            row2 = ['1A', section_1A]
            row3 = ['7A', section_7A]
            row4 =  ['8', section_8]
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row1)
            csvwriter.writerow(row2)
            csvwriter.writerow(row3)
            csvwriter.writerow(row4)
        num = num+1



path = os.path.join(os.getcwd(),"Task_1.2","Urls","IBM_urls.txt")
with open(path, 'r') as file:
    num=0
    for line in file:
        year = 2023-num
        url = str(line.strip())
        section_1 = extractorApi.get_section(filing_url=url, 
                                            section="1", 
                                            return_type="text")
        section_1A = extractorApi.get_section(filing_url=url, 
                                            section="1A", 
                                            return_type="text")
        section_7A = extractorApi.get_section(filing_url=url, 
                                            section="7A", 
                                            return_type="text")
        section_8 = extractorApi.get_section(filing_url=url, 
                                            section="8", 
                                            return_type="text")
        filename  = f"IBM_{year}.csv"
        with open(filename, 'w') as csvfile:
            row1 = ['1',section_1]
            row2 = ['1A', section_1A]
            row3 = ['7A', section_7A]
            row4 =  ['8', section_8]
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row1)
            csvwriter.writerow(row2)
            csvwriter.writerow(row3)
            csvwriter.writerow(row4)
        num = num+1
      
            
data = pd.read_csv(os.getcwd()+"\\Task_1.2\\csv_data\\AAPL\\AAPL_2010.csv")            
print(data)



with open(os.getcwd()+"\\Task_1.2\\csv_data\\AAPL\\AAPL_2010.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       print(row['1'])
       break










    









