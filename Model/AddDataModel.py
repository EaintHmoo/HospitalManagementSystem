import pandas as pd
class DataClass:
    def __init__(self,path):
        self.subject_table_path = path

    def addNewData(self,arr):
        try:
            df=pd.read_csv(self.subject_table_path)
            total_row=len(df)+1
            data_list=[]
            data_list.append(total_row)
            for x in arr:
                data_list.append(x)

            print(data_list)

            import csv
            with open(self.subject_table_path, "a",newline='') as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(data_list)
                print('add data')
        except Exception as e:
            print(str(e))