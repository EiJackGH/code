def test_isatty(capsys):
    import sys
    print("isatty:", sys.stdout.isatty())
