import json


class Config():
    def __init__(self):
        try:
            f1=open("E:\programme\Python\practice\config.txt",'r',encoding='UTF-8')
            confi_str=f1.read()
            self.config_dict=json.loads(confi_str)
            self.color=self.config_dict['color']
            f1.close()
        except:
            f=open("E:\programme\Python\practice\config.txt",'w',encoding='UTF-8')
            config_dict={'color':'#cef0dd'}
            config_str=json.dumps(config_dict)
            f.write(config_str)
            f.close()
    def get_color(self):
        return self.color
    def save_color(self,color):
        self.config_dict['color']=color
        f = open("E:\programme\Python\practice\config.txt", 'w', encoding='UTF-8')
        config_str = json.dumps(self.config_dict)
        f.write(config_str)
        f.close()

config=Config()