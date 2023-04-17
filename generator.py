""" Generate Website """

import os, shutil
from jinja2 import Template, Environment, FileSystemLoader

from tune_data.tune_data import tune_list

class SiteGenerator(object):
    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader('template')
        )

        # Actions to Generate Site
        self.empty_public()
        self.copy_static()
        self.render_main_page()
        self.finished()

    def empty_public(self) -> None:
        """ Ensure the public directory is empty before generating. """
        try:
            shutil.rmtree('./public') 
            os.mkdir('./public')
        except:
            print("Error cleaning up old files.")
    
    def copy_static(self) -> None:
        """ Copy static assets to the public directory """
        try:
            shutil.copytree('template/static', 'public/static')
        except:
            print("Error copying static files.")
    
    def render_main_page(self) -> None:
        """ Create Index Page """
        print("Rendering Main page to static file.")
        template = self.env.get_template('_index.html')
        with open('public/index.html', 'w+') as file:
            html = template.render(
                tune_list = tune_list
            )
            file.write(html)
    
    def finished(self) -> None:
        """ Finished Message """
        print("Finished webpage creation.")

if __name__ == "__main__":
    SiteGenerator()