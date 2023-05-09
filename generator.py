""" Generate Website """

import os, shutil
from jinja2 import Template, Environment, FileSystemLoader

from tune_data.tune_data import tune_list, tune_list_alphab, tune_dict
from tune_data.model.tune import tune_types
from tune_data.sets_data import set_list

class SiteGenerator(object):
    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader('template')
        )

        # Actions to Generate Site
        self.empty_public()
        self.copy_static()
        self.render_main_page()
        self.render_tune_page()
        self.render_tune_index_page()
        self.render_todo_page()
        self.render_submit_a_tune_page()
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
                tune_types = ['reel','jig','slip jig','polka','slide','mazurka','waltz'],
                set_list = set_list
            )
            file.write(html)
    
    def render_tune_page(self) -> None:
        """ Create Tune Page """
        print("Rendering Tune page to static file.")
        template = self.env.get_template('_tune.html')
        with open('public/tune.html', 'w+') as file:
            html = template.render(
                tune_types = tune_types,
                tune_list = tune_list_alphab
            )
            file.write(html)
    
    def render_tune_index_page(self) -> None:
        """ Create tune index Page """
        print("Rendering index page to static file.")
        template = self.env.get_template('_tune_index.html')
        with open('public/tune_index.html', 'w+') as file:
            html = template.render(
                tune_list = tune_list_alphab
            )
            file.write(html)
    
    def render_todo_page(self) -> None:
        """ Create Todo Page """
        print("Rendering Todo page to static file.")
        template = self.env.get_template('_todo.html')
        with open('public/todo.html', 'w+') as file:
            html = template.render()
            file.write(html)
    
    def render_submit_a_tune_page(self) -> None:
        """ Create Submit a Tune Page """
        print("Rendering Submit a Tune page to static file.")
        template = self.env.get_template('_submit_a_tune.html')
        with open('public/submit-a-tune.html', 'w+') as file:
            html = template.render()
            file.write(html)
    
    def finished(self) -> None:
        """ Finished Message """
        print("Finished webpage creation.")

if __name__ == "__main__":
    SiteGenerator()