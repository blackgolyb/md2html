from pathlib import Path

import click
import markdown
from jinja2 import Template

from services.base.apps_controller import AppsController
import config


def decorate_html(html, title):
    with open(config.template_file, "r", encoding="utf-8") as html_template_file:
        template = Template(html_template_file.read())

    styles = ""
    for css_file in config.css_files:
        with open(css_file, "r", encoding="utf-8") as styles_file:
            styles += styles_file.read() + "\n\n"

    scripts = ""
    for js_file in config.js_files:
        with open(js_file, "r", encoding="utf-8") as scripts_file:
            scripts += scripts_file.read() + "\n\n"

    controller = AppsController()
    controller.load_apps_from_dir()
    styles += controller.get_styles()
    scripts += controller.get_scripts()

    return template.render(
        title=title, styles=styles, scripts=scripts, markdown_html=html
    )


def md_to_html(input_file, output_file, title):
    with input_file.open("r", encoding="utf-8") as md_file:
        md_text = md_file.read()

    md_html = markdown.markdown(
        md_text,
        extensions=config.extensions,
        extension_configs=config.extensions_config,
    )
    md_html = decorate_html(md_html, title)

    with output_file.open(
        "w", encoding="utf-8", errors="xmlcharrefreplace"
    ) as html_file:
        html_file.write(md_html)


@click.command()
@click.help_option("-h", "--help")
@click.option(
    "--input",
    "-i",
    "input_file",
    help="Input markdown file path.",
    type=click.Path(file_okay=True, exists=True),
)
@click.option(
    "--output",
    "-o",
    "output_file",
    default=None,
    help="Output html file path.",
    type=click.Path(),
)
@click.option(
    "--title",
    "-t",
    "title",
    default=None,
    help="Title of the result file.",
    type=str,
)
def md_to_html_cli(input_file, output_file, title):
    input_file = Path(input_file)

    if output_file is None:
        output_file = input_file.parent / f"{input_file.stem}.html"
    else:
        output_file = Path(output_file)

    if title is None:
        title = output_file.stem

    if not output_file.parent.exists():
        click.echo(
            f"Error: Output file dir dose not exists. Path: {output_file.parent}",
            err=True,
        )
        return

    md_to_html(input_file, output_file, title)


def main():
    md_to_html_cli()


if __name__ == "__main__":
    main()
