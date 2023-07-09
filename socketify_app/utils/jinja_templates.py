from jinja2 import Environment, FileSystemLoader


class JinjaTemplate:
    """
    Provides support for Jinja2 templates.
    """

    def __init__(self, search_path, encoding="utf-8", follow_links=False):
        self.env = Environment(
            loader=FileSystemLoader(search_path, encoding, follow_links)
        )

    def render(self, template_name, **kwargs) -> str:
        """
        Renders the Jinja2 template.
        """
        try:
            template = self.env.get_template(template_name)
            return template.render(**kwargs)
        except Exception as err:
            return str(err)
