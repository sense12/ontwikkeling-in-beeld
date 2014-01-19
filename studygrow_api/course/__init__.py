from course_model import Course
from course_model import Assignment

"""

    <assignments>
        {% for assignment in assignments %}
        <assignment>
            <id>{{ assignment.uid }}</id>
            <title>{{ assignment.title }}</title>
            <weight>{{ assignment.weight }}</weight>

            {% for child in assignment.childs %}
            <child>
                <id>{{ child.uid }}</id>
                <title>{{ child.title }}</title>
                <weight>{{ child.weight }}</weight>
            </child>
            {% endfor %}
        </assignment>
        {% endfor %}
    </assignments>
"""
