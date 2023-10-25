DESKTOP_TEMPLATE = """
[Desktop Entry]

# The type as listed above
Type={entry_type}

# The version of the desktop entry specification to which this file complies
Version={version}

# The name of the application
Name={app_name}

# A comment which can/will be used as a tooltip
Comment={comment}

# The path to the folder in which the executable is run
# Path=<path_to_executable>

# The executable of the application, possibly with arguments.
Exec={executable}

# The name of the icon that will be used to display this entry
Icon={icon_path}

# Describes whether this application needs to be run in a terminal or not
Terminal={is_terminal}

# Describes the categories in which this entry should be shown
Categories={categories}
"""
