from cleo import Command


class PypiCommand(Command):
    """
    Check the availability of a package name in PyPI

    pypi
        {name : What package name do you want to see if it's available?}
    """

    def handle(self):
        name = self.argument("name")

        self.line(name)
