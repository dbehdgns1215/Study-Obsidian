old_emails = [
    b'63277906+ArinKim@users.noreply.github.com',
    b'dbehdgns1215',
    b'dbehdgns1215@naver.com'
]

def callback(commit):
    if commit.author_email in old_emails:
        commit.author_name = b'Dongni'
        commit.author_email = b'77192122+dbehdgns1215@users.noreply.github.com'
        commit.committer_name = b'Dongni'
        commit.committer_email = b'77192122+dbehdgns1215@users.noreply.github.com'
