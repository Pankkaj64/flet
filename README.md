# Flet UI Examples

Two small Python apps built with [Flet](https://flet.dev), a framework for building Flutter-based user interfaces in pure Python. The project shows how to compose controls, handle events and update the page state: an increment/decrement counter and a sign-up form with live validation. Both apps open in the web browser.

## Features

- **Counter app (`main.py`)**
  - Dark-themed page with a number field between minus and plus icon buttons
  - Clicking the buttons decrements or increments the value and refreshes the page
- **Sign-up form (`login.py`)**
  - Light-themed, fixed-size (400 x 400) window with username, password (masked) and an "I agree" checkbox
  - The **Sign up** button stays disabled until all three fields are filled in, re-validated on every change
  - On submit, the form is cleared from the page and replaced with a welcome message for the user

## Tech Stack

- Python 3
- Flet (Flutter UI rendered from Python)

## Project Structure

```
.
├── main.py    # Increment / decrement counter app
└── login.py   # Sign-up form with input validation
```

## How it works

Each script defines a `main(page: ft.Page)` function that configures the page (title, theme, alignment), builds controls such as `TextField`, `IconButton`, `Checkbox` and `ElevatedButton`, and wires event handlers (`on_click`, `on_change`). Handlers mutate control properties and call `page.update()` to re-render. The app is started with `ft.app(target=main, view=ft.AppView.WEB_BROWSER)`.

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Install

```bash
git clone https://github.com/Pankkaj64/flet.git
cd flet
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install flet
```

Note: the scripts import `ControlEvent` from the `flet_core` module, which recent Flet releases no longer provide. If you get an import error, install an earlier Flet version that still includes `flet_core`.

### Run

```bash
python main.py     # counter app
python login.py    # sign-up form
```

Each command starts a local Flet server and opens the app in your default web browser.

## Usage

- **Counter:** click `-` or `+` to change the number.
- **Sign-up:** enter a username and password, tick the checkbox to enable **Sign up**, then submit to see the welcome screen.
