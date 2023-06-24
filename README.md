



# Erste Vorlage vorgegeben

- Article 
- A4
- German
- Einige usepackages
- Formatierung

# Basis Funktion

Das `jinja_helper.py` enthält die Funktion `render_latex_table`. Diese Funktion übernimmt das Rendern der $LaTeX$ Templates.

```python
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
```

## Quellen
Ursprüngliche Quelle: Hossein Roshandel / July 19, 2022 https://www.hossein.codes/post/eKZMKla4 (hier leicht angepasst).
Weitere Infos bei der Tex User Group von Uwe Ziegenhagen 2019 https://tug.org/tug2019/slides/slides-ziegenhagen-python.pdf.

# Beispiel 1: Parameter

In diesem Beispiel wird nur ein Parameter zu Vorlage hinzugefügt und gerendert.


# Beispiel 2: Dictionary

In diesem Beispiel wird ein Python Dictionary mit mehreren Variablen übergeben und gerendert.


# Beispiel 3: Dict Erweiterung um Arrays



# Beispiel 4: Einbinden von Tabellen



# Beispiel 5: Erweiterte Tabellen



