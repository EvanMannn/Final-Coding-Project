import numpy as np
writing_score_array_with_header=np.genfromtxt('Writing Scores.csv', delimiter=',', encoding='utf-8', dtype=str)

focus_group_choices={}
for i in range(1,6):
    focus_group = writing_score_array_with_header[0,i].title()
    sub_sections = []
    for item in writing_score_array_with_header[1:, i]:
        if item not in sub_sections:
            sub_sections.append(item)
    print(focus_group)
    print(sub_sections)
    focus_group_choices[focus_group]=sub_sections
