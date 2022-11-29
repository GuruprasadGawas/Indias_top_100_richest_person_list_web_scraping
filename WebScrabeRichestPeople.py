from bs4 import BeautifulSoup
import requests, openpyxl


excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Indias 100 Richest'
sheet.append(['Rank','Name','Net Worth','Industry'])

try:
    r = requests.get('https://www.forbes.com/lists/india-billionaires/?sh=571ef015109b')
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')
    # print(soup.prettify)
    tableGroup = soup.find_all('div', class_='table-row-group')
    for tableRowCount in tableGroup:
        tableRowGroup = tableRowCount.find_all('a')
        for tableRow in tableRowGroup:
            rank = tableRow.text.split('.')[0]
            name = tableRow.text.split('.',1)[1].split('$')[0]
            NetWorth = tableRow.text.split('.',1)[1].split('$')[1].split('B',1)[0].strip(" ")
            Industry = tableRow.text.split('.',1)[1].split('$')[1].split('B',1)
            print(rank, name, f"${NetWorth} B", Industry[1])
            sheet.append([rank, name, f"${NetWorth} B", Industry[1]])
            
except Exception as e:
    print(e)

excel.save("India's_Top_100_Richest.xlsx")
        
    

