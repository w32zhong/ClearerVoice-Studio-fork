import argparse

from clearvoice import ClearVoice


DEFAULT_INPUT = "clearvoice/samples/input.wav"
DEFAULT_OUTPUT = "./output"


class HelpFormatter(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawDescriptionHelpFormatter,
):
    """Show argument defaults while preserving multiline help text."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Enhance a speech recording with ClearVoice.",
        formatter_class=HelpFormatter,
        epilog=(
            "Examples:\n"
            "  python cli.py\n"
            "  python cli.py path/to/input.wav path/to/output.wav"
        ),
    )
    parser.add_argument(
        "input",
        nargs="?",
        default=DEFAULT_INPUT,
        help="path to the input audio file",
    )
    parser.add_argument(
        "output",
        nargs="?",
        default=DEFAULT_OUTPUT,
        help="path where the enhanced audio file will be written",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    voice = ClearVoice(
        task="speech_enhancement",
        model_names=["MossFormer2_SE_48K"],
    )

    voice(input_path=args.input, online_write=True, output_path=args.output)


if __name__ == "__main__":
    main()
