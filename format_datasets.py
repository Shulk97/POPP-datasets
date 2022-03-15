import click
import json
from copy import deepcopy
from pathlib import Path

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("CLI invoked without subcommand")
    else:
        click.echo("Launching of command: %s" % ctx.invoked_subcommand)

@cli.command()
@click.option("--json_name", default="labels.json", help="Name of the json label file")
@click.option("--keep_col_sep", is_flag=True, help="Whether to keep column separator character")
@click.option("--rm_ool_chars", is_flag=True, help="Whether to remove out of line chars")
def formatdataset(json_name: str, keep_col_sep=True, rm_ool_chars=False):
    """
    Prepare labels for training by removing column separators or out-of-line characters
    """
    with open(json_name, "r") as f:
        info = json.load(f)

    charset = set()

    new_dict = deepcopy(info)

    for split_name, split_dict in info["ground_truth"].items():
        for key in split_dict:
            #remove annotation of out-of-line words:
            if rm_ool_chars:
                for char in ["!", "?"]:
                    if char in split_dict[key]["text"]:
                        cell_labels = split_dict[key]["text"].split("/")
                        for i, cell_label in enumerate(cell_labels):
                            if char in cell_label:# and cell_label != "?":
                                cell_labels[i] = cell_label[: cell_label.find(char)]
                        split_dict[key]["text"] = "/".join(cell_labels)

            if not keep_col_sep:
                # remove column separator characters
                split_dict[key]["text"] = split_dict[key]["text"].replace("/", " ").replace("¤", "")

            # update the charset:
            line_charset = set([character for character in split_dict[key]["text"]])
            charset = charset.union(line_charset)

        new_dict['ground_truth'][split_name]=split_dict
    # we replace the old charset with the new one deduced from the new labels:
    new_dict["charset"] = sorted(list(charset))

    output_name = Path(json_name).parent.joinpath("formatted_" + Path(json_name).name)
    with open(output_name, "w") as f:
        json.dump(new_dict, f)

if __name__ == "__main__":
    cli()