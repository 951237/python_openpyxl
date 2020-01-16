#개요
'''
1. 프로그램이 해야할 일
    현재 작업 디렉토리에 있는 모든 csv파일을 찾는다.
    각 파일의 전체 내용을 읽어들인다.
    첫 번째 줄은 건너 뛰고 내용을 새로운 csv파일에 기록한다.
2. 코드수준의 프로그램이 할일
    os.listdir()으로 부터 얻은 파일의 리스트를 루프로 돌리면서 csv가 아닌 파일은 건너뛴다.
    csv reader 객체를 만드록 파일 안의 내용을 읽기. 어떤 행을 건너뛸지 계산하기 위해 line_num속성을 이용
    csv writer 객체를 만들고 읽어들인 데이터를 새 파일에 저장한다.
'''

#알고리즘

#1단계 - 루프로 각 csv파일을 거쳐가기
'''
    임포트 csv os
    폴더 만들기 : headerRemoved
    반복문 : 현재디렉토리 파일의 모든파일들을 한 개식 검사 csvFilename
        조건문 : 파일 확장자가 ‘.csv’로 끝나지 않으면
        계속하기
    안내메세지 : ‘Removing header from’ + csvFilename + ‘. . .’
'''
import csv, os
os.makedirs('headerRemoved',exist_ok=True) #디렉토리 만들기
for csvFilename in os.listdir('.'): #디렉토리 파일모두 읽기
    if not csvFilename.endswith('.csv'): #확장자 비교하기
        continue
    print('Removing header from' + csvFilename + '. . .')

    #2단계 - csv 파일로부터 읽기
    '''
        리스트 만들기 : csvRow[]
        csvFilename를 열어서 csvFileObj로 지정하기
        csvFilename를 csv.reader 개체로 만들어 readerObj로 지정하기
        반복문 : readerObj에서 row을 불러서
            조건문 : readerObj의 줄수가 1줄이면
                계속진행하기
            아니면 csvRows에 추가하기
        csvFileObj 파일 닫기
    '''

    csvRow=[]
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj) #csv파일 읽기
    for row in readerObj:
        if readerObj.line_num == 1: #csv파일 라인의 갯수 확인
            continue
        csvRow.append(row)
    csvFileObj.close()

    #3단계 - 첫 행을 없앤 csv파일을 저장하기
    '''
        파일 열어서 csvFileObj로 설정하기: headerRomoved 폴더에 csvFilename으로 열기
        csvFileOjb를 csv writer 개체를 csvWriter로 지정하기
        반복문 : csvRows 리스트에서 한줄씩 
            csvWriter개체에 row를 행으로 쓰기
        csvFileObj 파일 닫기
    '''

    csvFileObj = open(os.path.join('headerRemoved',csvFilename),'w',newline='') #디렉토리 지정해서 파일 저장하기
    csvWriter = csv.writer(csvFileObj) #csv 파일 쓰기
    for row in csvRow:
        csvWriter.writerow(row)
    csvFileObj.close()