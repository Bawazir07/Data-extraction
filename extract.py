# fileName = input('Please enter file name: ')
import os

ward = input("Give ward pointer to review only func_max_lowvcc timing report: ")
ward.strip();
area = os.getenv('PWD');
fileName = 'report.txt'
full_path = os.path.join(ward,fileName)

input_file = open(full_path, 'r', encoding='utf8')

file_text = input_file.read().split('\n\n\n')[1]

output_text = "Scenario           'func_max_lowvcc'\n"
for scenario in file_text.split('Scenario')[1:]:
    if "           'func_max_lowvcc'" in scenario:
        scenario = scenario.replace('----------------------------------------', '')
        scenario = scenario.split('\n', 1)[1].replace('\n\n', '\n')
        sc_lines = scenario.split('\n')
        scenario = []
        for line in sc_lines:
            if any(x in line for x in ['Timing Path Group', 'Critical Path Slack', 'Total Negative Slack', 'No. of Violating Paths']):
                scenario.append(line)
        scenario = '\n'.join(scenario)
        output_text += scenario.strip() + '\n\n'

with open('output.txt', 'w+') as file:
    file.write(output_text)

print("making the script generic")
