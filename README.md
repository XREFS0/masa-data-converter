# MASA DataMorph Converter

Universal tabular and hierarchical data format converter bridging JSON, CSV, XML, and Excel

## Technical Architecture

The application is architected with modular separation of concerns adhering to modern clean code standards:

- **Component Layering**: Isolated view layouts, state managers, and service controllers.
- **Defensive Engineering**: Robust input sanitization and exception management.
- **Modern Design Standards**: High-contrast dark-mode interface styled for optimal usability and visual polish.

## Preview

![Application Interface](screenshots/app_interface.png)

## Features

- Bidirectional schema conversion across CSV, JSON, XML, and XLSX.
- Automatic data type inference and tabular preview grid.
- Batch translation pipeline for directory-wide document transformation.
- Syntax validation catching malformed formatting prior to processing.

## Prerequisites

- Python 3.10 or higher
- Required packages:

```bash
pip install customtkinter pillow requests
```

## Execution

Launch the application via Python:

```bash
python "File Data Converter in Python/index.py"
```

## Project Structure

```
.
├── File Data Converter in Python
├── screenshots/
│   └── app_interface.png
├── .gitignore
├── LICENSE             # MIT License
└── README.md           # Developer documentation
```

## License

This project is licensed under the terms of the MIT License. Refer to the `LICENSE` file for details.
