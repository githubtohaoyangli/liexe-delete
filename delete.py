import shutil
import os
b=None     
while True:
    if b ==None:
        print('uninstall liexe 1.0.1')
        print('The exe removes all liexe files(uninstall liexe),continue?(If you continue, press continue, if you exit, press exit)')
    b= input()
    if b=='exit':
        exit(0)
    elif b == 'continue':
        if os.path.exists('C:\\liexee'):
            shutil.rmtree('C:\\liexee')
            os.system('pause') 
            exit(0)  
        else:
            print('Cannot find the liexe files.')
            os.system('pause')
            exit(0)
    else:
        print('ERROR,void')       