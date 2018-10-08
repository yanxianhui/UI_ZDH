#coding=utf-8
import sys
sys.path.append('C:\\Users\yanxianhuiclearbos\PycharmProjects')
from utils.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
from  utils.path import CONFIG_FILE
from  utils.mail import Email
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil(CONFIG_FILE+'\keyword.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_value(i,3)
                if is_run == 'yes':
                    except_result_method = handle_excel.get_col_value(i,7)
                    except_result = handle_excel.get_col_value(i,8)
                    method = handle_excel.get_col_value(i,4)
                    send_value = handle_excel.get_col_value(i,5)
                    handle_value = handle_excel.get_col_value(i,6)
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print("没有else")
                    else:
                        print('预期结果为空')

    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')

    def run_method(self,method,send_value='',handle_value=''):
        method_value = getattr(self.action_method,method)
        if send_value == '' and handle_value !='':
            result = method_value(handle_value)
        elif send_value == '' and handle_value =='':
            result = method_value()
        elif send_value != '' and handle_value =='':
            result = method_value(send_value)
        else:
            result = method_value(send_value,handle_value)
        return result

if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()
    report = CONFIG_FILE + '\\keyword.xls'
    e = Email(title='ERP测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='825651673@qq.com',
              server='smtp.126.com',
              sender='luckyanhui@126.com',
              password='yan986165220',
              path=report
              )
    e.send()
