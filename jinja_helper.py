import jinja2
import os

def render_latex_table(input_data, templatefile=''):
    """Receives a table in the form of a DataFrame and converts it to a string containing the Latex code for the standalone table """
    latex_jinja_env = jinja2.Environment(
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
        loader = jinja2.FileSystemLoader(os.path.abspath('.'))
    )

    template = latex_jinja_env.get_template(templatefile)
    return template.render(input_data=input_data)

