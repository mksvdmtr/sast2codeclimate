import glob
import json

objects_list = []

sast_files = glob.glob('*-sast.json')

for sast_file in sast_files:
    with open(sast_file, 'r') as sast_infile:
        
        sast_json = json.load(sast_infile)

    for i in sast_json['vulnerabilities']:

        severity = 'info'

        match i['severity']:
            case 'Low':
                severity = 'minor'
            case 'Medium':
                severity = 'major'
            case 'High' | 'Critical':
                severity = 'critical'

        issue_object = {
                "type": "issue",
                "check_name": i['name'],
                "categories": [
                "Security"
                ],
                "description": i['description'] + ' | CVE: '  + i['cve'],
                "fingerprint": i['id'],
                "severity": severity,
                "location": {
                    "path": i['location']['file'],
                    "lines": {
                        "begin": i['location']['start_line']
                    }
                }
            }
        objects_list.append(issue_object)

cc_files = glob.glob('*-cq.json')
for cc_file in cc_files:
    with open(cc_file, 'r') as cc_infile:
        cc_json = json.load(cc_infile)
        for i in cc_json:
            objects_list.append(i)

with open('codequality.json', 'w', encoding='utf-8') as f:
    json.dump(objects_list, f, indent=4)