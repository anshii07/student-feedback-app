import os

def test_index_file_exists():
    assert os.path.exists("index.html")

def test_css_file_exists():
    assert os.path.exists("style.css")

def test_javascript_file_exists():
    assert os.path.exists("script.js")

def test_name_field():
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()

    assert 'id="name"' in content

def test_course_field():
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()

    assert 'id="course"' in content

def test_feedback_field():
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()

    assert 'id="feedback"' in content

def test_submit_button():
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()

    assert 'type="submit"' in content