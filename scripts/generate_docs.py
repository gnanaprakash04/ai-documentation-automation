from pathlib import Path

# Read the engineering input
input_file = Path("input/feature-request.md")
input_content = input_file.read_text()

# Create the documentation content
output_content = f"""# Generated Release Note

## Engineering Information

{input_content}

## Documentation Status

This documentation was generated automatically from the engineering input.
"""

# Create the output folder
output_folder = Path("docs/release-notes")
output_folder.mkdir(parents=True, exist_ok=True)

# Write the generated documentation
output_file = output_folder / "generated-release-note.md"
output_file.write_text(output_content)

print("Documentation generated successfully!")
