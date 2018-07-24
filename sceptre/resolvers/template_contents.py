# -*- coding: utf-8 -*-

from sceptre.resolvers import Resolver


import os
import jinja2
import json
import yaml


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


def resolve_yaml(yamlFile, context={}):
    thefile = open(yamlFile, 'r')
    rendered_file = render(yamlFile,context)
    return yaml.safe_load(rendered_file)


class TemplateContents(Resolver):
    """
    Resolver for the contents of a file.

    :param argument: Absolute path to file.
    :type argument: str
    """

    def __init__(self, *args, **kwargs):
        super(TemplateContents, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        Retrieves the contents of a file at a given absolute file path.

        :returns: Contents of file.
        :rtype: str
        """
        from pprint import pprint
        print('get stack info ....')
        print(self.stack.stack_config)

        try:
            return resolve_yaml(self.argument, self.stack.stack_config['user_data'])
        except (EnvironmentError, TypeError) as e:
            raise e
