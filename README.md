#Alfred Workflows
Various workflows and utilities for [Alfred 2 Beta](http://v2.alfredapp.com/)

##Workflows:
* **wiki**: Wikipedia auto-complete search
* **pyshell**: Evaluates python code and copies result to clipboard

##Utilities
* **feedback**: Class for creating python Feedback for Alfred script filter

    ```python
    from alfred_utils import feedback
    fb = feedback.Feedback()
    fb.add_item('Hello', 'World')
    fb.add_item('Foo', 'Bar')
    print fb
    ```

## Install
Run the linker.sh script to create symbolic for all workflows

    sh linker.sh

Alternatively you can create alfredworkflow file by zipping any individual workflow

    cd workflows/pyshell; zip -r pyshell.alfredworkflow .
