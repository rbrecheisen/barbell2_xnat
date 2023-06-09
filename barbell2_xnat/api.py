import os
import json
import xnat
import time


class XnatApiClient:

    def __init__(self, host, username, password, project_id):
        if not host.startswith('https'):
            self.host = 'https://' + host
        self.session = xnat.connect(self.host, username, password)
        self.project = self.session.projects[project_id]

    def download_subject_data(self, download_dir):
        os.makedirs(download_dir, exist_ok=True)
        subjects = []
        try:
            if os.path.isfile('/tmp/subjects.json'):
                print('loading subjects...')
                with open('/tmp/subjects.json', 'r') as f:
                    subjects = json.load(f)
            for subject_id in self.project.subjects.keys():
                if subject_id not in subjects:
                    print(f'downloading data for subject {subject_id}...')
                    subject = self.project.subjects[subject_id]
                    subject.download_dir(download_dir)
                    subjects.append(subject_id)
        finally:
            print('writing subjects.json...')
            with open('/tmp/subjects.json', 'w') as f:
                json.dump(subjects, f)


if __name__ == '__main__':
    def main():
        project_id = 'nihradiomics'
        # project_id = 'maastrothunder'
        download_directory = f'/Users/Ralph/Desktop/{project_id}'
        password = open(os.environ['HOME'] + '/xnat.bmia.nl.txt', 'r').readline().strip()
        client = XnatApiClient('xnat.bmia.nl', 'rbrecheisen', password, project_id)
        client.download_subject_data(download_directory)
    main()
