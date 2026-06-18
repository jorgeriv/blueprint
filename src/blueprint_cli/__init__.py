from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from importlib import resources
from importlib.abc import Traversable
from pathlib import Path


BLUEPRINT_DIR = ".blueprint"
CONFIG_FILE = "config.json"
AGENTS_SKILLS_DIR = Path(".agents") / "skills"


@dataclass(frozen=True)
class CopyResult:
    created: list[Path]
    skipped: list[Path]
    overwritten: list[Path]


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="blueprint",
        description="Initialize Blueprint project definition workspaces.",
    )
    subcommands = parser.add_subparsers(dest="command", required=True)

    init_parser = subcommands.add_parser(
        "init",
        help="Create Blueprint definition folders and placeholder files.",
    )
    init_parser.add_argument(
        "project_name",
        nargs="?",
        help="Project directory to create. Use '.' or --here for the current directory.",
    )
    init_parser.add_argument(
        "--here",
        action="store_true",
        help="Initialize Blueprint in the current directory.",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing scaffold files.",
    )

    args = parser.parse_args(argv)

    if args.command == "init":
        init_project(args.project_name, here=args.here, force=args.force)


def init_project(project_name: str | None, *, here: bool = False, force: bool = False) -> None:
    if project_name == ".":
        here = True
        project_name = None

    if here and project_name:
        raise SystemExit("Error: use either a project name or --here, not both.")

    if not here and not project_name:
        raise SystemExit("Error: provide a project name, '.', or --here.")

    project_path = Path.cwd() if here else Path(project_name).resolve()
    project_path.mkdir(parents=True, exist_ok=True)

    scaffold_result = copy_scaffold(project_path, force=force)
    skills_result = copy_skills(project_path, force=force)
    write_config(project_path, force=force)

    print(f"Blueprint initialized at {project_path}")
    print(
        "Definition files: "
        f"{len(scaffold_result.created)} created, "
        f"{len(scaffold_result.skipped)} skipped, "
        f"{len(scaffold_result.overwritten)} overwritten"
    )
    print(
        "Skills: "
        f"{len(skills_result.created)} created, "
        f"{len(skills_result.skipped)} skipped, "
        f"{len(skills_result.overwritten)} overwritten"
    )
    print()
    print("Next step: use $blueprint-kickstart-idea to turn a raw idea into a project north star.")


def copy_scaffold(project_path: Path, *, force: bool = False) -> CopyResult:
    scaffold_root = resources.files(__package__).joinpath("templates/scaffold")
    return copy_resource_tree(scaffold_root, project_path, force=force)


def copy_skills(project_path: Path, *, force: bool = False) -> CopyResult:
    skills_root = locate_skills_root()
    destination_root = project_path / AGENTS_SKILLS_DIR
    return copy_resource_tree(skills_root, destination_root, force=force)


def copy_resource_tree(
    resource_root: Traversable,
    destination_root: Path,
    *,
    force: bool = False,
) -> CopyResult:
    created: list[Path] = []
    skipped: list[Path] = []
    overwritten: list[Path] = []

    for source, relative_path in walk_resources(resource_root):
        destination = destination_root / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)

        existed = destination.exists()

        if existed and not force:
            skipped.append(relative_path)
            continue

        content = source.read_text(encoding="utf-8")
        destination.write_text(content, encoding="utf-8")

        if existed:
            overwritten.append(relative_path)
        else:
            created.append(relative_path)

    return CopyResult(created=created, skipped=skipped, overwritten=overwritten)


def locate_skills_root() -> Traversable:
    bundled = resources.files(__package__).joinpath("skills")
    if bundled.is_dir():
        return bundled

    source_checkout = Path(__file__).resolve().parents[2] / "skills"
    if source_checkout.is_dir():
        return source_checkout

    raise SystemExit("Error: Blueprint skills could not be found in this installation.")


def walk_resources(root: Traversable) -> list[tuple[Traversable, Path]]:
    files: list[tuple[Traversable, Path]] = []

    def visit(node: Traversable, relative_parts: tuple[str, ...]) -> None:
        if node.is_file():
            files.append((node, Path(*relative_parts)))
            return

        for child in node.iterdir():
            visit(child, (*relative_parts, child.name))

    visit(root, ())
    return files


def write_config(project_path: Path, *, force: bool = False) -> None:
    config_path = project_path / BLUEPRINT_DIR / CONFIG_FILE
    config_path.parent.mkdir(parents=True, exist_ok=True)

    if config_path.exists() and not force:
        return

    config = {
        "schema": "blueprint.project-definition",
        "version": "0.1.0",
        "definition_dir": "definition",
        "placeholder_policy": "initializer creates structure; skills create substantive content",
    }
    config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
