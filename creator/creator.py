import click
import pprintpp as pp
import strip

# Initialize click
@click.command()

# Main program
def creator():
    umbrella_specification = dict()
    project_name, project_note = None, None

    print("\nThis is a Umbrella Specification Creation command line tool for software preservation.\n"
          "This program will look for information on your system and determine what information is\n"
          "needed for writing a Umbrella Specification file.\n")

    # Get Project Name and Description
    project = strip.get_project()

    umbrella_specification['comment'] = project['name']
    umbrella_specification['note'] = project['note']

    # Get Kernel
    kernel = strip.get_kernel()
    umbrella_specification.update({"kernel": kernel})

    # Get Hardware
    hardware = strip.get_hardware()
    umbrella_specification.update({"hardware": hardware})

    # Get Operating System
    os = strip.get_os()
    umbrella_specification.update({"os": os})

    # Get Software
    software = strip.get_os()
    umbrella_specification.update({"software": software})

    # Get Data
    data = strip.get_data()
    umbrella_specification.update({"data": data})

    # Get Environmental Variables
    environ = strip.get_environ()
    # pp.pprint(environ)

    pp.pprint(umbrella_specification)

    if click.confirm("Would you like to edit your environmental variables?"):
        new_environ = strip.edit_environ(environ)

        umbrella_specification.update({"environ": new_environ})
    else:
        umbrella_specification.update({"environ": environ})

    pp.pprint(umbrella_specification)

if __name__ == "__main__":
    creator()