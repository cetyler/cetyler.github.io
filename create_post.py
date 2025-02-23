#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
# ]
# ///

import click
from pathlib import Path
import subprocess
from datetime import date

POST_TYPES = [
    "til",
    "post",
]

@click.command()
@click.argument(
    "post_type",
    type=click.Choice(POST_TYPES, case_sensitive=False,)
)
@click.argument(
    "post_title",
    type=str,
)
@click.option(
    "--post_date",
    default=f"{date.today()}",
    help="Will default to today's date.",
    type=click.DateTime(
        formats=[
            "%Y-%m-%d",
        ]
    )
)
def main(
    post_type: str,
    post_title: str,
    post_date: date,
):
    hugo_folder = Path.cwd()
    
    year = f"{post_date.year}"
    filename = f"{post_date.year}-{post_date.month}-{post_date.day}_{post_title}.md"
    if post_type == "post":
        article_folder = Path.cwd() / "content" / "posts" / year / filename
    else:
        article_folder = Path.cwd() / "content" / "til" / year / filename

    subprocess.call(f"hugo new content {article_folder}",
                    shell=True,
                    )
    subprocess.call(f"/usr/bin/micro {article_folder}", shell=True)

if __name__ == "__main__":
    main()    
