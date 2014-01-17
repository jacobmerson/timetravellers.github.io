from __future__ import with_statement
from __future__ import print_function
import os
import subprocess
import shutil

class Resume:
    '''
    generates resume for website
    '''
    resume = ''
    css = ''
    site_dir = os.path.abspath(os.path.curdir)
    temp_dir = os.path.abspath('assets/temp')
    res_file = 'resume'
    res_path='~/Documents/resume/resume.tex'

    def createTempFolder(self):
        '''
        creates a temp folder
        changes cwd to temp folder
        '''
        os.mkdir(self.temp_dir)
        os.chdir(self.temp_dir)


    def cleanTempFolder(self):
        '''
        removes temp folder and all internal files
        '''
        os.chdir(os.path.abspath('assets'))
        try:
            os.rmdir(self.temp_dir)
        except:
            for file in os.listdir(self.temp_dir):
                os.remove(os.path.join(self.temp_dir, file))
            os.rmdir(self.temp_dir)
            os.chdir(self.site_dir)


    def generateResume(self):
        '''
        generate html file of resume
        '''
        print('Generate Resume')
        #remove temp
        try:
            self.cleanTempFolder()
        except:
            pass
        self.createTempFolder()
        path = os.path.expanduser(self.res_path)
        with open('res_log.txt','w') as f:
            subprocess.call(['htlatex', path, 'html'], stdout=f);
        os.chdir(self.site_dir)
        shutil.copy(os.path.join(self.temp_dir, self.res_file +'.html'), 'templates/resume_content.html')
