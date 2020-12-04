class LoginFromFile:
    def __init__(self, filename,username,password):
        self.filename = filename
        self.username=username
        self.password=password


    def getDataFromFileCSV(self):
        filename = self.filename
        login_list = []
        import pandas as pd
        csv_file=pd.read_csv(filename)
        for id,row in csv_file.iterrows():
            info_dic=dict()
            info_dic['username']=row['username']
            info_dic['password']=row['password']
            info_dic['link_id']=row['link_id']
            info_dic['role']=row['role']
            login_list.append(info_dic)
        return login_list

    def checkLogin(self, lst):
        username = self.username
        password =self.password
        for x in lst:
            if (x['username'].strip() == username.strip()) & (str(x['password']).strip() == password.strip()):
                return True,x['link_id'],x['role']
        return False,0,None

    #-------for sign up---------#
    def addNewLoginInfo(self, lst):
        usr =self.username
        pwd = self.password
        for x in lst:
            if usr.strip() == x['username'].strip():
                return False

        # write to file
        with open('../dataset/login_table.csv', 'a') as f:
            f.writelines("\n" + usr + "," + pwd)
            print("Adding new info is ok.")
            return True


